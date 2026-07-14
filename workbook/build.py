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
from content.verbs import VERBS
from content.vocab import THEMES
from content import extras

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
    h.append(box('sea', 'Latin-America note',
        '<p>Your boyfriend\'s family uses <span class="es">ustedes</span> for '
        '“you all” — the <span class="es">vosotros</span> form is Spain only. '
        'Learn it to recognize it, but you\'ll speak with the others.</p>'))

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
    h.append(f'<h1><span style="font-size:1.1em">{t["icon"]}</span> &nbsp;{esc(t["title"])}</h1>')
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
        '<div class="flag">🇺🇸 🇨🇺</div>'
        '<h1>Spanish<br>for Your Real Life</h1>'
        '<div class="sub">A personalized workbook — built around the beach, your '
        'dogs, the gym, coffee, cooking, and the Cuban Spanish your boyfriend '
        'actually speaks.</div>'
        '<div class="who">Personalized for Celeste · Florida</div>'
        '</div>')

    # goals
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Your Goal</h1>')
    parts.append('<p>When we\'re finished, you will be able to:</p>')
    parts.append('<ul style="list-style:none;margin-left:0">'
        '<li>✅ Have a 20–30 minute conversation with your tutor.</li>'
        '<li>✅ Talk naturally with your boyfriend.</li>'
        '<li>✅ Read simple books.</li>'
        '<li>✅ Watch beginner Spanish YouTube.</li>'
        '<li>✅ Think in Spanish instead of translating.</li>'
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

    # Part III — vocab
    parts.append('<div class="page-break"></div>')
    parts.append('<div class="eyebrow">Part III</div>')
    parts.append('<h1>Real-Life Vocabulary</h1>')
    parts.append('<p class="muted">Forget “the airport” and “the museum.” '
        'We learn <em>your</em> life first — the beach, your dogs, the garden, the '
        'gym, coffee, cooking, work, and love — so every word is one you\'ll '
        'actually use this week.</p>')
    parts.append(chips([(t["icon"] + " " + t["title"], "") for t in THEMES]))
    for i, t in enumerate(THEMES, 1):
        parts.append(render_vocab_teach(t, i))

    # Parts IV–VII
    for fn in (extras.part4_past, extras.part5_reading,
               extras.part6_speaking, extras.part7_cuban):
        parts.append('<div class="page-break"></div>')
        parts.append(fn())

    parts.append('<div class="page-break"></div>')
    parts.append('<h1>¡Lo lograste! 🎉</h1>')
    parts.append('<p>You reached the end of the teaching book. Now the real work — '
        'and the fun — begins: use it. Do the practice pages, drill the flashcards, '
        'and above all, <strong>speak</strong>. Every mistake is a rep. '
        '<span class="es">¡Dale, tú puedes!</span></p>')

    w("book.html", shell("Hablar Workbook · The Book", "".join(parts),
                         subtitle="Parts I–VII"))


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
    h.append(f'<h2>{t["icon"]} {esc(t["title"])}</h2>')
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
        '<div class="flag">✍️</div>'
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
    parts.append('<div class="page-break"></div>')
    parts.append('<div class="eyebrow">Unit 4</div>')
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

    w("practice.html", shell("Hablar Workbook · Practice", "".join(parts),
                             subtitle="Practice Workbook"))


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
    parts.append('<div class="cover"><div class="flag">🔑</div>'
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
        parts.append(f'<h2>{t["icon"]} {esc(t["title"])}</h2>')
        parts.append('<p class="small"><strong>A · Fill in the blank.</strong></p>')
        for s, a in t["fill"]:
            parts.append(_ans_row(esc(s.replace("___", "____")), a))
        parts.append('<p class="small"><strong>B · Translation.</strong></p>')
        for en, es in t["translate"]:
            parts.append(_ans_row(esc(en), es))
        parts.append('<hr>')

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

    w("answers.html", shell("Hablar Workbook · Answers", "".join(parts),
                            subtitle="Answer Book"))


# ══════════════════════════════════════════════════════════════════════════
# FLASHCARDS
# ══════════════════════════════════════════════════════════════════════════
def build_flashcards():
    parts = []
    parts.append('<div class="cover"><div class="flag">🃏</div>'
        '<h1>Flashcards</h1>'
        '<div class="sub">Every vocabulary word in the workbook. Print, cut along '
        'the dashed lines, and drill 5 minutes a day.</div>'
        '<div class="who">Spanish → English · fold or cut</div></div>')

    # verbs deck
    parts.append('<div class="page-break"></div>')
    parts.append('<h1>Deck 1 · The 16 Verbs</h1>')
    verb_cards = []
    for v in VERBS:
        yo = v["conj"][0][1]
        verb_cards.append((v["inf"].lower(), v["meaning"].split("(")[0].strip(),
                           f'yo → {yo}'))
    parts.append(_cards(verb_cards))

    # vocab decks by theme
    for t in THEMES:
        parts.append('<div class="page-break"></div>')
        parts.append(f'<h1>{t["icon"]} {esc(t["title"])}</h1>')
        cards = [(es, en, note) for es, en, note in t["vocab"]]
        parts.append(_cards(cards))

    w("flashcards.html", shell("Hablar Workbook · Flashcards", "".join(parts),
                               subtitle="Flashcards"))


def _cards(items):
    out = ['<div class="cards">']
    for front, back, tag in items:
        tag_h = f'<div class="tag">{esc(tag)}</div>' if tag else ''
        out.append(f'<div class="card"><div class="front">{esc(front)}</div>'
                   f'<div class="back">{esc(back)}</div>{tag_h}</div>')
    out.append('</div>')
    return "".join(out)


# ══════════════════════════════════════════════════════════════════════════
# TESTS
# ══════════════════════════════════════════════════════════════════════════
def build_tests():
    parts = []
    parts.append('<div class="cover"><div class="flag">📝</div>'
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

    w("tests.html", shell("Hablar Workbook · Tests", "".join(parts),
                          subtitle="Progress Tests & Final Exam"))


# ══════════════════════════════════════════════════════════════════════════
# CHEAT SHEETS + INDEX
# ══════════════════════════════════════════════════════════════════════════
def build_cheats():
    w("cheatsheets.html", shell("Hablar Workbook · Cheat Sheets",
        extras.cheat_sheets(), subtitle="Cheat Sheets"))


def build_index():
    tiles = [
        ("book.html", "📘", "The Book", "Parts I–VII: foundations, the 16 core "
         "verbs, real-life vocabulary, past tense, reading, speaking & Cuban Spanish."),
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
        '<div class="flag">🇺🇸 🇨🇺</div>'
        '<h1 style="font-size:46px">Spanish for Your Real Life</h1>'
        '<div class="sub">Your personalized workbook — the beach, your dogs, coffee, '
        'cooking, the gym, and the Cuban Spanish your boyfriend actually speaks.</div>'
        '<div class="who">Personalized for Celeste · Florida</div></div>')

    body.append('<h2>What\'s inside</h2>')
    body.append('<div class="grid">')
    for href, ic, tt, dd in tiles:
        body.append(f'<a class="tile" href="{href}"><div class="ic">{ic}</div>'
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
    body.append(toc("Part III · Real-Life Vocabulary", " ".join(t["icon"] for t in THEMES)
        + " " + ", ".join(t["title"] for t in THEMES)))
    body.append(toc("Part IV · Past Tense", "Regular & irregular preterite, yesterday, "
        "trips, stories, exercises"))
    body.append(toc("Part V · Reading", "From 5-word stories up to a full page — "
        "vocab, grammar, questions, writing prompts"))
    body.append(toc("Part VI · Speaking", "Hundreds of conversation questions, "
        "role-plays, and the 20-minute conversation ladder"))
    body.append(toc("Part VII · Cuban Spanish", "Expressions, slang, pronunciation, "
        "culture — what your boyfriend actually says"))
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

    w("index.html", shell("Hablar · Personalized Spanish Workbook", "".join(body),
                          subtitle="Contents", show_nav=True))


if __name__ == "__main__":
    build_index()
    build_book()
    build_practice()
    build_answers()
    build_flashcards()
    build_cheats()
    build_tests()
    print("\n✅ Workbook built.")
