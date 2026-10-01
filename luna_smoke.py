from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parent
GAME = ROOT / "titans-of-luna.html"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


html = GAME.read_text(encoding="utf-8")
index = (ROOT / "index.html").read_text(encoding="utf-8")

require('url=./titans-of-luna.html' in index, "index.html must launch the game")
require('<meta name="viewport"' in html, "game must declare a mobile viewport")
require("function resizeCanvas()" in html, "high-DPI resize function is missing")
require("backingSize / CANVAS_SIZE" in html, "canvas must scale from logical coordinates")
require("CANVAS_SIZE / rect.width" in html, "pointer mapping must use logical coordinates")
require("@media (max-width: 800px)" in html, "mobile layout is missing")
require(".crisis-overlay" in html, "crisis keyboard guard is missing")
require("https://" not in html and "http://" not in html, "runtime must not use remote assets")

for relative in (
    "assets/lunar-terrain.png",
    "assets/colony-building-atlas.png",
    "assets/colony-building-atlas-expansion.png",
    "audio/handel-water-music-sarabande.mp3",
    "audio/holst-mars.mp3",
    "LICENSE",
    "MEDIA_RIGHTS.md",
):
    require((ROOT / relative).is_file(), f"missing release file: {relative}")
    require(relative in html or relative in {"LICENSE", "MEDIA_RIGHTS.md"}, f"unused runtime asset: {relative}")

scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.DOTALL | re.IGNORECASE)
require(len(scripts) == 1, "expected one embedded game script")
result = subprocess.run(
    ["node", "--input-type=module", "-e", "import fs from 'node:fs'; new Function(fs.readFileSync(0, 'utf8'));"],
    input=scripts[0],
    text=True,
    capture_output=True,
    check=False,
)
require(result.returncode == 0, f"embedded JavaScript failed to parse: {result.stderr.strip()}")

print("Titans of Luna release smoke test passed")
