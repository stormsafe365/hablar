# Hablar — Spanish for real life 🇨🇺🇨🇴

A personal, offline-first Spanish learning app built for real conversations — especially talking with a Cuban partner's family. It focuses on the situations you actually face, not textbook drills.

**Live app:** _(enable GitHub Pages — see below — and your URL will be here)_

## What's inside

- **🗂️ Flashcards** with spaced repetition — cards you miss come back sooner and collect in a **Needs practice** folder. Star phrases into a **Saved** folder for quick access.
- **🔍 Break it down** — tap any phrase for a word-by-word breakdown, literal translation, and a "how it works" note.
- **🎬 Scenarios** — 30 interactive roleplays across three categories (Family & friends, You & him, Out & about). Pick a response, get coached.
- **👂 Listening practice** — train your ear for fast Cuban speech (normal/slow), reveal the phrase, and tap any word.
- **🎯 Quiz** — 54-question pool with hints, shuffled each round.
- **📘 Verbs & tenses** — the core verbs conjugated, plus a **Quick test** with tappable words, audio, and examples.
- **🗣️ Pronunciation** — vowels, tricky letters, and side-by-side **Cuban vs Colombian** accent comparisons.
- **📌 My phrases** — save phrases you hear; the meaning auto-translates (online), and you can tap any word for its definition and real example sentences pulled from the app.

Progress (streak, XP, saved cards, your phrases) is stored **on your device** and the app works **offline** once installed.

## Run it

Just open `index.html` in any modern browser. Everything is self-contained — React is bundled in, no build step, no server.

- `index.html` — the installable offline app (PWA)
- `sw.js`, `manifest.webmanifest`, `icon-*.png` — offline + install support
- `spanish-app.html` — the same app as a single desktop file

## Install on your phone (Android)

Open the live URL in Chrome → menu (⋮) → **Add to Home screen / Install app**. It then runs fullscreen and works offline.

## Host it free on GitHub Pages (permanent URL)

1. Push this repo to GitHub.
2. In the repo: **Settings → Pages**.
3. Under **Build and deployment**, set **Source: Deploy from a branch**, **Branch: `main` / `/ (root)`**, then **Save**.
4. After a minute your app is live at `https://<your-username>.github.io/<repo-name>/`.

Because it's always the same URL, your saved phrases and streak persist across updates.

## Tech notes

- Vanilla single-file React (UMD, bundled) — no build tooling.
- Auto-translation in **My phrases** uses the free MyMemory API when online; offline it falls back to a word-by-word gloss from the built-in dictionary.
- Text-to-speech uses the browser's built-in voices (best on Chrome/Edge).

---

Made with love for Jenna. ¡Tú puedes! 💛
