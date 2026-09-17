from __future__ import annotations

import queue
import shutil
import stat
import subprocess
import sys
import threading
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / ".cache/minecraft/26.3/integration-server"
WORLD = SERVER / "validation-world-3"
PACKS = WORLD / "datapacks"


# Offers are generated when a villager takes a profession through its brain, not
# when VillagerData is written directly, so the test builds a floor, puts down a
# real job site, and waits for the villager to claim it.
COMMANDS = [
    # forceload add 200 0 loads exactly one chunk: x 192-207, z 0-15. Villagers
    # placed outside it never tick and never take a profession.
    "execute in minecraft:overworld run forceload add 200 0",
    "execute in minecraft:overworld run kill @e[type=villager]",
    "execute in minecraft:overworld run fill 194 99 0 206 99 15 minecraft:stone",
    "execute in minecraft:overworld run fill 194 100 0 206 102 15 minecraft:air",
    "execute in minecraft:overworld run setblock 198 100 1 minecraft:barrel",
    "execute in minecraft:overworld run setblock 198 100 5 minecraft:lectern",
    "execute in minecraft:overworld run setblock 198 100 9 minecraft:stonecutter",
    "execute in minecraft:overworld run setblock 198 100 13 minecraft:brewing_stand",
    "execute in minecraft:overworld run setblock 204 100 1 minecraft:cartography_table",
    "execute in minecraft:overworld run setblock 204 100 9 minecraft:blast_furnace",
    'execute in minecraft:overworld run summon minecraft:villager 197 100 1 {Invulnerable:1b,Tags:["sav.test"]}',
    'execute in minecraft:overworld run summon minecraft:villager 197 100 5 {Invulnerable:1b,Tags:["sav.books"]}',
    'execute in minecraft:overworld run summon minecraft:villager 197 100 9 {Invulnerable:1b,Tags:["sav.mason"]}',
    'execute in minecraft:overworld run summon minecraft:villager 197 100 13 {Invulnerable:1b,Tags:["sav.cleric"]}',
    'execute in minecraft:overworld run summon minecraft:villager 203 100 1 {Invulnerable:1b,Tags:["sav.carto"]}',
    'execute in minecraft:overworld run summon minecraft:villager 203 100 9 {Invulnerable:1b,Tags:["sav.armorer"]}',
    "WAIT:90",
    "data get entity @e[type=villager,tag=sav.test,limit=1] VillagerData",
    "data get entity @e[type=villager,tag=sav.mason,limit=1] VillagerData",
    "data get entity @e[type=villager,tag=sav.cleric,limit=1] VillagerData",
    "data get entity @e[type=villager,tag=sav.test,limit=1] Offers.Recipes",
    'execute if data entity @e[type=villager,tag=sav.test,limit=1] Offers.Recipes[{buy:{id:"minecraft:birch_log",count:64}}] run say CHECK Fisherman birch trade present',
    'execute if data entity @e[type=villager,tag=sav.test,limit=1] Offers.Recipes[{maxUses:100000}] run say CHECK Unlimited uses present',
    # A zero priceMultiplier equals the codec default, so it is omitted from the
    # NBT entirely. Vanilla fisherman trades carry 0.05; its absence is the check.
    'execute unless data entity @e[type=villager,tag=sav.test,limit=1] Offers.Recipes[{priceMultiplier:0.05f}] run say CHECK Reputation discount zeroed',
    'execute if data entity @e[type=villager,tag=sav.test,limit=1] Offers.Recipes[{buy:{id:"minecraft:ancient_debris"}}] run say CHECK Full catalog available at level one',
    'execute unless data entity @e[type=villager,tag=sav.test,limit=1] Offers.Recipes[{buy:{id:"minecraft:coal"}}] run say CHECK No vanilla fisherman trades leaked in',
    'execute if data entity @e[type=villager,tag=sav.mason,limit=1] Offers.Recipes[{sell:{id:"minecraft:end_stone",count:64}}] run say CHECK Mason sells End Stone at 64',
    'execute if data entity @e[type=villager,tag=sav.cleric,limit=1] Offers.Recipes[{buy:{id:"minecraft:emerald",count:8},sell:{id:"minecraft:ender_pearl"}}] run say CHECK Cleric Ender Pearl priced at 8',
    'execute if data entity @e[type=villager,tag=sav.cleric,limit=1] Offers.Recipes[{sell:{id:"minecraft:bone",count:32}}] run say CHECK Cleric Bone at 32 not 64',
    'execute unless data entity @e[type=villager,tag=sav.cleric,limit=1] Offers.Recipes[{sell:{id:"minecraft:rabbit_hide"}}] run say CHECK Rabbit Hide not both bought and sold',
    'execute if data entity @e[type=villager,tag=sav.carto,limit=1] Offers.Recipes[{buy:{id:"minecraft:emerald",count:16}}] run say CHECK Cartographer maps priced at 16',
    'execute if data entity @e[type=villager,tag=sav.armorer,limit=1] Offers.Recipes[{sell:{id:"minecraft:iron_chestplate"},buy:{count:3}}] run say CHECK Armorer Iron Chestplate derived at 3',
    'execute unless data entity @e[type=villager,tag=sav.armorer,limit=1] Offers.Recipes[{sell:{id:"minecraft:diamond_chestplate"}}] run say CHECK Equipment stops at Iron',
    "data get entity @e[type=villager,tag=sav.books,limit=1] VillagerData",
]


EXPECTED_MARKERS = [
    "CHECK Fisherman birch trade present",
    "CHECK Unlimited uses present",
    "CHECK Reputation discount zeroed",
    "CHECK Full catalog available at level one",
    "CHECK No vanilla fisherman trades leaked in",
    "CHECK Mason sells End Stone at 64",
    "CHECK Cleric Ender Pearl priced at 8",
    "CHECK Cartographer maps priced at 16",
    "CHECK Armorer Iron Chestplate derived at 3",
    "CHECK Equipment stops at Iron",
    "CHECK Cleric Bone at 32 not 64",
    "CHECK Rabbit Hide not both bought and sold",
]

# "Missing data pack" is expected noise: the shared validation world still
# lists the Enchanting and FancyUI packs in its level.dat.
ERROR_PATTERNS = (
    "Failed to load datapacks",
    "Failed to parse",
    "Registry loading errors",
    "Serialization errors",
    "Couldn't parse",
    "Unknown function",
)


def remove_readonly(function: object, path: str, _: object) -> None:
    Path(path).chmod(stat.S_IWRITE)
    function(path)  # type: ignore[operator]


def main() -> int:
    eula = SERVER / "eula.txt"
    if not eula.exists() or "eula=true" not in eula.read_text(encoding="utf-8"):
        print("The disposable server EULA has not been explicitly accepted.", file=sys.stderr)
        return 2

    PACKS.mkdir(parents=True, exist_ok=True)
    for existing in PACKS.iterdir():
        if existing.is_dir():
            shutil.rmtree(existing, onexc=remove_readonly)
    shutil.copytree(
        ROOT / "SuperAwesomeVillagers",
        PACKS / "SuperAwesomeVillagers",
        ignore=shutil.ignore_patterns(".git", "third_party"),
    )

    process = subprocess.Popen(
        ["java", "-Xmx2G", "-jar", "server.jar", "--nogui"],
        cwd=SERVER,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )
    assert process.stdin is not None
    assert process.stdout is not None

    lines: queue.Queue[str | None] = queue.Queue()

    def read_output() -> None:
        for line in process.stdout:
            lines.put(line.rstrip())
        lines.put(None)

    threading.Thread(target=read_output, daemon=True).start()
    captured: list[str] = []
    deadline = time.monotonic() + 180
    ready = False
    while time.monotonic() < deadline:
        try:
            line = lines.get(timeout=1)
        except queue.Empty:
            continue
        if line is None:
            break
        captured.append(line)
        print(line)
        if "Done (" in line:
            ready = True
            break

    if ready:
        for command in COMMANDS:
            if command.startswith("WAIT:"):
                seconds = float(command[5:])
                print(f"> waiting {seconds:.0f}s for villagers to claim a job site")
                time.sleep(seconds)
                continue
            print(f"> {command}")
            process.stdin.write(command + "\n")
            process.stdin.flush()
            time.sleep(2 if ("forceload" in command or "summon" in command or "fill " in command) else 0.4)
        process.stdin.write("stop\n")
        process.stdin.flush()

    try:
        process.wait(timeout=60)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=20)

    while True:
        try:
            line = lines.get_nowait()
        except queue.Empty:
            break
        if line is not None:
            captured.append(line)
            print(line)

    errors = [line for line in captured if any(p in line for p in ERROR_PATTERNS)]
    if errors:
        print("\n=== DATAPACK ERRORS ===", file=sys.stderr)
        for line in errors:
            print(line, file=sys.stderr)
        return 1
    if not ready:
        print("Server never reached Done", file=sys.stderr)
        return 1
    missing = [m for m in EXPECTED_MARKERS if not any(m in line for line in captured)]
    if missing:
        print(f"Missed expected results: {missing}", file=sys.stderr)
        return 1
    print("\nAll checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
