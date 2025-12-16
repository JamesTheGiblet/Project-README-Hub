# Command Decision

[](https://www.google.com/search?q=./)
[](https://react.dev/)
[](https://www.google.com/search?q=./LICENSE)

I wanted to see if a personality test could be disguised as a game. This is the result: a simple, branching-narrative game where your choices reveal what kind of leader you are under pressure.

It's a single React component that runs a whole "choose your own adventure" story. You're a convoy commander, pirates are attacking, and every choice you make impacts your fleet, your crew, and your reputation.

-----

## The Problem It Solves

Standard personality tests are boring. You click bubbles, you know you're being analyzed, and it feels sterile. I wanted something more engaging.

This game wraps the assessment in a story. You're not thinking about what a "strategic" or "empathetic" leader would do, you're just trying to survive. The analysis comes at the end, based on the patterns in your decisions.

-----

## Features

  * ✅ **Branching Story:** Your choices actually matter and send you down different paths. There are over 20 different endings.
  * ✅ **Live Stat Tracking:** Everything you do affects your Fleet, Morale, Reputation, and Cargo. Let your fleet strength drop to zero, and it's game over.
  * ✅ **8-Bit Pixel Ships:** A simple visual display shows your convoy, and ships actually disappear as you take damage.
  * ✅ **Achievement System:** Unlocks based on how you play (e.g., being ruthless, saving everyone, winning against the odds).
  * ✅ **Personality Profile:** At the end, it tells you what kind of leader you were—a Guardian, a Warrior, a Tactician, etc.
  * ✅ **Save Your Game:** You can download a JSON file of your progress and come back to it later.

-----

## Project Status

**MVP / In Progress.**

This is a one-file React project that proves the concept. It's fully playable from start to finish, but it's not a massive, production-ready game. The core loop is solid, and the story branches work as intended.

-----

## Why I Built It This Way

This is just a bit of fun, not a scientifically accurate test. I was more interested in building a simple, hackable engine for interactive stories. The idea is that you could swap out the sci-fi theme for a fantasy one, or change the logic to do a more detailed analysis, without having to rebuild everything from scratch. It's a pattern that can be adapted to all sorts of things.

-----

## Getting it Running

It's a standard React app. No weird dependencies.

```bash
# Clone it
git clone https://github.com/yourusername/command-decision.git

# Go into the folder
cd command-decision

# Install the stuff
npm install

# Run it
npm start
```

-----

## Tech Stack

Kept it simple.

  * **React 18**
  * **Tailwind CSS** (for styling)
  * **Lucide React** (for the icons)
  * Just plain **JavaScript/JSX**

-----

## Contributing

This was a fun project to build. If you have ideas for new scenarios, achievements, or want to fix something, feel free to open an issue or send a PR. "PRs welcome" is the vibe here.

-----

## License

MIT. Take it, learn from it, build your own version. Whatever you want.
