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
SERVER = ROOT / ".cache/minecraft/26.3-rc2/integration-server"
WORLD = SERVER / "validation-world-3"
PACKS = WORLD / "datapacks"


COMMANDS = [
    "execute in minecraft:overworld run forceload add 80 0",
    "execute in minecraft:overworld positioned 80 100 0 run kill @e[type=marker,distance=..2]",
    "execute in minecraft:overworld positioned 80 100 0 run function sae:workstation/place/create",
    "execute in minecraft:overworld positioned 80 100 0 run tag @e[type=marker,tag=sae.workstation,distance=..2,limit=1] remove sae.workstation",
    "execute in minecraft:overworld positioned 80 100 0 run tag @e[type=marker,tag=fancyui.container.watch,distance=..2,limit=1] remove fancyui.container.watch",
    "item replace block 80 100 0 container.10 with minecraft:diamond_sword",
    "item replace block 80 100 0 container.12 with minecraft:amethyst_block",
    "data get block 80 100 0 CustomName",
    "execute in minecraft:overworld if data block 80 100 0 {CustomName:\"Super Awesome Enchanting\"} run say UI title component passed",
    "execute in minecraft:overworld if data block 80 100 0 Items[{Slot:0b,components:{\"minecraft:custom_name\":{text:\"Armor recipes\"}}}] run say UI button text passed",
    "execute in minecraft:overworld unless data block 80 100 0 Items[{Slot:0b}].components.\"minecraft:tooltip_display\" run say UI tooltip visibility passed",
    "execute in minecraft:overworld positioned 80 100 0 if data entity @e[type=marker,tag=fancyui.container,distance=..2,limit=1] data.watch[{Slot:10b,criteria:\"*\"}] run say UI watch criteria passed",
    "execute in minecraft:overworld positioned 80 100 0 as @e[type=marker,tag=fancyui.container,distance=..2,limit=1] at @s run function sae:workstation/render",
    "execute in minecraft:overworld positioned 80 100 0 run data get entity @e[type=marker,tag=fancyui.container,distance=..2,limit=1] data.sae",
    "execute in minecraft:overworld positioned 80 100 0 as @e[type=marker,tag=fancyui.container,distance=..2,limit=1] at @s run function sae:enchant/apply",
    "data get block 80 100 0 Items[{Slot:10b}]",
    "execute in minecraft:overworld run loot spawn 80 102 0 loot minecraft:chests/abandoned_mineshaft",
    "execute in minecraft:overworld run forceload add 96 0",
    "execute in minecraft:overworld positioned 96 100 0 run kill @e[type=marker,distance=..2]",
    "execute in minecraft:overworld positioned 96 100 0 run function sae:workstation/place/create",
    "execute in minecraft:overworld positioned 96 100 0 run tag @e[type=marker,tag=sae.workstation,distance=..2,limit=1] remove sae.workstation",
    "execute in minecraft:overworld positioned 96 100 0 run tag @e[type=marker,tag=fancyui.container.watch,distance=..2,limit=1] remove fancyui.container.watch",
    'item replace block 96 100 0 container.10 with minecraft:diamond_sword[minecraft:enchantments={"minecraft:sharpness":5,"minecraft:unbreaking":3}]',
    "item replace block 96 100 0 container.12 with minecraft:amethyst_block",
    'item replace block 96 100 0 container.14 with minecraft:netherite_sword[minecraft:enchantments={"minecraft:mending":1}]',
    "execute in minecraft:overworld positioned 96 100 0 run data modify entity @e[type=marker,tag=fancyui.container,distance=..2,limit=1] data.sae.mode set value \"transfer\"",
    "execute in minecraft:overworld positioned 96 100 0 as @e[type=marker,tag=fancyui.container,distance=..2,limit=1] at @s run function sae:workstation/render",
    "execute in minecraft:overworld positioned 96 100 0 run data get entity @e[type=marker,tag=fancyui.container,distance=..2,limit=1] data.sae",
    "execute in minecraft:overworld positioned 96 100 0 as @e[type=marker,tag=fancyui.container,distance=..2,limit=1] at @s run function sae:transfer/apply",
    "data get block 96 100 0 Items[{Slot:14b}]",
    "execute in minecraft:overworld run forceload add 112 0",
    "execute in minecraft:overworld positioned 112 100 0 run kill @e[type=marker,distance=..2]",
    "execute in minecraft:overworld positioned 112 100 0 run function sae:workstation/place/create",
    "execute in minecraft:overworld positioned 112 100 0 run tag @e[type=marker,tag=sae.workstation,distance=..2,limit=1] remove sae.workstation",
    "execute in minecraft:overworld positioned 112 100 0 run tag @e[type=marker,tag=fancyui.container.watch,distance=..2,limit=1] remove fancyui.container.watch",
    "item replace block 112 100 0 container.10 with minecraft:book",
    "item replace block 112 100 0 container.12 with minecraft:amethyst_block",
    "execute in minecraft:overworld positioned 112 100 0 as @e[type=marker,tag=fancyui.container,distance=..2,limit=1] at @s run function sae:workstation/render",
    "execute in minecraft:overworld positioned 112 100 0 as @e[type=marker,tag=fancyui.container,distance=..2,limit=1] at @s run function sae:enchant/apply",
    "data get block 112 100 0 Items[{Slot:10b}]",
    "execute in minecraft:overworld run forceload add 128 0",
    "execute in minecraft:overworld run setblock 128 100 0 minecraft:chest",
    "item replace block 128 100 0 container.0 with minecraft:netherite_pickaxe[minecraft:damage=50]",
    "item modify block 128 100 0 container.0 sae:maintenance/add_unbreakable",
    "data get block 128 100 0 Items[{Slot:0b}]",
    "execute in minecraft:overworld run forceload add 144 0",
    "execute in minecraft:overworld run setblock 144 100 0 minecraft:chest",
    'item replace block 144 100 0 container.0 with minecraft:netherite_shovel[minecraft:enchantments={"minecraft:mending":9,"minecraft:efficiency":5}]',
    "item modify block 144 100 0 container.0 sae:maintenance/add_unbreakable",
    "item modify block 144 100 0 container.0 sae:maintenance/add_unbreakable",
    "data get block 144 100 0 Items[{Slot:0b}]",
    'execute in minecraft:overworld if data block 144 100 0 Items[{Slot:0b,components:{"minecraft:enchantments":{"minecraft:mending":1,"minecraft:efficiency":5}}}] run say Unbreakable remained level one',
    "data get storage sae:registry entries",
    "function sae:uninstall/registry_start",
    "execute in minecraft:overworld if block 80 100 0 minecraft:enchanting_table run say Workstation registry restore passed",
]

EXPECTED_MARKERS = [
    "UI title component passed",
    "UI button text passed",
    "UI tooltip visibility passed",
    "UI watch criteria passed",
    "Unbreakable remained level one",
    "Workstation registry restore passed",
]


def remove_readonly(function: object, path: str, _: object) -> None:
    Path(path).chmod(stat.S_IWRITE)
    function(path)  # type: ignore[operator]


def main() -> int:
    eula = SERVER / "eula.txt"
    if not eula.exists() or "eula=true" not in eula.read_text(encoding="utf-8"):
        print("The disposable server EULA has not been explicitly accepted.", file=sys.stderr)
        return 2

    PACKS.mkdir(parents=True, exist_ok=True)
    for name, source in (
        ("FancyUI", ROOT / "FancyUI"),
        ("SuperAwesomeEnchanting", ROOT / "SuperAwesomeEnchanting"),
    ):
        destination = PACKS / name
        if destination.exists():
            shutil.rmtree(destination, onexc=remove_readonly)
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns(".git", "third_party"))

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
    deadline = time.monotonic() + 120
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

    if not ready:
        process.kill()
        process.wait(timeout=20)
        return 1

    for command in COMMANDS:
        print(f"> {command}")
        process.stdin.write(command + "\n")
        process.stdin.flush()
        time.sleep(0.25)

    process.stdin.write("stop\n")
    process.stdin.flush()
    try:
        process.wait(timeout=60)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=20)
        captured.append("Server did not stop cleanly")

    while True:
        try:
            line = lines.get_nowait()
        except queue.Empty:
            break
        if line is not None:
            captured.append(line)
            print(line)

    datapack_errors = [
        line for line in captured
        if "Failed to load function" in line
        or "Failed to parse" in line
        or "Registry loading errors" in line
        or "Unknown function" in line
        or "Serialization errors" in line
        or "Expected literal" in line
        or "unexpected error occurred" in line.lower()
    ]
    if datapack_errors:
        print("Integration test found datapack errors:", file=sys.stderr)
        for line in datapack_errors:
            print(line, file=sys.stderr)
        return 1
    missing_markers = [marker for marker in EXPECTED_MARKERS if not any(marker in line for line in captured)]
    if missing_markers:
        print(f"Integration test missed expected results: {missing_markers}", file=sys.stderr)
        return 1
    return process.returncode or 0


if __name__ == "__main__":
    sys.exit(main())
