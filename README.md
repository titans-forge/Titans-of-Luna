# Titans of Luna

A turn-based moon colony city-builder inspired by classic city-building games. Balance power, water, oxygen, food, materials, and crew survival while the lunar environment tests every weak link.

[Play](https://titans-forge.itch.io/titans-of-luna) · [Forge collection](https://github.com/titans-forge/educational-games)

The upgraded edition is supplied under [Forge Game Hosting License 1.0](LICENSE).
See [the checkpoint](LICENSING.md) for covered material, earlier grants and the
commercial hosting threshold. This is a clean source snapshot, not a new gameplay update.

## Play

Open `index.html` in any modern browser. The game can also be launched directly from `titans-of-luna.html`.

No install. No npm. No external dependencies for core gameplay. Fully self-contained.

**Optional soundtrack**: The `audio/` folder contains two federal recordings
with their separate rights notes in `MEDIA_RIGHTS.md`. The game attempts calm
playback after the first turn, subject to browser autoplay rules. Use the music
controls to stop playback or adjust its volume.

**Save recovery note**: After reopening the game, dismiss the sponsor-selection
overlay by selecting a sponsor before pressing Load to restore an existing save.
The selected-source gameplay is unchanged; direct Load through that overlay is
a known limitation, not evidence that the stored save was lost.

Run `python3 luna_smoke.py` for the static asset and embedded-JavaScript checks.

## Concept

You are establishing the first permanent human presence on the Moon.

- Choose your sponsor faction: US/SpaceX, China, or Russia. Each has different strengths.
- Place critical infrastructure on the lunar grid: reactors for power, greenhouses for food and oxygen, habitats, ice miners, processors, etc.
- Every turn the colony consumes and produces resources.
- Random crises and issues arise (lunar night, regolith storms, radiation events, equipment failures, supply delays...).
- Manage carefully or the colony fails.

## Goals

- Grow population and keep resources stable.
- Survive as many lunar cycles as possible.
- Unlock better buildings through research and milestones.

## Key Moon-Specific Challenges

- Extended "Lunar Night" periods cripple solar power.
- Regolith dust degrades exposed solar arrays.
- Radiation events.
- Extremely expensive and infrequent resupply from Earth.
- Everything must be built to last in vacuum and extreme temperatures.

## Design Notes

- Pure vanilla HTML + Canvas + JavaScript (single file for maximum portability).
- Detailed lunar terrain with colony-building sprites and visible utility links.
- Grid-based placement with connections extending through chains of buildings.
- Building **integrity** and **regolith dust** systems (buildings lose efficiency when damaged or dirty).
- Lightweight **connection** requirement (buildings perform poorly if too far from the central hub).
- **Choice-driven crises** — many events present meaningful trade-off decisions.
- Deterministic per-turn simulation with strong lunar flavor (long nights, dust, radiation).
- Three distinct factions with different strengths.
- Designed to be understandable and modifiable.

## Current Features

- 11 buildable structures with costs and effects.
- Faction-specific bonuses for US/SpaceX, China, Russia.
- Building integrity, regolith dust, and a simple hub connection system.
- Choice-based crises with trade-offs.
- Lightweight research progression using science to unlock advanced buildings (Medical, Research Lab, Launch Pad).
- Launch Pad enables occasional supply missions.
- Turn-based simulation with lunar night cycles.
- Save/Load and New Game support.
- Canvas-based visual grid with status indicators.
- Moon-specific terrain, realistic structures, ice markers, damage/dust treatment, and night lighting.

All gameplay runs locally from the included HTML and asset files. No account, server, or network connection is required.

Enjoy building the first city on the Moon.
