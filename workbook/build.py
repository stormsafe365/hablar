#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the Hablar personalized Spanish workbook into a set of print-ready
HTML files. Run:  python3 build.py

Outputs (next to this script):
  index.html         landing page + full table of contents
  book.html          Parts I–VII  (the teaching book)
  practice.html      the separate practice workbook (exercises)
  answers.html       the answer book (every answer worked out)
  cheatsheets.html   quick-reference sheets
  flashcards.html    printable flashcards for every vocab word
  tests.html         progress tests for every unit + final exam
"""
import os

from content.theme import (shell, box, examples, dialogue, vocab_table,
    conj_table, chips, write_lines, questions, drill, blank, esc)
from content.theme import CSS as THEME_CSS
from content.verbs import VERBS
from content.vocab import THEMES
from content import extras
from content import grammar

OUT = os.path.dirname(os.path.abspath(__file__))

def w(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name, f"({len(html)//1024} KB)")


# ══════════════════════════════════════════════════════════════════════════
# RENDERERS — TEACHING BOOK
# ══════════════════════════════════════════════════════════════════════════
def render_verb_teach(v, n):
    h = [f'<div class="page-break"></div>' if n > 1 else '']
    h.append(f'<div class="eyebrow">Present Tense · Verb {n} of {len(VERBS)}</div>')
    h.append(f'<h1>{esc(v["inf"])}</h1>')
    h.append(f'<p class="muted" style="font-size:18px">{esc(v["meaning"])}</p>')

    h.append('<h3>When it\'s used</h3>')
    h.append('<ul>' + "".join(f'<li>{u}</li>' for u in v["when"]) + '</ul>')

    h.append(box('trick', 'Memory trick', f'<p>{v["trick"]}</p>'))

    h.append('<h3>Complete conjugation (present)</h3>')
    h.append(f'<p class="small">{esc(v["pattern"])}</p>')
    h.append(conj_table("", v["conj"]))
    if n == 1:
        h.append(box('sea', 'Why only five forms?',
            '<p>For “you all,” Joshua\'s Cuban &amp; Colombian family always says '
            '<span class="es">ustedes</span>. The Spain-only '
            '<span class="es">vosotros</span> form is left out of every table on '
            'purpose — it\'s one whole column you never have to learn.</p>'))

    h.append(f'<h3>Examples ({len(v["examples"])}+)</h3>')
    h.append(examples(v["examples"]))

    # speaking / reading / writing quick blocks
    h.append('<h3>Speaking practice</h3>')
    h.append('<ol>' + "".join(f'<li>{s}</li>' for s in v["speak"]) + '</ol>')

    h.append('<h3>Reading</h3>')
    read = v["examples"][0]
    h.append(f'<p class="es">{esc(read[0])}</p><p class="en small">{esc(read[1])}</p>'
             '<p class="small">Read it aloud three times, then cover the English.</p>')

    h.append('<h3>Writing</h3>')
    h.append(box('tip', 'Escribe',
        f'<p>Write three of your own sentences using <span class="es">{esc(v["inf"].lower())}</span>. '
        'Make them true about your life.</p>' + write_lines(3)))

    # a compact preview of the drills (full versions live in practice.html)
    h.append('<h3>Quick check</h3>')
    qs = [f'{esc(s)} &nbsp; {blank()}' for s, _ in v["fill"][:4]]
    h.append(drill(f'Fill in the blank with the right form of {v["inf"].lower()}',
                   questions(qs)))
    h.append('<p class="small no-print">More fill-ins, translation, conversation '
             'and a full quiz for this verb are in the '
             '<a href="practice.html">Practice Workbook</a>. Answers in the '
             '<a href="answers.html">Answer Book</a>.</p>')
    return "".join(h)


def render_vocab_teach(t, n):
    h = ['<div class="page-break"></div>']
    h.append(f'<div class="eyebrow">Real-Life Vocabulary · Chapter {n}</div>')
    h.append(f'<h1>{esc(t["title"])}</h1>')
    h.append(f'<p class="muted">{esc(t["intro"])}</p>')

    h.append('<h3>Vocabulary</h3>')
    h.append(vocab_table(t["vocab"]))

    h.append('<h3>Dialogue</h3>')
    h.append(dialogue(t["dialogue"]))

    h.append('<h3>Story</h3>')
    st = t["story"]
    h.append(f'<h4>{esc(st["title"])}</h4>')
    h.append(f'<p class="es" style="font-size:16.5px">{esc(st["es"])}</p>')
    h.append(f'<details class="no-print"><summary class="small">English</summary>'
             f'<p class="en small">{esc(st["en"])}</p></details>')

    h.append('<h3>Speaking drills</h3>')
    h.append('<ol>'
             f'<li>Say five things you see/do related to <em>{esc(t["title"].lower())}</em> '
             'using this chapter\'s words.</li>'
             '<li>Re-read the dialogue out loud, taking both parts.</li>'
             '<li>Retell the story in your own words, in the present tense.</li>'
             '</ol>')

    h.append('<h3>Writing</h3>')
    h.append(box('tip', 'Escribe',
        f'<p>Write 3–4 sentences about <em>{esc(t["title"].lower())}</em> in your '
        'own life.</p>' + write_lines(4)))

    h.append('<h3>Exercises (preview)</h3>')
    qs = [f'{esc(s)} &nbsp; {blank(90)}' for s, _ in t["fill"][:3]]
    h.append(drill('Fill in the blank', questions(qs)))
    h.append('<p class="small no-print">Full exercises in the '
             '<a href="practice.html">Practice Workbook</a> · answers in the '
             '<a href="answers.html">Answer Book</a>.</p>')
    return "".join(h)


def build_book():
    parts = []
    # cover
    parts.append(
        '<div class="cover">'
        '<div class="eyebrow">Jenna · Boynton Beach, FL</div>'
        '<h1>Spanish for<br><em>your real life.</em></h1>'
        '<div class="sub">A personalized workbook — built around the beach, '
        'Maggie, the gym, gardening, coffee, cooking, and the Cuban &amp; '
        'Colombian Spanish Joshua and his family actually speak.</div>'
        '</div>')

    # goals
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Your Goal</h1>')
    parts.append('<p>When we\'re finished, you will be able to:</p>')
    parts.append('<ul class="goals">'
        '<li>Have a real 20–30 minute conversation in Spanish.</li>'
        '<li>Talk naturally with Joshua.</li>'
        '<li>Read simple books.</li>'
        '<li>Watch beginner Spanish YouTube.</li>'
        '<li>Think in Spanish instead of translating.</li>'
        '</ul>')
    parts.append(box('tip', 'How to use this book',
        '<ol><li>Work through the Parts in order — each builds on the last.</li>'
        '<li>After each verb or chapter, do the matching pages in the '
        '<strong>Practice Workbook</strong>.</li>'
        '<li>Check yourself in the <strong>Answer Book</strong> — read the '
        '<em>why</em>, not just the ✓.</li>'
        '<li>Review with the <strong>Flashcards</strong> daily (5 minutes).</li>'
        '<li>Take the <strong>Progress Test</strong> at the end of each unit.</li></ol>'))

    # Part I
    parts.append('<div class="page-break"></div>')
    parts.append(extras.part1_foundations())

    # Part II — verbs
    parts.append('<div class="page-break"></div>')
    parts.append('<div class="eyebrow">Part II</div>')
    parts.append('<h1>Present Tense — The 16 Core Verbs</h1>')
    parts.append('<p class="muted">These sixteen verbs do most of the heavy lifting '
        'in everyday Spanish. Each one is taught the same way, so the method becomes '
        'automatic: meaning → when → memory trick → full conjugation → many examples '
        '→ practice. Master these and you can say almost anything.</p>')
    parts.append(chips([(v["inf"], v["meaning"].split("(")[0].strip()) for v in VERBS]))
    for i, v in enumerate(VERBS, 1):
        parts.append(render_verb_teach(v, i))

    # Part III — everyday verb forms (near future, progressive, reflexive, stem-change)
    parts.append('<div class="page-break"></div>')
    parts.append(grammar.part_verb_forms())

    # Part IV — vocab
    parts.append('<div class="page-break"></div>')
    parts.append('<div class="eyebrow">Part IV</div>')
    parts.append('<h1>Real-Life Vocabulary</h1>')
    parts.append('<p class="muted">Forget “the airport” and “the museum.” '
        'We learn <em>your</em> life first — the beach, Maggie, the garden, the '
        'gym, coffee, cooking, work, and love — so every word is one you\'ll '
        'actually use this week.</p>')
    parts.append(chips([(t["title"], "") for t in THEMES]))
    for i, t in enumerate(THEMES, 1):
        parts.append(render_vocab_teach(t, i))

    # Part V — past tense
    parts.append('<div class="page-break"></div>')
    parts.append(extras.part4_past())

    # Part VI — reading
    parts.append('<div class="page-break"></div>')
    parts.append(extras.part5_reading())

    # Part VII — speaking (+ the one-word-answer fix, ladders, cards, about-you)
    parts.append('<div class="page-break"></div>')
    parts.append(extras.part6_speaking())
    parts.append(grammar.one_word_fix())
    parts.append(grammar.grow_ladders())
    parts.append(grammar.conversation_cards())
    parts.append(grammar.about_you())

    # Part VIII — Cuban & Colombian Spanish
    parts.append('<div class="page-break"></div>')
    parts.append(extras.part7_cuban())

    parts.append('<div class="page-break"></div>')
    parts.append('<h1>¡Lo lograste!</h1>')
    parts.append('<p>You reached the end of the teaching book. Now the real work — '
        'and the fun — begins: use it. Do the practice pages, drill the flashcards, '
        'and above all, <strong>speak</strong>. Every mistake is a rep. '
        '<span class="es">¡Dale, tú puedes!</span></p>')

    body = "".join(parts)
    w("book.html", shell("Hablar Workbook · The Book", body,
                         subtitle="Parts I–VIII"))
    return body


# ══════════════════════════════════════════════════════════════════════════
# RENDERERS — PRACTICE WORKBOOK
# ══════════════════════════════════════════════════════════════════════════
def render_verb_practice(v, n):
    h = ['<div class="page-break"></div>' if n > 1 else '']
    h.append(f'<div class="eyebrow">Practice · {v["inf"]}</div>')
    h.append(f'<h2>{esc(v["inf"])} — {esc(v["meaning"].split("(")[0].strip())}</h2>')

    # A. Conjugation recall
    h.append(drill('A · Write the full conjugation from memory',
        questions([f'{esc(p)} &nbsp; {blank(140)}' for p, _ in v["conj"]])))

    # B. Fill in the blanks
    h.append(drill('B · Fill in the blank with the correct present-tense form',
        questions([f'{esc(s)} &nbsp; {blank()}' for s, _ in v["fill"]])))

    # C. Translate
    h.append(drill('C · Translate into Spanish',
        questions([f'{esc(en)} &nbsp; {blank(200)}' for en, _ in v["translate"]])))

    # D. Conversation / speaking (written prep)
    h.append(drill('D · Conversation — write your own true answer',
        questions([f'{s}{write_lines(1)}' for s in v["speak"]])))

    # E. Mini quiz
    quiz = [f'Give the <strong>yo</strong> form of {v["inf"].lower()}: {blank(90)}',
            f'Give the <strong>nosotros</strong> form: {blank(90)}',
            f'Write one full sentence using {v["inf"].lower()}: {blank(230)}']
    h.append(drill('E · Quiz', questions(quiz)))
    return "".join(h)


def render_vocab_practice(t, n):
    h = ['<div class="page-break"></div>']
    h.append(f'<div class="eyebrow">Practice · {t["title"]}</div>')
    h.append(f'<h2>{esc(t["title"])}</h2>')
    h.append(drill('A · Fill in the blank',
        questions([f'{esc(s)} &nbsp; {blank()}' for s, _ in t["fill"]])))
    h.append(drill('B · Translate into Spanish',
        questions([f'{esc(en)} &nbsp; {blank(200)}' for en, _ in t["translate"]])))
    # C. match / recall vocab
    words = t["vocab"][:8]
    h.append(drill('C · Write the Spanish word',
        questions([f'{esc(en)} &nbsp; {blank(130)}' for _, en, _ in words])))
    h.append(drill('D · Free writing',
        f'<p>Write five sentences about {esc(t["title"].lower())} using this '
        'chapter\'s vocabulary.</p>' + write_lines(6)))
    return "".join(h)


def build_practice():
    parts = []
    parts.append('<div class="cover">'
        '<div class="eyebrow">Práctica</div>'
        '<h1>The Practice<br>Workbook</h1>'
        '<div class="sub">Thousands of questions. Nearly every page is exercises. '
        'Write directly in it — that\'s the point.</div>'
        '<div class="who">Companion to the Book · check yourself in the Answer Book</div>'
        '</div>')

    parts.append('<div class="page-break"></div>')
    parts.append('<div class="eyebrow">Unit 2</div>')
    parts.append('<h1>Present-Tense Verb Drills</h1>')
    parts.append('<p class="muted">One drill set per verb: recall the conjugation, '
        'fill in the blanks, translate, converse, and quiz. Do a verb a day.</p>')
    for i, v in enumerate(VERBS, 1):
        parts.append(render_verb_practice(v, i))

    parts.append('<div class="page-break"></div>')
    parts.append('<div class="eyebrow">Unit 3</div>')
    parts.append('<h1>Vocabulary Drills</h1>')
    for i, t in enumerate(THEMES, 1):
        parts.append(render_vocab_practice(t, i))

    # past-tense practice
    # everyday verb forms drills
    parts.append('<div class="page-break"></div>')
    parts.append('<div class="eyebrow">Unit 4</div>')
    parts.append('<h1>Everyday Verb-Form Drills</h1>')
    parts.append(drill('A · Near future — rewrite with "voy a / vamos a…"',
        questions([f'{esc(s)} &nbsp; {blank(180)}' for s in [
            "(beach, this weekend) → I'm going to…",
            "(paddleboard with Joshua) → …",
            "(water the plants tomorrow) → …",
            "(gym after work) → …",
            "(cook something Cuban) → …"]])))
    parts.append(drill('B · Progressive — "estoy ___-ando/-iendo" (right now)',
        questions([f'{esc(en)} &nbsp; {blank(190)}' for en in [
            "I'm learning Spanish.", "I'm cooking.", "Maggie is sleeping.",
            "We're walking on the beach.", "I'm trying it. (lo…)"]])))
    parts.append(drill('C · Reflexives — your daily routine',
        questions([f'{esc(s)} &nbsp; {blank()}' for s in [
            "Yo (levantarse) ___ a las seis.",
            "Yo (ducharse) ___ por la mañana.",
            "Mi novio (llamarse) ___ Joshua.",
            "Los domingos yo (quedarse) ___ en casa.",
            "Yo (acostarse) ___ temprano."]])))
    parts.append(drill('D · Stem-changers (the boot)',
        questions([f'{esc(s)} &nbsp; {blank()}' for s in [
            "Yo (querer) ___ aprender comida cubana.",
            "Yo no (poder) ___ dormir con calor.",
            "Yo (regar) ___ las plantas.",
            "Yo (empezar) ___ a trabajar a las nueve.",
            "Yo (preferir) ___ la playa por la mañana."]])))

    parts.append('<div class="page-break"></div>')
    parts.append('<div class="eyebrow">Unit 5</div>')
    parts.append('<h1>Past-Tense Drills</h1>')
    past_fill = [
        ("Ayer (yo, ir) ___ a la playa.", "fui"),
        ("Anoche (nosotros, comer) ___ arroz con pollo.", "comimos"),
        ("(yo, hacer) ___ paddleboard el sábado.", "Hice"),
        ("Mi novio (cocinar) ___ la cena.", "cocinó"),
        ("(tú, trabajar) ¿___ ayer?", "Trabajaste"),
        ("(nosotros, ver) ___ un delfín.", "vimos"),
        ("(yo, tener) ___ un día muy bueno.", "Tuve"),
        ("Ellos (bailar) ___ salsa toda la noche.", "bailaron"),
    ]
    parts.append(drill('A · Put the verb into the preterite (past)',
        questions([f'{esc(s)} &nbsp; {blank()}' for s, _ in past_fill])))
    parts.append(drill('B · Translate into the past',
        questions([f'{esc(en)} &nbsp; {blank(210)}' for en in [
            "Yesterday I went to the beach.",
            "We ate at a Cuban restaurant.",
            "I paddleboarded in the morning.",
            "My boyfriend made coffee.",
            "Did you work yesterday?",
            "We saw a dolphin.",
        ]])))
    parts.append(drill('C · Write it',
        '<p>Describe your last weekend in 5–6 sentences, in the past tense.</p>'
        + write_lines(7)))

    body = "".join(parts)
    w("practice.html", shell("Hablar Workbook · Practice", body,
                             subtitle="Practice Workbook"))
    return body


# ══════════════════════════════════════════════════════════════════════════
# ANSWER BOOK
# ══════════════════════════════════════════════════════════════════════════
def _ans_row(prompt, answer, why=""):
    why_h = f'<div class="small" style="color:var(--soft)">{why}</div>' if why else ''
    return (f'<div class="q"><span class="num">›</span>'
            f'<span>{prompt} &nbsp;→&nbsp; <span class="es">{esc(answer)}</span></span>'
            f'{why_h}</div>')


def build_answers():
    parts = []
    parts.append('<div class="cover"><div class="eyebrow">Respuestas</div>'
        '<h1>The Answer<br>Book</h1>'
        '<div class="sub">Every answer — and the <em>why</em> behind it, not just '
        'right or wrong.</div>'
        '<div class="who">For the Practice Workbook</div></div>')

    # verb answers
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Present-Tense Verb Answers</h1>')
    for v in VERBS:
        parts.append(f'<h2>{esc(v["inf"])}</h2>')
        # conjugation
        conj = " · ".join(f'{p.split("/")[0].strip()}: <span class="es">{f}</span>'
                          for p, f in v["conj"])
        parts.append(f'<p class="small"><strong>A · Conjugation.</strong> {conj}</p>')
        # fill
        parts.append('<p class="small"><strong>B · Fill in the blank.</strong></p>')
        for s, a in v["fill"]:
            parts.append(_ans_row(esc(s.replace("___", "____")), a))
        # translate
        parts.append('<p class="small"><strong>C · Translation.</strong></p>')
        for en, es in v["translate"]:
            parts.append(_ans_row(esc(en), es))
        parts.append('<hr>')

    # vocab answers
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Vocabulary Answers</h1>')
    for t in THEMES:
        parts.append(f'<h2>{esc(t["title"])}</h2>')
        parts.append('<p class="small"><strong>A · Fill in the blank.</strong></p>')
        for s, a in t["fill"]:
            parts.append(_ans_row(esc(s.replace("___", "____")), a))
        parts.append('<p class="small"><strong>B · Translation.</strong></p>')
        for en, es in t["translate"]:
            parts.append(_ans_row(esc(en), es))
        parts.append('<hr>')

    # everyday verb-form answers
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Everyday Verb-Form Answers</h1>')
    parts.append('<p class="small"><strong>A · Near future (voy a + verb).</strong></p>')
    for en, es in [
        ("beach this weekend", "Voy a la playa este fin de semana."),
        ("paddleboard with Joshua", "Voy a hacer paddleboard con Joshua."),
        ("water the plants tomorrow", "Mañana voy a regar las plantas."),
        ("gym after work", "Voy al gimnasio después del trabajo."),
        ("cook something Cuban", "Voy a cocinar algo cubano."),
    ]:
        parts.append(_ans_row(esc(en), es))
    parts.append('<p class="small"><strong>B · Progressive (estar + -ando/-iendo).</strong></p>')
    for en, es in [
        ("I'm learning Spanish.", "Estoy aprendiendo español."),
        ("I'm cooking.", "Estoy cocinando."),
        ("Maggie is sleeping.", "Maggie está durmiendo."),
        ("We're walking on the beach.", "Estamos caminando por la playa."),
        ("I'm trying it.", "Lo estoy intentando."),
    ]:
        parts.append(_ans_row(esc(en), es))
    parts.append('<p class="small"><strong>C · Reflexives.</strong></p>')
    for s, a, why in [
        ("Yo (levantarse) ____ a las seis.", "me levanto", "yo → me + levanto."),
        ("Yo (ducharse) ____ por la mañana.", "me ducho", "yo → me + ducho."),
        ("Mi novio (llamarse) ____ Joshua.", "se llama", "él → se + llama."),
        ("Los domingos yo (quedarse) ____ en casa.", "me quedo", "yo → me + quedo."),
        ("Yo (acostarse) ____ temprano.", "me acuesto", "reflexive + o→ue stem change."),
    ]:
        parts.append(_ans_row(esc(s), a, why))
    parts.append('<p class="small"><strong>D · Stem-changers (the boot).</strong></p>')
    for s, a, why in [
        ("Yo (querer) ____ aprender…", "quiero", "e→ie."),
        ("Yo no (poder) ____ dormir…", "puedo", "o→ue."),
        ("Yo (regar) ____ las plantas.", "riego", "e→ie — the sneaky one."),
        ("Yo (empezar) ____ a trabajar…", "empiezo", "e→ie."),
        ("Yo (preferir) ____ la playa…", "prefiero", "e→ie."),
    ]:
        parts.append(_ans_row(esc(s), a, why))

    # past-tense answers with explanations
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Past-Tense Answers</h1>')
    explained = [
        ("Ayer (ir) ___ a la playa.", "fui", "ir and ser share the past — fui = I went."),
        ("Anoche (comer) ___ arroz con pollo.", "comimos", "-er nosotros preterite = -imos."),
        ("(hacer) ___ paddleboard el sábado.", "Hice", "hacer is irregular: hice, hiciste, hizo."),
        ("Mi novio (cocinar) ___ la cena.", "cocinó", "regular -ar él form: stress the final ó."),
        ("(trabajar) ¿___ ayer?", "Trabajaste", "regular -ar tú form: -aste."),
        ("(ver) ___ un delfín.", "vimos", "ver nosotros: vimos (no accent needed)."),
        ("(tener) ___ un día muy bueno.", "Tuve", "tener is irregular: tuve, tuviste, tuvo."),
        ("(bailar) Ellos ___ salsa.", "bailaron", "regular -ar ellos form: -aron."),
    ]
    for s, a, why in explained:
        parts.append(_ans_row(esc(s.replace("___", "____")), a, why))
    parts.append('<p class="small"><strong>Translations (past):</strong></p>')
    for en, es in [
        ("Yesterday I went to the beach.", "Ayer fui a la playa."),
        ("We ate at a Cuban restaurant.", "Comimos en un restaurante cubano."),
        ("I paddleboarded in the morning.", "Hice paddleboard por la mañana."),
        ("My boyfriend made coffee.", "Mi novio hizo café."),
        ("Did you work yesterday?", "¿Trabajaste ayer?"),
        ("We saw a dolphin.", "Vimos un delfín."),
    ]:
        parts.append(_ans_row(esc(en), es))

    body = "".join(parts)
    w("answers.html", shell("Hablar Workbook · Answers", body,
                            subtitle="Answer Book"))
    return body


# ══════════════════════════════════════════════════════════════════════════
# FLASHCARD DETAIL SHEETS (tap a card → full breakdown)
# ══════════════════════════════════════════════════════════════════════════
import re as _re

# Hand-written preterite + gerund for the 16 core verbs (yo, tú, él, nos, ellos)
PRETERITE = {
    "Ser":    ["fui", "fuiste", "fue", "fuimos", "fueron"],
    "Estar":  ["estuve", "estuviste", "estuvo", "estuvimos", "estuvieron"],
    "Ir":     ["fui", "fuiste", "fue", "fuimos", "fueron"],
    "Tener":  ["tuve", "tuviste", "tuvo", "tuvimos", "tuvieron"],
    "Hacer":  ["hice", "hiciste", "hizo", "hicimos", "hicieron"],
    "Ver":    ["vi", "viste", "vio", "vimos", "vieron"],
    "Venir":  ["vine", "viniste", "vino", "vinimos", "vinieron"],
    "Decir":  ["dije", "dijiste", "dijo", "dijimos", "dijeron"],
    "Dar":    ["di", "diste", "dio", "dimos", "dieron"],
    "Poner":  ["puse", "pusiste", "puso", "pusimos", "pusieron"],
    "Salir":  ["salí", "saliste", "salió", "salimos", "salieron"],
    "Oír":    ["oí", "oíste", "oyó", "oímos", "oyeron"],
    "Querer": ["quise", "quisiste", "quiso", "quisimos", "quisieron"],
    "Poder":  ["pude", "pudiste", "pudo", "pudimos", "pudieron"],
    "Saber":  ["supe", "supiste", "supo", "supimos", "supieron"],
    "Conocer":["conocí", "conociste", "conoció", "conocimos", "conocieron"],
}
GERUNDS = {
    "Ser": "siendo", "Estar": "estando", "Ir": "yendo", "Tener": "teniendo",
    "Hacer": "haciendo", "Ver": "viendo", "Venir": "viniendo",
    "Decir": "diciendo", "Dar": "dando", "Poner": "poniendo",
    "Salir": "saliendo", "Oír": "oyendo", "Querer": "queriendo",
    "Poder": "pudiendo", "Saber": "sabiendo", "Conocer": "conociendo",
}

DETAIL = {}   # key -> detail sheet HTML, embedded in the app

def _sheet_head(kicker, word, en, note=""):
    n = f'<div class="small muted">{esc(note)}</div>' if note else ''
    return (f'<div class="sh-k">{esc(kicker)}</div>'
            f'<h3 class="sh-w es" data-sheetword="{esc(word)}">{esc(word)}</h3>'
            f'<div class="sh-en">{esc(en)}</div>{n}'
            '<div class="sh-stress"></div>')

def _rev(q, a):
    return (f'<div class="rev"><span class="rev-q">{esc(q)}</span>'
            f'<button class="rev-btn" data-es="{esc(a)}">Show</button>'
            f'<span class="rev-ans">{esc(a)}</span></div>')

def verb_detail_html(v):
    inf = v["inf"]; low = inf.lower()
    pret = PRETERITE[inf]; ger = GERUNDS[inf]
    h = [_sheet_head("Verb · full breakdown", low, v["meaning"])]
    h.append('<h4>One verb, four jobs</h4>')
    h.append(vocab_table([
        (f"yo {v['conj'][0][1]}", "present — today / usually", "hoy"),
        (f"yo {pret[0]}", "past — done and finished", "ayer"),
        (f"voy a {low}", "going to — the easy future", "mañana"),
        (f"estoy {ger}", "-ing — right this second", "ahora mismo"),
    ]))
    h.append('<h4>Present</h4>')
    h.append(conj_table("", v["conj"]))
    h.append('<h4>Past (preterite)</h4>')
    h.append(conj_table("", list(zip([p for p, _ in v["conj"]], pret))))
    h.append('<h4>When you use it</h4>')
    h.append('<ul>' + "".join(f'<li>{u}</li>' for u in v["when"]) + '</ul>')
    h.append(box('trick', 'Memory trick', f'<p>{v["trick"]}</p>'))
    h.append('<h4>In real sentences</h4>')
    h.append(examples(v["examples"][:6]))
    h.append('<h4>Try it — tap to check</h4>')
    for s, a in v["fill"][:4]:
        h.append(_rev(s, a))
    for en_, es_ in v["translate"][:2]:
        h.append(_rev(en_, es_))
    return "".join(h)

_ARTICLES = {"el", "la", "los", "las", "un", "una", "unos", "unas", "de", "para"}

def _core_token(es):
    words = _re.sub(r"[¡!¿?.,…()/]", " ", es.lower()).split()
    for w in words:
        if w not in _ARTICLES and len(w) > 2:
            return w
    return words[0] if words else es.lower()

def vocab_detail_html(t, es, en, note):
    tok = _core_token(es)
    h = [_sheet_head(t["title"], es, en, note)]
    found, seen = [], set()
    for _, ses, sen in t["dialogue"]:
        if tok in ses.lower() and ses not in seen:
            found.append((ses, sen)); seen.add(ses)
    for een, ees in t["translate"]:
        if tok in ees.lower() and ees not in seen:
            found.append((ees, een)); seen.add(ees)
    if found:
        h.append('<h4>In real sentences</h4>')
        h.append(examples(found[:3]))
    prac = [(s, a) for s, a in t["fill"] if tok in s.lower() or tok == a.lower()]
    if prac:
        h.append('<h4>Try it — tap to check</h4>')
        for s, a in prac[:2]:
            h.append(_rev(s, a))
    h.append(box('tip', 'Make it yours',
        f'<p>Say one true sentence about your life using '
        f'<span class="es">{esc(es)}</span> — out loud, right now. '
        'Add a <em>porque</em> if you can.</p>'))
    return "".join(h)


# ══════════════════════════════════════════════════════════════════════════
# FLASHCARDS
# ══════════════════════════════════════════════════════════════════════════
def build_flashcards():
    parts = []
    parts.append('<div class="cover"><div class="eyebrow">Tarjetas</div>'
        '<h1>Flashcards</h1>'
        '<div class="sub">Every word in the workbook. <strong>Tap any card for '
        'the full breakdown</strong> — tenses, real sentences, and quick practice. '
        '(On paper: print and cut along the dashed lines.)</div>'
        '<div class="who">Spanish → English</div></div>')

    # verbs deck
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Deck 1 · The 16 Verbs</h1>')
    verb_cards = []
    for i, v in enumerate(VERBS):
        yo = v["conj"][0][1]
        key = f"v{i}"
        DETAIL[key] = verb_detail_html(v)
        verb_cards.append((v["inf"].lower(), v["meaning"].split("(")[0].strip(),
                           f'yo → {yo}', key))
    parts.append(_cards(verb_cards))

    # vocab decks by theme
    for ti, t in enumerate(THEMES):
        parts.append('<div class="page-break"></div>')
        parts.append(f'<h1>{esc(t["title"])}</h1>')
        cards = []
        for wi, (es, en, note) in enumerate(t["vocab"]):
            key = f"t{ti}_{wi}"
            DETAIL[key] = vocab_detail_html(t, es, en, note)
            cards.append((es, en, note, key))
        parts.append(_cards(cards))

    body = "".join(parts)
    w("flashcards.html", shell("Hablar Workbook · Flashcards", body,
                               subtitle="Flashcards"))
    return body


def _cards(items):
    """items: (front, back, tag) or (front, back, tag, detail_key)."""
    out = ['<div class="cards">']
    for it in items:
        front, back, tag = it[0], it[1], it[2]
        key = it[3] if len(it) > 3 else None
        tag_h = f'<div class="tag">{esc(tag)}</div>' if tag else ''
        key_h = f' data-key="{esc(key)}"' if key else ''
        out.append(f'<div class="card"{key_h}><div class="front">{esc(front)}</div>'
                   f'<div class="back">{esc(back)}</div>{tag_h}</div>')
    out.append('</div>')
    return "".join(out)


# ══════════════════════════════════════════════════════════════════════════
# TESTS
# ══════════════════════════════════════════════════════════════════════════
def build_tests():
    parts = []
    parts.append('<div class="cover"><div class="eyebrow">Exámenes</div>'
        '<h1>Progress Tests<br>& Final Exam</h1>'
        '<div class="sub">One test per unit, then a final exam that combines '
        'everything. No peeking — answers are in the Answer Book section below.</div>'
        '<div class="who">Track your progress</div></div>')

    # Unit 1 — foundations
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Test · Unit 1 — Foundations</h1>')
    parts.append(drill('Pronunciation & basics', questions([
        'How do you pronounce the letter <span class="es">j</span>? ' + blank(160),
        'Which "to be" verb is for feelings and location? ' + blank(120),
        'Add the accent if needed: <span class="es">cafe</span> ' + blank(90),
        'Make it negative: <span class="es">Quiero café.</span> ' + blank(150),
        'Masculine or feminine? <span class="es">___ playa</span> (el/la) ' + blank(70),
        'What\'s wrong with <span class="es">Soy 30</span>? ' + blank(200),
    ])))

    # Unit 2 — present tense verbs
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Test · Unit 2 — Present Tense</h1>')
    v2 = [
        ("Yo (ser) ___ de Florida.", "soy"),
        ("Mi novio (estar) ___ cansado.", "está"),
        ("Nosotros (ir) ___ a la playa.", "vamos"),
        ("Yo (tener) ___ dos perros.", "tengo"),
        ("Hoy (hacer) ___ calor.", "hace"),
        ("Yo (poner) ___ música.", "pongo"),
        ("¿Tú (querer) ___ un café?", "quieres"),
        ("Yo no (poder) ___ dormir.", "puedo"),
        ("Yo (saber) ___ nadar.", "sé"),
        ("Yo (conocer) ___ a tu familia.", "conozco"),
    ]
    parts.append(drill('Conjugate in the present',
        questions([f'{esc(s)} &nbsp; {blank()}' for s, _ in v2])))
    parts.append(drill('Translate', questions([f'{esc(e)} &nbsp; {blank(200)}' for e in [
        "I have to work today.", "We're going to the beach.",
        "I want a Cuban coffee.", "Do you know how to dance salsa?"]])))

    # Unit 3 — vocab
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Test · Unit 3 — Real-Life Vocabulary</h1>')
    parts.append(drill('Write the Spanish', questions([f'{esc(e)} &nbsp; {blank(150)}' for e in [
        "the beach", "the paddleboard", "the sunscreen", "the dog (leash)",
        "the coffee", "the garden", "to cook", "the weights", "the sunset",
        "the storm"]])))
    parts.append(drill('Fill in', questions([f'{esc(s)} &nbsp; {blank()}' for s in [
        "Voy a la ___ los sábados.", "Mi perro es muy ___ (affectionate).",
        "El café cubano es fuerte y ___.", "En verano hace mucho ___ en Florida."]])))

    # Unit 4 — past tense
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Test · Unit 4 — Past Tense</h1>')
    parts.append(drill('Preterite', questions([f'{esc(s)} &nbsp; {blank()}' for s in [
        "Ayer yo (ir) ___ a la playa.", "Nosotros (comer) ___ arroz con pollo.",
        "Yo (hacer) ___ paddleboard.", "Mi novio (cocinar) ___ la cena.",
        "¿Tú (trabajar) ___ ayer?", "Yo (tener) ___ un buen día."]])))

    # Final exam
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Final Exam</h1>')
    parts.append('<p class="muted">Everything combined. Take your time. Aim for '
        '80%+ before you call it — then celebrate with a cafecito.</p>')
    parts.append('<h3>Section A · Verbs (present)</h3>')
    parts.append(drill('Conjugate', questions([f'{esc(s)} &nbsp; {blank()}' for s in [
        "Yo (estar) ___ en la playa.", "Nosotros (tener) ___ una casa.",
        "Yo (hacer) ___ ejercicio.", "Mi novio (querer) ___ cocinar.",
        "Yo (salir) ___ de casa a las ocho.", "Yo (dar) ___ de comer al perro."]])))
    parts.append('<h3>Section B · Past</h3>')
    parts.append(drill('Preterite', questions([f'{esc(s)} &nbsp; {blank()}' for s in [
        "El sábado yo (ir) ___ a la playa.", "Nosotros (ver) ___ un delfín.",
        "Yo (comer) ___ en un restaurante cubano."]])))
    parts.append('<h3>Section C · Vocabulary</h3>')
    parts.append(drill('Translate', questions([f'{esc(e)} &nbsp; {blank(150)}' for e in [
        "the sunset", "to water the plants", "the weekend", "tasty (food)"]])))
    parts.append('<h3>Section D · Cuban Spanish</h3>')
    parts.append(drill('What do these mean?', questions([f'<span class="es">{esc(s)}</span> &nbsp; {blank(160)}' for s in [
        "¡Dale!", "¿Qué bolá?", "asere", "¡Qué rico!"]])))
    parts.append('<h3>Section E · Write</h3>')
    parts.append(drill('Free response',
        '<p>Write 8–10 sentences about a perfect day in your life — present and '
        'past tense, real vocabulary. This is your 20-minute conversation on '
        'paper.</p>' + write_lines(10)))

    # answer key for tests
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Test Answer Key</h1>')
    parts.append('<h3>Unit 2</h3>')
    parts.append('<p class="small">' + " · ".join(f'{esc(s.split("(")[0])}<b class="es"> {a}</b>' for s, a in v2) + '</p>')
    parts.append('<h3>Unit 4 / Final past</h3>')
    parts.append('<p class="small es">fui · comimos · hice · cocinó · trabajaste · tuve · vimos</p>')
    parts.append('<h3>Cuban Spanish</h3>')
    parts.append('<p class="small">¡Dale! = okay/go for it · ¿Qué bolá? = what\'s up '
        '· asere = buddy · ¡Qué rico! = how delicious/nice</p>')

    body = "".join(parts)
    w("tests.html", shell("Hablar Workbook · Tests", body,
                          subtitle="Progress Tests & Final Exam"))
    return body


# ══════════════════════════════════════════════════════════════════════════
# CHEAT SHEETS + INDEX
# ══════════════════════════════════════════════════════════════════════════
def build_cheats():
    body = extras.cheat_sheets()
    w("cheatsheets.html", shell("Hablar Workbook · Cheat Sheets",
        body, subtitle="Cheat Sheets"))
    return body


def build_index():
    tiles = [
        ("book.html", "📘", "The Book", "Parts I–VIII: foundations, the 16 core "
         "verbs, everyday verb forms, real-life vocabulary, past tense, reading, "
         "speaking & Cuban & Colombian Spanish."),
        ("practice.html", "✍️", "Practice Workbook", "Thousands of exercises — "
         "fill-ins, translation, conversation, and quizzes for every verb and theme."),
        ("answers.html", "🔑", "Answer Book", "Every answer worked out, with the "
         "reasoning — not just right or wrong."),
        ("flashcards.html", "🃏", "Flashcards", "Every vocabulary word, printable "
         "and ready to cut."),
        ("cheatsheets.html", "📎", "Cheat Sheets", "Survival phrases, verb tables, "
         "numbers, time, and question words at a glance."),
        ("tests.html", "📝", "Tests & Final Exam", "A progress test for every unit, "
         "plus a combined final exam."),
    ]
    body = []
    body.append('<div class="cover" style="min-height:auto;padding-bottom:8px">'
        '<div class="eyebrow">Jenna · Boynton Beach, FL</div>'
        '<h1 style="font-size:clamp(30px,8vw,46px)">Spanish for '
        '<em>your real life.</em></h1>'
        '<div class="sub">Your personalized workbook — the beach, Maggie, coffee, '
        'cooking, the gym, gardening, and the Cuban &amp; Colombian Spanish Joshua '
        'and his family actually speak.</div></div>')

    body.append('<a class="go-card" href="book.html">'
        '<div><div class="gc-k">Sigue aprendiendo · keep going</div>'
        '<div class="gc-t">The Book — start where you left off</div></div>'
        '<span class="gc-a">→</span></a>')

    body.append('<h2>What\'s inside</h2>')
    body.append('<div class="grid">')
    for i, (href, ic, tt, dd) in enumerate(tiles, 1):
        body.append(f'<a class="tile" href="{href}">'
                    f'<div class="tn">{i:02d}</div>'
                    f'<div class="tt">{esc(tt)}</div><div class="dd">{esc(dd)}</div></a>')
    body.append('</div>')

    # full table of contents
    body.append('<h2>Full Table of Contents</h2>')
    def toc(title, desc):
        return (f'<li><span class="t">{esc(title)}</span>'
                f'<span class="d">{esc(desc)}</span></li>')
    body.append('<h3>The Book</h3><ul class="toc">')
    body.append(toc("Part I · Foundations", "How Spanish works, pronunciation, "
        "accents, rolling R's, sentence structure, thinking in Spanish, mistakes, "
        "memory tricks"))
    body.append(toc("Part II · Present Tense", "16 core verbs, each taught the same "
        "way: " + ", ".join(v["inf"] for v in VERBS)))
    body.append(toc("Part III · Everyday Verb Forms", "Near future (voy a…), the "
        "true future (hablaré), the two-verb rule, present progressive (-ing), "
        "reflexive verbs, and stem-changing verbs (the boot)"))
    body.append(toc("Part IV · Real-Life Vocabulary",
        ", ".join(t["title"] for t in THEMES)))
    body.append(toc("Part V · Past Tense", "Regular & irregular preterite, yesterday, "
        "trips, stories, exercises"))
    body.append(toc("Part VI · Reading", "From 5-word stories up to a full page — "
        "vocab, grammar, questions, writing prompts"))
    body.append(toc("Part VII · Speaking", "The one-word-answer fix + porque, "
        "grow-an-answer ladders, your 30 conversation cards, your about-you script, "
        "and role-plays"))
    body.append(toc("Part VIII · Cuban & Colombian Spanish", "Expressions, slang, "
        "pronunciation, and culture — what Joshua and his family actually say"))
    body.append('</ul>')
    body.append('<h3>Companion Books</h3><ul class="toc">')
    body.append(toc("Practice Workbook", "Verb drills, vocabulary drills, past-tense drills"))
    body.append(toc("Answer Book", "Full worked answers with explanations"))
    body.append(toc("Flashcards", "Verb deck + 16 themed vocabulary decks"))
    body.append(toc("Cheat Sheets", "Survival phrases, verb table, numbers, time, questions"))
    body.append(toc("Progress Tests & Final Exam", "One test per unit + a combined final"))
    body.append('</ul>')

    body.append(box('tip', 'Printing to PDF',
        '<p>Open any page and use your browser\'s <strong>Print → Save as PDF</strong>. '
        'The layout is built for letter-size paper with clean page breaks. Print the '
        'Practice Workbook and write in it by hand — that\'s where the learning '
        'sticks.</p>'))

    body.append('<p class="small muted" style="margin-top:26px">Built with the Hablar '
        'method · personalized for your life in Florida · '
        '<span class="es">¡Dale, tú puedes!</span></p>')

    html_body = "".join(body)
    w("index.html", shell("Hablar · Personalized Spanish Workbook", html_body,
                          subtitle="Contents", show_nav=True))
    return html_body


# ══════════════════════════════════════════════════════════════════════════
# COMBINED SINGLE-PAGE ARTIFACT  (self-contained, tabbed, light + dark)
# ══════════════════════════════════════════════════════════════════════════
ARTIFACT_EXTRA_CSS = r"""
/* true neutral charcoal (no brown) — salmon primary + mint secondary */
:root{
  --bg:#1a1c1e; --paper:#242729; --sand:#1a1c1e; --sand2:#2d3134;
  --ink:#eef1f1; --soft:#a8b0b3; --faint:#747c81; --line:#34393d;
  --accent:#ff8f7d; --accent2:#f97a66; --accent-soft:#362827;
  --cuba:#ff8f7d; --cuba-soft:#362827; --sea:#5fd6a5; --sea-soft:#1c322a;
  --sun:#d8b36a; --sun-soft:#322c1d; --coral:#ff8f7d; --coral-soft:#362827;
}
@media (prefers-color-scheme: light){:root:not([data-theme]){
  --bg:#f3f4f5; --paper:#ffffff; --sand:#f3f4f5; --sand2:#e9ebec;
  --ink:#22262a; --soft:#5f676d; --faint:#8f979c; --line:#e2e5e6;
  --accent:#e8604a; --accent2:#d44e39; --accent-soft:#fdeae6;
  --cuba:#e8604a; --cuba-soft:#fdeae6; --sea:#1fa97e; --sea-soft:#dff4ec;
  --sun:#b8933a; --sun-soft:#f6eecf; --coral:#e8604a; --coral-soft:#fdeae6;
}}
:root[data-theme="light"]{
  --bg:#f3f4f5; --paper:#ffffff; --sand:#f3f4f5; --sand2:#e9ebec;
  --ink:#22262a; --soft:#5f676d; --faint:#8f979c; --line:#e2e5e6;
  --accent:#e8604a; --accent2:#d44e39; --accent-soft:#fdeae6;
  --cuba:#e8604a; --cuba-soft:#fdeae6; --sea:#1fa97e; --sea-soft:#dff4ec;
  --sun:#b8933a; --sun-soft:#f6eecf; --coral:#e8604a; --coral-soft:#fdeae6;
}
:root[data-theme="dark"]{
  --bg:#1a1c1e; --paper:#242729; --sand:#1a1c1e; --sand2:#2d3134;
  --ink:#eef1f1; --soft:#a8b0b3; --faint:#747c81; --line:#34393d;
  --accent:#ff8f7d; --accent2:#f97a66; --accent-soft:#362827;
  --cuba:#ff8f7d; --cuba-soft:#362827; --sea:#5fd6a5; --sea-soft:#1c322a;
  --sun:#d8b36a; --sun-soft:#322c1d; --coral:#ff8f7d; --coral-soft:#362827;
}
/* in dark mode the hardcoded pale borders should track the line token */
@media (prefers-color-scheme: dark){
  .tip,.trick,.warn,.cuba,.sea{border-color:var(--line)}
  .card{border-color:var(--faint)}
}
:root[data-theme="dark"] .tip,:root[data-theme="dark"] .trick,
:root[data-theme="dark"] .warn,:root[data-theme="dark"] .cuba,
:root[data-theme="dark"] .sea{border-color:var(--line)}

/* sticky header + tabs — translucent, melts into the gradient */
.wb-header{position:sticky;top:0;z-index:50;
  background:color-mix(in srgb,var(--bg) 55%,transparent);
  -webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px)}
.wb-bar{max-width:1000px;margin:0 auto;display:flex;align-items:center;gap:10px;
  padding:12px 20px 10px}
.wb-brand{font-family:var(--serif);font-weight:700;font-size:17px;white-space:nowrap;color:var(--ink)}
.wb-brand .dot{color:var(--accent)}
.wb-tabs{display:flex;gap:4px;overflow-x:auto;margin-left:auto;scrollbar-width:none;min-width:0}
.wb-tabs::-webkit-scrollbar{display:none}
.wb-tab{font-family:var(--round);font-weight:800;font-size:12.5px;letter-spacing:.01em;
  padding:8px 13px;border-radius:999px;color:var(--soft);white-space:nowrap;
  border:1px solid transparent;background:none;cursor:pointer;transition:.12s}
.wb-tab:hover{color:var(--ink);background:var(--sand2)}
.wb-tab.on{background:var(--accent-soft);color:var(--accent);border-color:var(--line)}
.wb-tab:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.tab{display:none}
.tab.on{display:block;animation:fade .18s ease}
@keyframes fade{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.tab.on{animation:none}}
html,body{overflow-x:hidden;max-width:100%}
.page{margin-top:20px;margin-bottom:40px;max-width:min(820px,100%)}
h1,h2,h3{overflow-wrap:break-word}
.cover h1{text-wrap:balance}
details summary{cursor:pointer}

/* header slow-speed toggle — quiet ghost control until active */
.slow-btn{font-family:var(--round);font-weight:700;font-size:12.5px;padding:7px 10px;
  border-radius:999px;border:1px solid transparent;background:none;
  color:var(--faint);cursor:pointer;white-space:nowrap;flex:0 0 auto}
.slow-btn:hover{color:var(--soft)}
.slow-btn.on{background:var(--accent-soft);color:var(--accent);border-color:var(--accent)}

/* one-time tap-to-hear toast (replaces the old permanent hint bar) */
.hint-toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(8px);
  z-index:90;background:var(--paper);color:var(--soft);border:1px solid var(--line);
  border-radius:999px;padding:10px 18px;font-size:13.5px;box-shadow:var(--shadow);
  opacity:0;pointer-events:none;transition:opacity .4s ease,transform .4s ease;
  white-space:nowrap;max-width:92vw;overflow:hidden;text-overflow:ellipsis}
.hint-toast b{color:var(--accent)}
.hint-toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

/* what's tappable */
.ex .es,.dlg .es,p.es,li.es,span.es,.vocab td:first-child,.conj .v,.chip,
.card .front{cursor:pointer;-webkit-tap-highlight-color:transparent}
.vocab td:first-child,.conj .v,.ex .es,.dlg .es,p.es{
  text-decoration:underline dotted color-mix(in srgb,var(--accent) 50%,transparent);
  text-underline-offset:3px;text-decoration-thickness:1px}
.conj .v::after,.card .front::after,.chip::after{content:"♪";font-size:.78em;
  margin-left:6px;opacity:.5;color:var(--accent);vertical-align:middle}
.speaking{background:var(--accent-soft);border-radius:6px;
  box-shadow:0 0 0 4px var(--accent-soft);transition:background .1s}

/* stress popup (dark in both themes for consistent contrast) */
.stress-pop{position:absolute;z-index:100;background:#212426;color:#f1f3f3;
  padding:8px 13px;border-radius:11px;font-family:var(--round);font-weight:700;
  font-size:17px;box-shadow:0 8px 24px rgba(0,0,0,.3);pointer-events:none;
  white-space:nowrap;max-width:92vw;overflow:hidden;text-overflow:ellipsis}
.stress-pop b{color:#ffab9b;font-weight:800}
.stress-pop .dot2{opacity:.4;margin:0 1px}
.stress-pop .sp-ic{margin-right:6px}

/* ---------- charcoal gradient ground — on a fixed layer so it ALWAYS shows,
   including phones (background-attachment:fixed is broken on iOS) ---------- */
:root{
  --bggrad:
    radial-gradient(880px 520px at 88% -6%, rgba(255,143,125,.13) 0%, rgba(255,143,125,0) 60%),
    radial-gradient(1100px 720px at -12% 14%, rgba(95,214,165,.10) 0%, rgba(95,214,165,0) 55%),
    linear-gradient(160deg, #26292c 0%, #1c1f21 45%, #141617 80%, #0f1011 100%);
  --hover-shadow:0 2px 4px rgba(0,0,0,.4), 0 22px 48px rgba(0,0,0,.6);
}
@media (prefers-color-scheme: light){:root:not([data-theme]){
  --bggrad:
    radial-gradient(880px 520px at 88% -6%, rgba(232,96,74,.08) 0%, rgba(232,96,74,0) 60%),
    radial-gradient(1100px 720px at -12% 14%, rgba(31,169,126,.07) 0%, rgba(31,169,126,0) 55%),
    linear-gradient(160deg, #fafbfb 0%, #eef0f1 50%, #e4e7e8 100%);
  --hover-shadow:0 1px 2px rgba(30,35,40,.06), 0 18px 38px rgba(30,35,40,.14);
}}
:root[data-theme="light"]{
  --bggrad:
    radial-gradient(880px 520px at 88% -6%, rgba(232,96,74,.08) 0%, rgba(232,96,74,0) 60%),
    radial-gradient(1100px 720px at -12% 14%, rgba(31,169,126,.07) 0%, rgba(31,169,126,0) 55%),
    linear-gradient(160deg, #fafbfb 0%, #eef0f1 50%, #e4e7e8 100%);
  --hover-shadow:0 1px 2px rgba(30,35,40,.06), 0 18px 38px rgba(30,35,40,.14);
}
:root[data-theme="dark"]{
  --bggrad:
    radial-gradient(880px 520px at 88% -6%, rgba(255,143,125,.13) 0%, rgba(255,143,125,0) 60%),
    radial-gradient(1100px 720px at -12% 14%, rgba(95,214,165,.10) 0%, rgba(95,214,165,0) 55%),
    linear-gradient(160deg, #26292c 0%, #1c1f21 45%, #141617 80%, #0f1011 100%);
  --hover-shadow:0 2px 4px rgba(0,0,0,.4), 0 22px 48px rgba(0,0,0,.6);
}
body{background:var(--bg);min-height:100vh}
body::before{content:"";position:fixed;inset:0;z-index:-1;background:var(--bggrad)}

/* ---------- NO giant paper sheet: content floats on the gradient ---------- */
.page{background:transparent;box-shadow:none;border-radius:0;max-width:720px;
  margin:0 auto;padding:12px 20px 72px}
.box,.drill{background:var(--paper);box-shadow:var(--shadow)}
.tip{background:var(--accent-soft)}.trick{background:var(--sun-soft)}
.warn{background:var(--coral-soft)}.cuba{background:var(--cuba-soft)}
.sea{background:var(--sea-soft)}
table{background:var(--paper);border:1px solid var(--line);border-radius:14px;
  border-collapse:separate;border-spacing:0;box-shadow:var(--shadow);overflow:hidden}
th{background:transparent}
table tr:last-child td{border-bottom:none}
.tile,.chip,.cards .card,.qa{background:var(--paper);box-shadow:var(--shadow)}
.toc li{border-bottom-color:var(--line)}
.write-lines .ln{border-bottom-color:var(--faint)}

/* grown-up cover: no emoji flags, italic coral accent instead */
.cover{min-height:auto;padding:44px 0 8px}
.cover .flag{display:none}
.cover h1 em{font-style:italic;color:var(--accent)}
.cover .sub{font-size:16.5px}
.goals{list-style:none;margin-left:0}
.goals li{padding-left:26px;position:relative;margin:8px 0}
.goals li::before{content:"→";position:absolute;left:0;color:var(--accent);font-weight:700}

/* two-accent rhythm: tiles alternate salmon / mint */
.grid .tile:nth-child(even) .tn{color:var(--sea)}
@media (hover:hover){
  .grid .tile:nth-child(even):hover{border-color:var(--sea)}
}

/* dashboard "continue" card (salmon gradient, app-style) */
.go-card{display:flex;align-items:center;justify-content:space-between;gap:14px;
  background:linear-gradient(135deg,var(--accent) 0%,#ffb39f 100%);color:#20211f;
  border-radius:20px;padding:18px 20px;margin:4px 0 20px;box-shadow:var(--shadow);
  border:none}
.go-card .gc-k{font-family:var(--round);font-weight:800;font-size:11px;
  letter-spacing:.1em;text-transform:uppercase;opacity:.72}
.go-card .gc-t{font-family:var(--serif);font-weight:700;font-size:19px;line-height:1.2}
.go-card .gc-a{font-size:24px;font-weight:700;flex:0 0 auto}
@media (hover:hover){
  .go-card{transition:transform .16s ease, box-shadow .16s ease}
  .go-card:hover{transform:translateY(-2px);box-shadow:var(--hover-shadow)}
}

/* mobile: app-style floating bottom nav (top tabs hide) */
.bottomnav{display:none}
@media (max-width:640px){
  .wb-tabs{display:none}
  .page{padding-bottom:120px}
  .bottomnav{display:flex;position:fixed;left:12px;right:12px;bottom:12px;z-index:60;
    background:color-mix(in srgb,var(--paper) 94%,transparent);
    -webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);
    border:1px solid var(--line);border-radius:22px;box-shadow:var(--hover-shadow);
    justify-content:space-around;padding:8px 4px;
    padding-bottom:calc(8px + env(safe-area-inset-bottom,0px))}
  .bn-item{display:flex;flex-direction:column;align-items:center;gap:3px;
    font-family:var(--round);font-weight:700;font-size:10.5px;color:var(--faint);
    background:none;border:none;padding:6px 10px;border-radius:14px;cursor:pointer}
  .bn-item svg{width:20px;height:20px;stroke:currentColor;fill:none;
    stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .bn-item.on{color:var(--accent)}
  .bn-item:nth-child(even).on{color:var(--sea)}
}

/* ---------- flashcard detail sheet (slide-up, app style) ---------- */
.sheet-back{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:110;
  opacity:0;pointer-events:none;transition:opacity .25s}
.sheet-back.show{opacity:1;pointer-events:auto}
.wb-sheet{position:fixed;left:0;right:0;bottom:0;z-index:120;background:var(--paper);
  border:1px solid var(--line);border-bottom:none;border-radius:24px 24px 0 0;
  box-shadow:0 -18px 50px rgba(0,0,0,.5);max-height:86vh;display:flex;
  flex-direction:column;transform:translateY(103%);
  transition:transform .3s cubic-bezier(.2,.8,.2,1)}
.wb-sheet.show{transform:none}
@media (min-width:700px){
  .wb-sheet{left:50%;right:auto;width:620px;transform:translate(-50%,103%)}
  .wb-sheet.show{transform:translate(-50%,0)}
}
.sh-grab{width:44px;height:5px;border-radius:3px;background:var(--line);
  margin:10px auto 0;flex:0 0 auto}
.sh-x{position:absolute;top:12px;right:14px;width:34px;height:34px;border-radius:50%;
  background:var(--sand2);color:var(--soft);font-size:19px;line-height:1;z-index:2;
  border:none;cursor:pointer}
.sh-body{overflow-y:auto;padding:12px 22px calc(30px + env(safe-area-inset-bottom,0px))}
.sh-k{font-family:var(--round);font-weight:800;font-size:11px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--faint);margin-top:8px}
.sh-w{font-family:var(--serif);font-size:34px;font-weight:700;color:var(--accent);
  margin:2px 0 0;cursor:pointer}
.sh-w::after{content:"♪";font-size:.5em;margin-left:8px;opacity:.5;vertical-align:middle}
.sh-en{color:var(--soft);font-size:15px}
.sh-stress{font-family:var(--round);font-weight:700;color:var(--sea);font-size:15.5px;
  margin:5px 0 4px;letter-spacing:.02em}
.sh-stress b{color:var(--sea)}
.sh-body h4{margin:18px 0 6px}
@media (prefers-reduced-motion: reduce){
  .wb-sheet{transition:none}.sheet-back{transition:none}
}

/* tap-to-check practice rows */
.rev{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:9px 0;
  border-bottom:1px dashed var(--line)}
.rev-q{font-size:14.5px}
.rev-btn{font-family:var(--round);font-weight:700;font-size:12px;color:var(--sea);
  background:var(--sea-soft);border:none;border-radius:999px;padding:5px 13px;cursor:pointer}
.rev-ans{display:none;font-family:var(--serif);font-weight:700;font-size:16px;
  color:var(--sea);cursor:pointer}
.rev-ans.show{display:inline}

/* ---------- hover: lift + colored border ---------- */
@media (hover:hover){
  .box,.drill,.card,.tile,.chip,.conj,.qa{
    transition:transform .16s ease, box-shadow .16s ease, border-color .16s ease}
  .box:hover,.drill:hover,.card:hover,.tile:hover,.qa:hover{
    transform:translateY(-3px);box-shadow:var(--hover-shadow);border-color:var(--accent)}
  .trick:hover{border-color:var(--sun)}
  .warn:hover{border-color:var(--coral)}
  .cuba:hover{border-color:var(--cuba)}
  .sea:hover{border-color:var(--sea)}
  .tip:hover{border-color:var(--accent)}
  .card:hover .front{color:var(--accent)}
  .conj:hover{border-color:var(--accent);box-shadow:var(--hover-shadow)}
  .chip:hover{transform:translateY(-1px);border-color:var(--accent);color:var(--accent)}
}
@media (prefers-reduced-motion: reduce){
  .box,.drill,.card,.tile,.chip,.conj,.qa{transition:border-color .16s ease}
  .box:hover,.drill:hover,.card:hover,.tile:hover,.qa:hover,.chip:hover{transform:none}
}
"""

TAB_ORDER = [
    ("contents", "Contents"), ("book", "The Book"), ("practice", "Practice"),
    ("answers", "Answers"), ("flashcards", "Flashcards"),
    ("cheatsheets", "Cheat Sheets"), ("tests", "Tests"),
]

def _detail_json():
    import json
    return json.dumps(DETAIL, ensure_ascii=False).replace('</', '<\\/')


def _to_tabs(html):
    """Rewrite cross-file links into in-page tab switches."""
    m = {"index.html": "contents", "book.html": "book", "practice.html": "practice",
         "answers.html": "answers", "flashcards.html": "flashcards",
         "cheatsheets.html": "cheatsheets", "tests.html": "tests"}
    for f, tab in m.items():
        html = html.replace(f'href="{f}"', f'href="#{tab}" data-tab="{tab}"')
    return html


def build_artifact(bodies):
    nav = "".join(
        f'<button class="wb-tab" data-tab="{k}">{esc(label)}</button>'
        for k, label in TAB_ORDER)
    sections = []
    for k, _ in TAB_ORDER:
        inner = _to_tabs(bodies[k])
        sections.append(f'<section class="tab" id="tab-{k}">'
                        f'<div class="page">{inner}</div></section>')

    js = r"""
(function(){
  // ---------- tabs ----------
  function show(name){
    document.querySelectorAll('.tab').forEach(function(s){
      s.classList.toggle('on', s.id==='tab-'+name); });
    document.querySelectorAll('.wb-tab,.bn-item').forEach(function(b){
      b.classList.toggle('on', b.dataset.tab===name); });
    window.scrollTo({top:0,behavior:'instant'});
    hidePop();
  }

  // ---------- Spanish syllabifier + stress (rule-based) ----------
  var VOWELS='aeiouáéíóúü', ACCENTED='áéíóú', STRONG='aeoáéó';
  var CLUSTERS=['ch','ll','rr','pr','pl','br','bl','cr','cl','dr','tr','gr','gl','fr','fl'];
  function isV(c){return VOWELS.indexOf(c)>=0;}
  function syllabify(word){
    var w=word.toLowerCase(), nuclei=[], i=0;
    while(i<w.length){
      if(isV(w[i])){
        var j=i;
        while(j+1<w.length && isV(w[j+1])){
          var a=w[j], b=w[j+1];
          var hiatus=(STRONG.indexOf(a)>=0&&STRONG.indexOf(b)>=0)||
                     ('íú'.indexOf(a)>=0)||('íú'.indexOf(b)>=0);
          if(hiatus) break; j++;
        }
        nuclei.push([i,j]); i=j+1;
      } else i++;
    }
    if(nuclei.length<=1) return [word];
    var bounds=[0];
    for(var n=0;n<nuclei.length-1;n++){
      var cStart=nuclei[n][1]+1, cEnd=nuclei[n+1][0]-1, cons=w.slice(cStart,cEnd+1), L=cons.length, splitAt;
      if(L===0) splitAt=nuclei[n+1][0];
      else if(L===1) splitAt=cStart;
      else if(L===2) splitAt=CLUSTERS.indexOf(cons)>=0?cStart:cStart+1;
      else if(L===3) splitAt=CLUSTERS.indexOf(cons.slice(1))>=0?cStart+1:cStart+2;
      else splitAt=cStart+2;
      bounds.push(splitAt);
    }
    var syl=[];
    for(var b2=0;b2<bounds.length;b2++){
      var st=bounds[b2], en=(b2+1<bounds.length)?bounds[b2+1]:word.length;
      syl.push(word.slice(st,en));
    }
    return syl;
  }
  function stressIndex(s){
    for(var k=0;k<s.length;k++){var t=s[k].toLowerCase();
      for(var c=0;c<t.length;c++) if(ACCENTED.indexOf(t[c])>=0) return k;}
    if(s.length===1) return 0;
    var last=s[s.length-1].toLowerCase(), lc=last[last.length-1];
    return ('aeiouns'.indexOf(lc)>=0)?s.length-2:s.length-1;
  }
  function markHTML(word){
    var s=syllabify(word), idx=stressIndex(s), out=[];
    for(var k=0;k<s.length;k++)
      out.push(k===idx?('<b>'+s[k].toUpperCase()+'</b>'):s[k].toLowerCase());
    return out.join('<span class="dot2">·</span>');
  }
  function markPhrase(text){
    return text.trim().split(/\s+/).map(function(tok){
      var m=tok.match(/^([¿¡"'(]*)([\wáéíóúüñ]+)([.,!?;:"')]*)$/i);
      return m ? (m[1]+markHTML(m[2])+m[3]) : tok;
    }).join(' ');
  }

  // ---------- speech (phone's built-in Spanish voice) ----------
  var VOICE=null, SLOW=false;
  function loadVoices(){
    if(!('speechSynthesis' in window)) return;
    var vs=speechSynthesis.getVoices()||[];
    var order=['es-us','es-mx','es-419','es-co','es-ar','es-es','es'];
    VOICE=null;
    for(var i=0;i<order.length&&!VOICE;i++)
      VOICE=vs.filter(function(v){return v.lang&&v.lang.toLowerCase().indexOf(order[i])===0;})[0]||null;
    if(!VOICE) VOICE=vs.filter(function(v){return /^es/i.test(v.lang||'');})[0]||null;
  }
  if('speechSynthesis' in window){ loadVoices(); speechSynthesis.onvoiceschanged=loadVoices; }
  function speak(text, el){
    if(!('speechSynthesis' in window)||!text) return;
    try{
      speechSynthesis.cancel();
      var u=new SpeechSynthesisUtterance(text);
      if(VOICE){u.voice=VOICE; u.lang=VOICE.lang;} else u.lang='es-US';
      u.rate=SLOW?0.6:0.92;
      if(el){el.classList.add('speaking');
        u.onend=u.onerror=function(){el.classList.remove('speaking');};}
      speechSynthesis.speak(u);
    }catch(e){}
  }

  // ---------- stress popup ----------
  var pop=null;
  function ensurePop(){ if(!pop){pop=document.createElement('div');
    pop.className='stress-pop';pop.style.display='none';document.body.appendChild(pop);} return pop; }
  function hidePop(){ if(pop) pop.style.display='none'; }
  function showPop(html, rect){
    var p=ensurePop();
    p.innerHTML='<span class="sp-ic">🔊</span>'+html;
    p.style.left='0px'; p.style.top='0px'; p.style.display='block';
    var pw=p.offsetWidth, ph=p.offsetHeight, cw=document.documentElement.clientWidth;
    var top=rect.top+window.scrollY-ph-10;
    if(top<window.scrollY+4) top=rect.bottom+window.scrollY+10;
    var left=rect.left+window.scrollX+rect.width/2-pw/2;
    left=Math.max(window.scrollX+8, Math.min(left, window.scrollX+cw-pw-8));
    p.style.top=top+'px'; p.style.left=left+'px';
    clearTimeout(p._t); p._t=setTimeout(hidePop, 4500);
  }

  function esText(el){
    var c=el.cloneNode(true);
    c.querySelectorAll('.en,.ipa,.small').forEach(function(n){n.remove();});
    return (c.textContent||'').replace(/🔊/g,'').trim();
  }

  // ---------- flashcard detail sheet ----------
  var sheetBack=document.getElementById('sheetBack'),
      wbSheet=document.getElementById('wbSheet'),
      sheetBody=document.getElementById('sheetBody');
  function openSheet(key){
    var d=(window.WB_DETAIL||{})[key]; if(!d||!wbSheet) return;
    sheetBody.innerHTML=d; sheetBody.scrollTop=0;
    var w=sheetBody.querySelector('[data-sheetword]');
    var slot=sheetBody.querySelector('.sh-stress');
    if(w){var txt=w.getAttribute('data-sheetword');
      if(slot){
        if(txt.split(/\s+/).length<=3 && /[a-záéíóúñü]/i.test(txt))
          slot.innerHTML=markPhrase(txt);
        else slot.style.display='none';
      }
      speak(txt);
    }
    sheetBack.classList.add('show'); wbSheet.classList.add('show');
  }
  function closeSheet(){
    if(!wbSheet) return;
    sheetBack.classList.remove('show'); wbSheet.classList.remove('show');
  }
  if(sheetBack) sheetBack.addEventListener('click', closeSheet);
  document.addEventListener('keydown', function(e){ if(e.key==='Escape') closeSheet(); });

  var SEL='.ex .es,.dlg .es,p.es,li.es,span.es,.vocab td:first-child,.conj .v,.chip,.sh-w';
  document.addEventListener('click', function(e){
    if(e.target.closest('[data-tab]')){ e.preventDefault(); closeSheet(); show(e.target.closest('[data-tab]').getAttribute('data-tab')); return; }
    if(e.target.closest('.sh-x')){ closeSheet(); return; }
    var rb=e.target.closest('.rev-btn');
    if(rb){ var ans=rb.nextElementSibling;
      if(ans) ans.classList.add('show');
      rb.style.display='none'; speak(rb.getAttribute('data-es')); return; }
    var ra=e.target.closest('.rev-ans.show');
    if(ra){ speak(ra.textContent); return; }
    var cd=e.target.closest('.card[data-key]');
    if(cd){ openSheet(cd.getAttribute('data-key')); return; }
    if(e.target.closest('.slow-btn')) return;
    var t=e.target.closest(SEL);
    if(!t){ hidePop(); return; }
    var text=esText(t);
    if(!text) return;
    speak(text, t);
    var words=text.split(/\s+/);
    if(words.length<=3 && /[a-záéíóúñü]/i.test(text) && !t.closest('.wb-sheet'))
      showPop(markPhrase(text), t.getBoundingClientRect());
    else hidePop();
  });
  window.addEventListener('scroll', hidePop, {passive:true});

  // ---------- controls ----------
  var sb=document.getElementById('slowBtn');
  if(sb) sb.addEventListener('click', function(){ SLOW=!SLOW; sb.classList.toggle('on',SLOW);
    sb.setAttribute('aria-pressed', SLOW?'true':'false'); });

  // one-time hint toast
  try{
    if(!localStorage.getItem('wbHintSeen')){
      var ht=document.getElementById('hintToast');
      if(ht){ setTimeout(function(){ ht.classList.add('show'); }, 900);
        setTimeout(function(){ ht.classList.remove('show'); }, 7500);
        localStorage.setItem('wbHintSeen','1'); }
    }
  }catch(e){}

  show('contents');
})();
"""
    body = (f'<style>{THEME_CSS}{ARTIFACT_EXTRA_CSS}</style>'
            '<div class="wb-header"><div class="wb-bar">'
            '<span class="wb-brand">Hablar<span class="dot">.</span></span>'
            f'<nav class="wb-tabs">{nav}</nav>'
            '<button id="slowBtn" class="slow-btn" title="Slow speech" '
            'aria-pressed="false">Slow</button>'
            '</div></div>'
            '<div class="hint-toast" id="hintToast">♪ Tap any <b>Spanish word or '
            'sentence</b> to hear it</div>'
            + "".join(sections)
            + '<nav class="bottomnav">'
            '<button class="bn-item" data-tab="contents">'
            '<svg viewBox="0 0 24 24"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/></svg>'
            'Home</button>'
            '<button class="bn-item" data-tab="book">'
            '<svg viewBox="0 0 24 24"><path d="M4 4h7v16H6a2 2 0 0 1-2-2V4Z"/><path d="M20 4h-7v16h5a2 2 0 0 0 2-2V4Z"/></svg>'
            'Book</button>'
            '<button class="bn-item" data-tab="practice">'
            '<svg viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>'
            'Practice</button>'
            '<button class="bn-item" data-tab="flashcards">'
            '<svg viewBox="0 0 24 24"><rect x="3" y="6" width="13" height="12" rx="2"/><path d="M8 6V5a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-1"/></svg>'
            'Cards</button>'
            '<button class="bn-item" data-tab="tests">'
            '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="m8.5 12.5 2.5 2.5 5-6"/></svg>'
            'Tests</button>'
            '</nav>'
            '<div class="sheet-back" id="sheetBack"></div>'
            '<div class="wb-sheet" id="wbSheet" role="dialog" aria-modal="true">'
            '<div class="sh-grab"></div>'
            '<button class="sh-x" aria-label="Close">&times;</button>'
            '<div class="sh-body" id="sheetBody"></div></div>'
            + f'<script>window.WB_DETAIL={_detail_json()};</script>'
            + f'<script>{js}</script>')
    w("hablar-workbook.html", body)
    return body


# ══════════════════════════════════════════════════════════════════════════
# STANDALONE INSTALLABLE APP  (full-screen PWA, offline, home-screen icon)
# ══════════════════════════════════════════════════════════════════════════
PWA_MANIFEST = """{
  "name": "Spanish for Your Real Life",
  "short_name": "Mi Español",
  "description": "Jenna's personalized Spanish workbook — beach life, Maggie, coffee, cooking, and Cuban & Colombian Spanish.",
  "start_url": "./index.html",
  "scope": "./",
  "display": "standalone",
  "orientation": "portrait",
  "background_color": "#1a1c1e",
  "theme_color": "#1a1c1e",
  "lang": "en",
  "icons": [
    {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
    {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"}
  ]
}
"""

PWA_SW = """/* Offline cache for the standalone workbook app */
const CACHE = 'hablar-workbook-v1';
const ASSETS = ['./', './index.html', './manifest.webmanifest',
  './icon-192.png', './icon-512.png', './apple-touch-icon.png'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks =>
    Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(res => {
    const copy = res.clone();
    caches.open(CACHE).then(c => c.put(e.request, copy)).catch(() => {});
    return res;
  }).catch(() => caches.match('./index.html'))));
});
"""

def build_pwa(body):
    sw_reg = ("if('serviceWorker' in navigator){window.addEventListener('load',"
              "function(){navigator.serviceWorker.register('sw.js').catch(function(){})});}")
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"/>
<title>Mi Español · Personalized Workbook</title>
<meta name="description" content="Jenna's personalized Spanish workbook."/>
<meta name="theme-color" content="#1a1c1e"/>
<link rel="manifest" href="manifest.webmanifest"/>
<meta name="mobile-web-app-capable" content="yes"/>
<meta name="apple-mobile-web-app-capable" content="yes"/>
<meta name="apple-mobile-web-app-status-bar-style" content="default"/>
<meta name="apple-mobile-web-app-title" content="Mi Español"/>
<link rel="apple-touch-icon" href="apple-touch-icon.png"/>
<link rel="icon" type="image/png" href="icon-192.png"/>
</head>
<body>
{body}
<script>{sw_reg}</script>
</body>
</html>"""
    with open(os.path.join(OUT, "app", "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    with open(os.path.join(OUT, "app", "manifest.webmanifest"), "w", encoding="utf-8") as f:
        f.write(PWA_MANIFEST)
    with open(os.path.join(OUT, "app", "sw.js"), "w", encoding="utf-8") as f:
        f.write(PWA_SW)
    print("wrote app/index.html, app/manifest.webmanifest, app/sw.js "
          f"({len(doc)//1024} KB)")


if __name__ == "__main__":
    bodies = {
        "index":       build_index(),
        "contents":    None,   # filled below (alias of index)
        "book":        build_book(),
        "practice":    build_practice(),
        "answers":     build_answers(),
        "flashcards":  build_flashcards(),
        "cheatsheets": build_cheats(),
        "tests":       build_tests(),
    }
    bodies["contents"] = bodies["index"]
    combined = build_artifact(bodies)
    build_pwa(combined)
    print("\n✅ Workbook built (7 print files + combined artifact + installable app).")
