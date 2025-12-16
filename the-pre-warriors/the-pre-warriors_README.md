# Warriors: The Founding

This is a text-based, interactive fiction game that serves as an unofficial prequel to the 1979 cult classic film, *The Warriors*. It explores a simple question: how did the Warriors come to be?

## Premise

The game is set in 1978, a year before the fateful conclave in the Bronx. The streets of New York are ruled by gangs, but in Coney Island, the local set—The Destroyers—is losing its edge under weak leadership.

You play as **Cleon**, a disillusioned Destroyer who sees the rot from the inside. It's on you to break away, find a new name, recruit the soldiers who will one day become legends, and build a gang worthy of the name: **The Warriors**.

## How to Play

Simply open the `pre-warriors.html` file in any modern web browser to start the game.

## Current State

The game is in its early stages. It currently features a branching narrative where the player takes on the role of **Cleon**, the future leader of the Warriors.

The story begins with Cleon and his friend **Vermin** as disillusioned members of a rival gang, **The Destroyers**. The player makes choices that lead to them breaking away to form their own set. The narrative currently includes:

* **The inciting incident:** A botched shakedown that reveals the corruption within The Destroyers.
* **The founding moment:** Cleon decides to create a new gang, "The Warriors."
* **First recruitment:** The player can find and recruit the first new member, **Ajax**.
* **Multiple choice paths:** The game offers choices tagged with `[MUSCLE]`, `[SMARTS]`, and `[VISION]`, allowing for different approaches to situations.

The game engine is a simple script within the HTML file that reads from a `gameData` object and dynamically renders story text and choices.

## Characters

### The Warriors (Player's Crew)

* **Cleon:** The player character. Ambitious, visionary, and tired of the weakness of his current gang.
* **Vermin:** Cleon's loyal best friend and first follower.
* **Ajax:** The first potential recruit. A hot-headed brawler who brings much-needed muscle to the fledgling gang.

### Mentioned Recruits

These characters are mentioned as future recruitment possibilities:

* **Swan:** A quiet and capable future Warlord.
* **Rembrandt:** A young graffiti artist.

### Antagonists

* **Virgil:** The weak and erratic leader of **The Destroyers**.
* **Tiny:** A corrupt member of The Destroyers.

## Planned Features & Future Direction

The story is designed to be expanded upon. Several plot points are marked as `[TO BE CONTINUED...]`. The plan is to build this out into a more complete narrative experience.

* **Continue the Story:**
  * Implement the recruitment missions for **Swan** and **Rembrandt**.
  * Develop the conflict with **The Destroyers** and their leader, Virgil.
  * Show the Warriors solidifying their turf in Coney Island.

* **Introduce New Mechanics:**
  * **`RESPECT` System:** The story mentions building `RESPECT`. This could be implemented as a stat that tracks the player's standing and unlocks new choices, dialogue options, or story branches.
  * **Gang Roster:** A simple UI element to show which members you have successfully recruited.

* **Code & Engine Improvements:**
  * Separate the `gameData` object into its own JSON file for better organization and easier story editing.
  * Refactor the JavaScript to be more modular, potentially separating the game engine from the game data loader.

---
*Can you dig it?*
