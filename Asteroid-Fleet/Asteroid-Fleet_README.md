# **AstroFleet: A Tactical Space Game in Python**

### **The Problem**

Classic `Battleship` is too simple. There's no movement, no special units, no real strategy beyond random guessing. I wanted to build a proper turn-based fleet commander game that runs in the terminal, inspired by the classics but with more depth.

### **The Solution**

AstroFleet. It's a tactical game built in Python where you command a fleet of ships on a grid. You have to find and destroy the enemy fleet while dealing with things like asteroids and limited visibility. It's built to be modular so anyone can add new ships, maps, and rules.

### **How to Win**

There are three ways to win a match. Keep it simple.

  * **Destroy Them:** Blow up all the other guy's ships.
  * **Hold Ground:** Control key sectors of the map for a certain number of turns.
  * **Find the Thing (Optional):** In this game mode, you have to collect special items scattered around the map.

### **The File Structure**

Here's how it's bolted together. **The code is the proof.** No magic.

```
astrofleet/
├── main.py        # Runs the game. The entry point.
├── core.py        # The main game loop and turn logic.
├── board.py       # Handles the grid, coordinates, and asteroids.
├── units/         # All the ship and damage logic lives here.
│   ├── ship.py    # The base ship class and different types (Cruiser, etc.).
│   └── damage.py  # What happens when things get hit.
├── combat.py      # How shooting works (weapons, line-of-sight).
├── tests/         # Unit tests to make sure things aren't broken.
└── config.py      # Game settings. Change board size, rules, etc. here.
```

*(I've trimmed the rest of the files for clarity. A full, working project would have more for AI, abilities, etc.)*

### **How to Run It**

```bash
# 1. Clone the repo
git clone https://github.com/yourname/astrofleet

# 2. Go into the directory
cd astrofleet

# 3. Run the game
python main.py
```

You might need `pygame` or `curses` if you want a fancier terminal UI, but it works without them.

### **How It Works: The Core Mechanics**

  * **Fog of War:** You can't see the whole board by default. You have to actually find the enemy. You can turn this off in `config.py` for a simpler game.
  * **Scouts:** These are fast, weak ships that can detect enemies in a 3-tile radius. They're your eyes and ears.
  * **The Ships:** The starting ships are listed below. They're just modules; you can build your own.

| Class       | Speed  | Armor  | Weapons       | Job               |
|-------------|--------|--------|---------------|-------------------|
| Cruiser     | Medium | Medium | Laser         | All-rounder       |
| Interceptor | High   | Low    | Pulse Cannon  | Fast attacker     |
| Destroyer   | Low    | High   | Missile, EMP  | Heavy hitter      |
| Carrier     | Low    | Medium | Drone Deploy  | Support           |
| Scout       | High   | Fragile| None / Pulse  | Recon             |

  * **Damage Effects:** Getting hit does more than just lower your HP. It can break your engines (slowing you down), knock out your weapons, or disable your shields.
  * **Hazards:** The board has asteroids on it. They block shots and damage ships that crash into them.
  * **Special Abilities:** Some ships have special moves like a short-range `Warp Jump` or a `Shield Pulse`. They have cooldowns so you can't spam them.

### **For Builders: The Nitty-Gritty**

This engine is built to be messed with.

  * **Modding:** The `modding.md` file explains how to add your own ships, factions, and abilities without breaking everything.
  * **Logging:** The game logs key events (hits, detections, etc.) to `telemetry.log`. Useful for debugging or replaying matches.
  * **AI:** There's a basic `ai_agent.py` so you can play solo or run AI vs. AI simulations to test balance. It's still pretty dumb, so this is a good place to contribute.
  * **Testing:** The `tests/` directory has unit tests. If you add something new, add a test for it.

### **The Philosophy**

**Perfect is the imaginary friend of never shipped.** This isn't a "sovereign artifact," it's a game engine. It's meant to be played, broken, and improved upon. It's modular so you can hack on it without asking for permission.

Fork it, add a ship with a ridiculous weapon, build a better AI. **Build first, ask permission never.**
