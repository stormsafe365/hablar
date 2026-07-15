# Spanish for Your Real Life — a personalized workbook

A print-ready Spanish workbook built around real life in Florida: the beach,
paddleboarding, dogs, gardening, the gym, music, cooking, coffee, work,
texting, relationships, and the **Cuban Spanish** a boyfriend actually speaks.

It matches the look and feel of the **Hablar** app (Fraunces + Inter, the
mint/cream palette) and is designed to be read on screen or printed to PDF.

## Open it

Open **`index.html`** in any browser — it links to every piece:

| File | What it is |
|------|-----------|
| `index.html` | Landing page + full table of contents |
| `book.html` | **The Book** — Parts I–VII (the teaching) |
| `practice.html` | **Practice Workbook** — exercises, write directly in it |
| `answers.html` | **Answer Book** — every answer, with the *why* |
| `flashcards.html` | **Flashcards** — every vocab word, printable |
| `cheatsheets.html` | **Cheat Sheets** — quick references |
| `tests.html` | **Progress Tests** + **Final Exam** |

### Print to PDF
Open a page → **Print → Save as PDF**. The layout is tuned for letter-size
paper with clean page breaks. Printing the Practice Workbook and writing in it
by hand is where the learning sticks.

## What's inside

- **Part I – Foundations:** how Spanish works, pronunciation, accent marks,
  rolling R's, sentence structure, thinking in Spanish, common mistakes,
  memory tricks.
- **Part II – Present Tense:** the 16 core verbs (ser, estar, ir, tener, hacer,
  ver, venir, decir, dar, poner, salir, oír, querer, poder, saber, conocer),
  each taught the same way — meaning, when it's used, memory trick, full
  conjugation, examples, and practice.
- **Part III – Real-Life Vocabulary:** 16 themed chapters (beach,
  paddleboarding, Florida/weather, tropical plants, gardening, dogs, gym,
  music, relationships, cooking, groceries, home, coffee, work, texting) with
  vocab, dialogues, stories, and exercises.
- **Part IV – Past Tense**, **Part V – Reading** (5-word stories → full page),
  **Part VI – Speaking** (question banks, role-plays, the 20-minute ladder),
  **Part VII – Cuban Spanish** (expressions, slang, pronunciation, culture).

## Regenerating / extending

Everything is generated from data, so it's easy to add or fix content and keep
all seven books in sync.

```bash
cd workbook
python3 build.py
```

- Verbs live in `content/verbs.py` (conjugations, examples, exercises).
- Vocabulary themes live in `content/vocab.py`.
- Parts I, IV–VII, cheat sheets and tests live in `content/extras.py`.
- Shared styling and layout helpers live in `content/theme.py`.

Add an entry to the relevant data list, run `build.py`, and the Book, Practice
Workbook, Answer Book, Flashcards, and Tests all update together.
