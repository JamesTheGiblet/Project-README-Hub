# lightweight-env-validator

[![npm version](https://badge.fury.io/js/lightweight-env-validator.svg)](https://badge.fury.io/js/lightweight-env-validator)
[![npm downloads](https://img.shields.io/npm/dm/lightweight-env-validator.svg)](https://www.npmjs.com/package/lightweight-env-validator)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Env validation was annoying me. Built this in 2 days.

-----

## What It Is

You're probably already using `dotenv` or Node's built-in `.env` support. This is the missing piece. It's not a framework, and there's no learning curve. It's just a simple, clean validation layer that sits on top of what you already have, making sure your config is right before your app even starts.

-----

## The Problem It Solves

I was tired of writing the same boilerplate `if` statements and `parseInt` calls all over my projects. It's messy, and it's way too easy to miss something or chase down a bug that's just a typo in an `.env` file.

```js
// Instead of this scattered everywhere...
if (!process.env.API_KEY) throw new Error('API_KEY required');
const port = parseInt(process.env.PORT) || 3000;
if (isNaN(port)) throw new Error('PORT must be number');

// You just do this once:
const config = env({
  PORT: { type: 'number', default: 3000 },
  API_KEY: { type: 'string', required: true },
  NODE_ENV: { type: 'string', enum: ['development', 'production'] }
});
```

This lets you define all your env rules in one place and get on with the actual work.

-----

## Features

* ✅ **Tiny** (like, 2KB tiny). Zero dependencies because bloat is annoying.
* ✅ **Works with anything** that loads env vars (`dotenv`, Node's built-in, whatever you use).
* ✅ **Clear errors** that actually tell you what's wrong instead of just crashing.
* ✅ **Built-in TypeScript support** that just works. Your config object is fully typed without any extra setup.
* ✅ **Handles the usual stuff** out of the box: strings, numbers, booleans, arrays, and JSON.
* ✅ **Add your own validators** if you need something special.

-----

## Installation

```bash
npm install lightweight-env-validator
```

-----

## How to Use It

### The Basic Idea

Just define a schema and pass it to the `env` function. It'll read `process.env`, validate everything, and return a clean, typed config object.

```js
const { env } = require('lightweight-env-validator');

const config = env({
  // String with a list of allowed values
  NODE_ENV: {
    type: 'string',
    enum: ['development', 'production', 'test'],
    default: 'development'
  },

  // Number with some rules
  PORT: {
    type: 'number',
    default: 3000,
    min: 1000,
    max: 9999
  },

  // Something that absolutely must be there
  DATABASE_URL: {
    type: 'string',
    required: true,
    format: 'uri' // and it has to look like a URI
  },

  // A simple on/off switch
  ENABLE_LOGGING: {
    type: 'boolean',
    default: false
  }
});

console.log(config.PORT); // 3000 (as a number, not a string)
console.log(config.NODE_ENV); // 'development'
```

### Works with `dotenv` (of course)

```js
// Option 1: You load your .env file first
require('dotenv').config();
const { env } = require('lightweight-env-validator');
const config = env({ /* ... your schema ... */ });

// Option 2: Tell this tool to load it for you
const config = env({
  PORT: { type: 'number', default: 3000 }
}, {
  dotEnvPath: '.env.local' // or whatever your file is
});
```

### Using a Prefix

Got sick of typing `APP_` everywhere in my env files. This cleans it up.

```js
// Your .env file has APP_PORT, APP_HOST, etc.
const config = env({
  PORT: { type: 'number', default: 3000 },
  HOST: { type: 'string', default: 'localhost' },
}, {
  prefix: 'APP_'
});

// Now you can just use config.PORT, config.HOST
console.log(config.PORT); // reads from process.env.APP_PORT
```

### TypeScript

**✨ Automatic type inference!** No more `as const` annotations needed (requires TypeScript 5.0+).

The types are inferred automatically from your schema. No extra work needed. If a variable isn't required and has no default, TypeScript will correctly know it might be `undefined`.

```ts
import { env } from 'lightweight-env-validator';

// Types are automatically inferred from your schema!
const config = env({
  NODE_ENV: {
    type: 'string',
    enum: ['development', 'production', 'test'], // ← Becomes literal union automatically!
    default: 'development'
  },
  PORT: { type: 'number', default: 3000 },
  DATABASE_URL: { type: 'string', required: true },
  OPTIONAL_KEY: { type: 'string' } // Not required, no default
});

// TypeScript knows the exact types:
const port: number = config.PORT; // Always a number
const nodeEnv: 'development' | 'production' | 'test' = config.NODE_ENV; // Literal union!
const dbUrl: string = config.DATABASE_URL; // Never undefined (required)
const optional: string | undefined = config.OPTIONAL_KEY; // Correctly typed as possibly undefined
```

**Backward compatibility:** Old code with `as const` still works perfectly!

-----

## Project Status

**Shipped & Working.** It's stable, does what it says on the tin, and people are using it.

-----

## Why Not Just Use Zod?

Zod is a fantastic, powerful library. It's also much bigger and does a million things. I built this because I needed something that *only* did env validation and was tiny enough to not even think about.

* **Use this if:** You want a tiny, zero-dependency tool that just solves env validation.
* **Use Zod if:** You're already using it in your project for other things or need more complex, general-purpose validation.

-----

## Contributing

Got an idea or a fix? **PRs are welcome**. The goal here is to keep this thing small, focused, and free of bloat, so please keep that in mind.

-----

## License

MIT. Use it however you want.
