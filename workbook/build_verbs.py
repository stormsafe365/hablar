#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the VERB WORKBOOK — a dedicated companion to the Hablar workbook that
teaches the Spanish *verb system*: present tense as patterns, then a gentle
on-ramp into the past and future.

Run:  python3 build_verbs.py
Outputs into  ./verbs/ :
  index.html        landing page + how-to-use + table of contents
  book.html         the teaching (Chapters 1–13)
  practice.html     exercises to write in
  answers.html      every answer, worked out
  quizzes.html      quizzes + cumulative final (with answer key)
  cheatsheets.html  one-page references
  reference.html    full conjugation tables for ~45 verbs
"""
import os

from content.theme import (shell, box, examples, dialogue, conj_table, chips,
    write_lines, drill, blank, esc)
from content import verb_book as vb

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verbs")
os.makedirs(OUT, exist_ok=True)


def w(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote verbs/%s (%d KB)" % (name, len(html) // 1024))


# ── verb-workbook nav + a little extra CSS ──────────────────────────────────
NAV = """
<div class="no-print" style="max-width:820px;margin:0 auto;padding:10px 16px;
  display:flex;gap:14px;flex-wrap:wrap;font-family:var(--round);font-weight:700;
  font-size:13px">
  <a href="../index.html">&larr; Main&nbsp;Workbook</a>
  <a href="index.html">Verbs&nbsp;Home</a>
  <a href="book.html">Learn</a>
  <a href="practice.html">Practice</a>
  <a href="answers.html">Answers</a>
  <a href="quizzes.html">Quizzes</a>
  <a href="cheatsheets.html">Cheat&nbsp;Sheets</a>
  <a href="reference.html">Reference</a>
</div>
"""

EXTRA_CSS = """
<style>
.pattern-badge{display:inline-block;font-family:var(--round);font-weight:800;
  font-size:11px;text-transform:uppercase;letter-spacing:.08em;padding:3px 10px;
  border-radius:999px;background:var(--accent-soft);color:var(--accent);
  border:1px solid #cfe9dd;margin-bottom:8px}
.tense-tag{display:inline-block;font-family:var(--round);font-weight:800;
  font-size:11px;text-transform:uppercase;letter-spacing:.06em;padding:2px 8px;
  border-radius:6px;margin-right:6px}
.tt-past{background:var(--sun-soft);color:var(--sun)}
.tt-pres{background:var(--accent-soft);color:var(--accent)}
.tt-fut{background:var(--sea-soft);color:var(--sea)}
table.grid-conj{border:1px solid var(--line);border-radius:12px;overflow:hidden;
  border-collapse:separate;border-spacing:0;font-size:14.5px}
table.grid-conj th{background:var(--bg);font-family:var(--round);font-weight:800;
  font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--soft)}
table.grid-conj td:first-child{color:var(--soft)}
table.grid-conj .v{color:var(--accent);font-weight:700}
table.grid-conj .boot{background:var(--sun-soft)}
.endgrid td:first-child{color:var(--soft);width:28%}
.endgrid .v{color:var(--cuba);font-weight:800;font-family:var(--round)}
.timeline{border:1px solid var(--line);border-radius:14px;overflow:hidden;margin:16px 0}
.timeline table{margin:0}
.timeline .en{display:block;font-size:13px;color:var(--soft)}
.steps{counter-reset:step;list-style:none;margin:14px 0;padding:0}
.steps li{position:relative;padding:10px 0 10px 44px;border-bottom:1px solid var(--line)}
.steps li:last-child{border-bottom:none}
.steps li::before{counter-increment:step;content:counter(step);position:absolute;
  left:0;top:8px;width:28px;height:28px;border-radius:50%;background:var(--accent);
  color:#fff;font-family:var(--round);font-weight:800;display:flex;
  align-items:center;justify-content:center;font-size:14px}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:13px;color:var(--soft);margin:8px 0}
.legend b{color:var(--ink)}
</style>
"""


def shell_v(title, body, subtitle=""):
    """Wrap in the theme shell but inject our own nav + extra CSS."""
    full = NAV + EXTRA_CSS + body
    return shell(title, full, subtitle=subtitle, show_nav=False)


# ── local renderers ─────────────────────────────────────────────────────────
def eyebrow(text):
    return f'<div class="eyebrow">{esc(text)}</div>'


def grid_conj(verbs, boot=False):
    """verbs: list of (title, [6 forms]). Rows = the shown pronouns (no vosotros).
    If boot=True, highlight every shown row except nosotros (the flat one)."""
    head = "<tr><th></th>" + "".join(f"<th>{esc(t)}</th>" for t, _ in verbs) + "</tr>"
    rows = []
    for i in vb.SHOW:
        pro = vb.PRON_SHORT[i]
        cls = ' class="boot"' if boot and i not in (3, 4) else ""
        cells = "".join(f'<td class="v"{cls}>{esc(f[i])}</td>' for _, f in verbs)
        rows.append(f'<tr><td{cls}>{esc(pro)}</td>{cells}</tr>')
    return ('<div style="overflow-x:auto"><table class="grid-conj"><thead>' + head
            + "</thead><tbody>" + "".join(rows) + "</tbody></table></div>")


def endings_table(caption, rows):
    """rows: list of (pron, ending). Shows just endings."""
    body = "".join(f'<tr><td>{esc(p)}</td><td class="v">{esc(e)}</td></tr>' for p, e in rows)
    cap = f'<h4>{esc(caption)}</h4>' if caption else ""
    return cap + '<table class="conj endgrid"><tbody>' + body + "</tbody></table>"


def verb_block(v, show_examples=3):
    """A single irregular verb: badge, conjugation, hook, examples."""
    h = [f'<h4 style="margin-top:20px">{esc(v["inf"])} <span class="muted" '
         f'style="font-weight:400">— {esc(v["en"])}</span></h4>']
    h.append(conj_table("", v["conj"]))
    h.append(box("trick", "Hook", f'<p>{v["hook"]}</p>'))
    if show_examples:
        h.append(examples(v["examples"][:show_examples]))
    return "".join(h)


def two_col_uses(title, cls, rows):
    """rows: (use, es, en)."""
    out = [f'<div class="box {cls}"><span class="lead">{esc(title)}</span>']
    for use, es, en in rows:
        out.append(f'<p style="margin:8px 0"><b>{esc(use)}</b><br>'
                   f'<span class="es">{esc(es)}</span> '
                   f'<span class="en">— {esc(en)}</span></p>')
    out.append("</div>")
    return "".join(out)


# ══════════════════════════════════════════════════════════════════════════
#  PAGE 1 — LANDING
# ══════════════════════════════════════════════════════════════════════════
def build_index():
    b = []
    b.append('<div class="cover">')
    b.append('<div class="flag">🇪🇸 🇨🇺 ✍️</div>')
    b.append('<h1>The Verb Book</h1>')
    b.append('<p class="sub">Master Spanish verbs the smart way — not by memorizing '
             'a thousand forms, but by learning the handful of <em>patterns</em> they '
             'follow. Deep on the present tense, with a friendly first step into the '
             'past and the future.</p>')
    b.append('<div class="who">A Hablar companion · made for Celeste</div>')
    b.append("</div>")

    b.append('<div class="page-break"></div>')
    b.append(eyebrow("Start here"))
    b.append("<h2>How to use this book</h2>")
    b.append('<p>Verbs are the engine of every sentence. Once you can drive them, you '
             'can say almost anything. This book is built around one big idea from your '
             'notes:</p>')
    b.append(box("tip", "The one idea that changes everything",
        "<p>You don't memorize every verb as if it were unique. You ask <b>which "
        "pattern</b> it follows. There are only a few patterns — learn them once and "
        "every new verb slots into place.</p>"))
    b.append('<ol class="steps">'
        '<li><b>Read a chapter</b> in <a href="book.html">Learn</a>. Say every example '
        'out loud — your mouth learns verbs faster than your eyes.</li>'
        '<li><b>Do the matching exercises</b> in the <a href="practice.html">Practice</a> '
        'book. Write by hand; that\'s where it sticks.</li>'
        '<li><b>Check yourself</b> in <a href="answers.html">Answers</a> — every one is '
        'explained, not just listed.</li>'
        '<li><b>Test it</b> with the <a href="quizzes.html">Quizzes</a> when a section '
        'feels solid.</li>'
        '<li>Keep the <a href="cheatsheets.html">Cheat Sheets</a> and '
        '<a href="reference.html">Reference</a> tables next to you the whole time.</li>'
        '</ol>')
    b.append(box("cuba", "Your Latin-American reality",
        "<p>Your boyfriend's family speaks Cuban Spanish. They use <span class='es'>"
        "ustedes</span> for “you all,” so every table in this book uses the "
        "five persons you'll actually speak with. Spain's "
        "<span class='es'>vosotros</span> is left out on purpose — one less form "
        "to learn.</p>"))

    b.append('<div class="page-break"></div>')
    b.append(eyebrow("Contents"))
    b.append("<h2>What's inside</h2>")
    tiles = [
        ("book.html", "📗", "Learn", "13 chapters: how verbs work, the four irregular "
         "patterns, ser vs estar, reflexives, gustar, and your first past & future tenses."),
        ("practice.html", "✍️", "Practice", "Conjugation grids, fill-in-the-blank, "
         "translation, and free-writing — organized to follow every chapter."),
        ("answers.html", "🔑", "Answers", "Every exercise worked out, with a short "
         "“why” so mistakes turn into understanding."),
        ("quizzes.html", "📝", "Quizzes", "Five quizzes plus a cumulative final — built "
         "in the same style as your original quiz, but much bigger."),
        ("cheatsheets.html", "📎", "Cheat Sheets", "Endings for all four tenses, the "
         "irregular-yo list, the boot diagram, ser/estar triggers, time-word signals."),
        ("reference.html", "📚", "Reference", "Full conjugation tables for ~45 verbs — "
         "the ones from your real life."),
    ]
    b.append('<div class="grid">')
    for href, ic, tt, dd in tiles:
        b.append(f'<a class="tile" href="{href}"><div class="ic">{ic}</div>'
                 f'<div class="tt">{esc(tt)}</div><div class="dd">{esc(dd)}</div></a>')
    b.append("</div>")

    b.append(box("tip", "The map of this book",
        "<p><span class='tense-tag tt-pres'>Now</span> Chapters 1–10 make the "
        "<b>present tense</b> second nature. "
        "<span class='tense-tag tt-past'>Before</span> Chapter 11 opens the "
        "<b>past</b>. <span class='tense-tag tt-fut'>Later</span> Chapter 12 opens the "
        "<b>future</b>, and Chapter 13 puts all three on one timeline.</p>"))

    w("index.html", shell_v("The Verb Book · Hablar", "".join(b),
                            subtitle="The Verb Book"))


# ══════════════════════════════════════════════════════════════════════════
#  PAGE 2 — LEARN (the teaching)
# ══════════════════════════════════════════════════════════════════════════
def chapter(n, title, kicker=""):
    br = '<div class="page-break"></div>' if n > 1 else ''
    k = eyebrow(kicker or f"Chapter {n}")
    return f'{br}{k}<h1>{esc(title)}</h1>'


def build_book():
    b = []

    # ---------- Ch 1: How Spanish verbs work ----------
    b.append(chapter(1, "How Spanish verbs work", "Chapter 1 · The mental model"))
    b.append('<p>Every Spanish verb starts life as an <b>infinitive</b> — the '
             '“to ___” form. You can spot it instantly because it ends in one '
             'of three ways:</p>')
    b.append(chips([("-ar", "hablar · to speak"), ("-er", "comer · to eat"),
                    ("-ir", "vivir · to live")]))
    b.append('<p>A conjugated verb is just two pieces glued together:</p>')
    b.append(box("tip", "Stem + ending",
        "<p><b>habl</b> (the stem — the meaning) &nbsp;+&nbsp; <b>-o</b> (the ending — "
        "who's doing it) &nbsp;=&nbsp; <span class='es'>hablo</span> "
        "(“I speak”).</p><p>The ending does a job English needs a pronoun for. "
        "That's why Spanish can drop the pronoun: <span class='es'>hablo</span> already "
        "means <em>I</em> speak.</p>"))

    b.append("<h3>The five people you'll use (subject pronouns)</h3>")
    b.append(conj_table("", [
        ("yo", "I"), ("tú", "you (friendly)"),
        ("él / ella / usted", "he / she / you (polite)"),
        ("nosotros", "we"),
        ("ellos / ellas / ustedes", "they / you all")]))
    b.append(box("cuba", "Two quick notes for real life",
        "<p><b>tú vs usted:</b> use <span class='es'>tú</span> with friends, family, "
        "your boyfriend; <span class='es'>usted</span> to be respectful with strangers "
        "or elders. <br><b>ustedes:</b> in Cuba and all of Latin America this is the "
        "only “you all,” so this book leaves out Spain's "
        "<span class='es'>vosotros</span> entirely — one less form to learn.</p>"))

    b.append("<h3>The four questions to ask every new verb</h3>")
    b.append('<p>This is the checklist from your notes, and it\'s the whole game. When '
             'you meet any verb, run down this list:</p>')
    b.append('<ol class="steps">'
             '<li><b>Is it regular?</b> If yes, just add the normal endings. Done.</li>'
             '<li><b>Is only the <span class="es">yo</span> form irregular?</b> '
             '(hacer → <span class="es">hago</span>) The rest are normal.</li>'
             '<li><b>Does the stem change?</b> (querer → <span class="es">quiero</span>) '
             'These are the “boot” verbs.</li>'
             '<li><b>Is it completely irregular?</b> (ser, ir) A short list you memorize '
             'like song lyrics.</li></ol>')
    b.append(box("trick", "Why this saves you",
        "<p>Most verbs are regular or only-yo-irregular. The truly wild ones are a tiny "
        "club. Sort first, memorize second — you'll do a fraction of the work.</p>"))

    # ---------- Ch 2: Regular present ----------
    b.append(chapter(2, "Regular present tense", "Chapter 2 · The foundation"))
    b.append('<p>This is the ground everything else stands on. Take off the '
             '<span class="es">-ar / -er / -ir</span>, then add the endings for that '
             'family. Here are the three model verbs in full:</p>')
    for m in vb.REGULAR_MODELS:
        b.append(f'<h3>{esc(m["inf"])} <span class="muted" style="font-weight:400;'
                 f'font-size:16px">— {esc(m["en"])} ({esc(m["fam"])})</span></h3>')
        b.append(f'<p class="small">{esc(m["note"])}</p>')
        b.append(conj_table("", vb.conj(m["inf"], "present")))
        b.append(examples(m["examples"]))

    b.append("<h3>Just the endings (memorize this grid)</h3>")
    b.append('<div class="legend"><span><b>-ar</b> is the biggest family.</span>'
             '<span><b>-er</b> and <b>-ir</b> are twins except for the '
             '<span class="es">nosotros</span> form.</span></div>')
    b.append(grid_conj([("-ar", ["-o", "-as", "-a", "-amos", "-áis", "-an"]),
                        ("-er", ["-o", "-es", "-e", "-emos", "-éis", "-en"]),
                        ("-ir", ["-o", "-es", "-e", "-imos", "-ís", "-en"])]))
    b.append(box("tip", "Notice",
        "<p>The <span class='es'>yo</span> form is always <b>-o</b> for regular verbs "
        "(hablo, como, vivo). And -er/-ir differ in only two spots. Two families for "
        "the price of one.</p>"))
    b.append("<h3>Regular verbs from your life</h3>")
    b.append('<p>All of these follow the models above exactly — no surprises:</p>')
    b.append(chips([(inf, en) for inf, en, _ in vb.REGULAR_BANK]))

    # ---------- Ch 3: Pattern A ----------
    b.append(chapter(3, "Pattern A — only the “yo” form is irregular",
                     "Chapter 3 · The first irregular pattern"))
    b.append('<span class="pattern-badge">Pattern A · yo is the odd one</span>')
    b.append('<p>The friendliest irregulars: only the <span class="es">yo</span> form '
             'misbehaves. Every other form is perfectly regular. Two main flavors:</p>')
    b.append(box("trick", "The two flavors",
        "<p><b>“-go” verbs:</b> the yo form grows a <b>g</b> — "
        "hacer → <span class='es'>hago</span>, poner → <span class='es'>pongo</span>, "
        "salir → <span class='es'>salgo</span>.<br>"
        "<b>“-zco” verbs:</b> verbs ending in -cer/-cir → "
        "conocer → <span class='es'>conozco</span>.</p>"))
    for v in vb.YO_IRREGULAR:
        b.append(verb_block(v, show_examples=2))
    b.append(box("warn", "Watch out",
        "<p>Because only <span class='es'>yo</span> changes, the temptation is to change "
        "the others too. Don't — it's <span class='es'>hago</span> but "
        "<span class='es'>haces, hace, hacemos, hacen</span> (all regular).</p>"))

    # ---------- Ch 4: Pattern B ----------
    b.append(chapter(4, "Pattern B — stem-changing “boot” verbs",
                     "Chapter 4 · The boot"))
    b.append('<span class="pattern-badge">Pattern B · the stem changes</span>')
    b.append('<p>In these verbs the vowel inside the stem changes — but <b>only</b> in '
             'the forms that fall inside the “boot.” The '
             '<span class="es">nosotros</span> form sits outside the boot and stays '
             'flat. (Teachers call it the “boot” because with all six persons written '
             'out, the changed forms trace a boot shape.)</p>')
    b.append(box("trick", "The rule in one line",
        "<p>The stem changes everywhere <b>except</b> <span class='es'>nosotros</span>. "
        "So if you can conjugate <span class='es'>yo</span> and "
        "<span class='es'>nosotros</span>, you know the whole verb.</p>"))
    b.append("<h3>The boot, shaded (querer, e→ie)</h3>")
    b.append(grid_conj([("querer", vb.STEM_CHANGING["e→ie"][0]["forms"])], boot=True))
    b.append('<p class="small">Shaded = inside the boot (changes). '
             'Only <span class="es">queremos</span> stays regular.</p>')

    groups = [("e→ie", "e becomes ie", "The most common change."),
              ("o→ue", "o becomes ue", "The second most common."),
              ("e→i", "e becomes i", "Only in -ir verbs."),
              ("u→ue", "u becomes ue", "Basically just jugar.")]
    for key, label, note in groups:
        b.append(f'<h3>{esc(key)} &nbsp;<span class="muted" style="font-size:15px;'
                 f'font-weight:400">({esc(label)})</span></h3>')
        b.append(f'<p class="small">{esc(note)}</p>')
        verbs = vb.STEM_CHANGING[key]
        b.append(grid_conj([(v["inf"], v["forms"]) for v in verbs], boot=True))
        # one example line each
        ex = "".join(f'<li><span class="es">{esc(v["examples"][0][0])}</span>'
                     f'<span class="en">{esc(v["examples"][0][1])}</span></li>'
                     for v in verbs)
        b.append(f'<ul class="ex">{ex}</ul>')

    # ---------- Ch 5: Pattern C ----------
    b.append(chapter(5, "Pattern C — completely irregular",
                     "Chapter 5 · Memorize these like song lyrics"))
    b.append('<span class="pattern-badge">Pattern C · no pattern — just learn them</span>')
    b.append('<p>A tiny club of verbs that don\'t follow any rule. The good news: '
             'they\'re the most common verbs in the language, so you\'ll drill them '
             'constantly and they\'ll stick fast. Say each one as a little chant.</p>')
    b.append(grid_conj([(v["inf"], v["forms"]) for v in vb.FULLY_IRREGULAR]))
    for v in vb.FULLY_IRREGULAR:
        b.append(verb_block(v, show_examples=2))

    # ---------- Ch 6: Pattern D + attack plan ----------
    b.append(chapter(6, "Pattern D — combination verbs",
                     "Chapter 6 · Two twists at once"))
    b.append('<span class="pattern-badge">Pattern D · irregular yo + stem change</span>')
    b.append('<p>These do <b>both</b> tricks at once: an irregular '
             '<span class="es">yo</span> form <i>and</i> a stem change in the boot. '
             'They\'re worth special attention because they\'re everyday verbs.</p>')
    b.append(grid_conj([(v["inf"], v["forms"]) for v in vb.COMBINATION]))
    for v in vb.COMBINATION:
        b.append(verb_block(v, show_examples=2))
    b.append(box("tip", "Attack plan for ANY new verb",
        "<p>1) Try the regular endings. 2) Fix the <span class='es'>yo</span> form if "
        "it's a -go/-zco verb. 3) Check for a boot stem change. 4) If it's ser/estar/"
        "ir/haber, you already know it. That's it — four moves cover almost everything."
        "</p>"))

    # ---------- Ch 7: Ser vs Estar ----------
    b.append(chapter(7, "Ser vs. Estar — two ways to “be”",
                     "Chapter 7 · The famous pair"))
    b.append('<p>Spanish has two verbs for “to be,” and choosing between them '
             'is one of the biggest early wins. The short version:</p>')
    b.append(box("trick", "The one-line rule",
        "<p><b>SER</b> = the <i>essence</i> — what something fundamentally <i>is</i>. "
        "<b>ESTAR</b> = the <i>state</i> — how/where something <i>is right now</i>.</p>"))
    b.append('<div class="grid" style="grid-template-columns:1fr;gap:12px">')
    b.append(two_col_uses("SER — identity & essence", "sea", vb.SER_USES))
    b.append(two_col_uses("ESTAR — state, place & feeling", "cuba", vb.ESTAR_USES))
    b.append("</div>")
    b.append("<h3>Same word, different verb, different meaning</h3>")
    b.append('<table class="grid-conj"><thead><tr><th>With SER</th><th></th>'
             '<th>With ESTAR</th><th></th></tr></thead><tbody>')
    for s_es, s_en, e_es, e_en in vb.SER_ESTAR_CONTRAST:
        b.append(f'<tr><td class="v">{esc(s_es)}</td><td class="en">{esc(s_en)}</td>'
                 f'<td class="v">{esc(e_es)}</td><td class="en">{esc(e_en)}</td></tr>')
    b.append("</tbody></table>")
    b.append(box("tip", "A memory trick — “How you feel and where you are, always use ESTAR.”",
        "<p>Feelings and location = estar. Almost everything permanent = ser.</p>"))

    # ---------- Ch 8: Reflexive ----------
    b.append(chapter(8, "Reflexive verbs — your daily routine",
                     "Chapter 8 · Doing things to yourself"))
    b.append('<p>Reflexive verbs describe actions you do <i>to yourself</i> — wake up, '
             'get up, shower, get dressed. You spot them by the <span class="es">-se</span> '
             'stuck on the infinitive: <span class="es">levantarse</span>. To use one, '
             'you move that little pronoun to the front and conjugate normally.</p>')
    b.append(box("tip", "The reflexive pronouns",
        "<p><b>me</b> (myself) · <b>te</b> (yourself) · <b>se</b> (him/herself) · "
        "<b>nos</b> (ourselves) · <b>se</b> (themselves / yourselves)</p>"
        "<p>So <span class='es'>levantarse</span> → <span class='es'>me levanto</span> "
        "= “I get (myself) up.”</p>"))
    for inf, en, forms, es, eng in vb.REFLEXIVE:
        b.append(f'<h4 style="margin-top:18px">{esc(inf)} <span class="muted" '
                 f'style="font-weight:400">— {esc(en)}</span></h4>')
        b.append(conj_table("", [(vb.PRONOUNS[i], forms[i]) for i in vb.SHOW]))
        b.append(f'<ul class="ex"><li><span class="es">{esc(es)}</span>'
                 f'<span class="en">{esc(eng)}</span></li></ul>')
    b.append(box("cuba", "Put your morning in Spanish",
        "<p>Try narrating your real morning: <span class='es'>Me despierto, me levanto, "
        "me ducho, me visto, y salgo a la playa.</span> That one sentence uses five "
        "verbs correctly.</p>"))

    # ---------- Ch 9: Gustar ----------
    b.append(chapter(9, "Gustar & friends — “backwards” verbs",
                     "Chapter 9 · Likes, loves, and aches"))
    b.append('<p>Here\'s the surprise: <span class="es">gustar</span> doesn\'t really '
             'mean “to like.” It means “to be pleasing.” So '
             '<span class="es">me gusta el café</span> literally says '
             '“coffee is pleasing <b>to me</b>.” The thing you like is the '
             'subject — so the verb agrees with <i>it</i>, not with you.</p>')
    b.append(box("trick", "The two shapes you need",
        "<p><b>me gusta</b> + one thing / an action → "
        "<span class='es'>Me gusta la playa. Me gusta nadar.</span><br>"
        "<b>me gustan</b> + plural things → "
        "<span class='es'>Me gustan los perros.</span></p>"))
    b.append("<h3>The pronouns that go in front</h3>")
    b.append(conj_table("", [(p, en) for p, en in vb.GUSTAR_PRON]))
    b.append("<h3>The whole family works the same way</h3>")
    for inf, en, es, eng in vb.GUSTAR_LIKE:
        b.append(f'<p style="margin:10px 0"><b>{esc(inf)}</b> '
                 f'<span class="muted">— {esc(en)}</span><br>'
                 f'<span class="es">{esc(es)}</span> '
                 f'<span class="en">— {esc(eng)}</span></p>')

    # ---------- Ch 10: Present progressive ----------
    b.append(chapter(10, "Right now — the present progressive",
                     "Chapter 10 · -ando / -iendo"))
    b.append('<p>To stress that something is happening <i>at this very moment</i>, use '
             '<span class="es">estar</span> + the <b>-ando/-iendo</b> form (English '
             '“-ing”). You already know <span class="es">estar</span> from '
             'Chapter 7 — now just bolt on the gerund.</p>')
    b.append(box("tip", "Build it in two steps",
        "<p>1) Conjugate <span class='es'>estar</span> (estoy, estás, está…). "
        "2) Add the gerund: <span class='es'>-ar → -ando</span>, "
        "<span class='es'>-er/-ir → -iendo</span>.<br>"
        "<span class='es'>Estoy + nadando = Estoy nadando</span> — “I am "
        "swimming.”</p>"))
    b.append("<h3>Forming the gerund</h3>")
    b.append('<table class="grid-conj"><thead><tr><th>Verb</th><th>Gerund</th>'
             '<th>Rule</th></tr></thead><tbody>')
    for inf, ger, rule in vb.GERUNDS:
        b.append(f'<tr><td>{esc(inf)}</td><td class="v">{esc(ger)}</td>'
                 f'<td class="en">{esc(rule)}</td></tr>')
    b.append("</tbody></table>")
    b.append(examples(vb.PROG_EXAMPLES))
    b.append(box("warn", "Don't overuse it",
        "<p>Unlike English, Spanish uses the plain present for habits and near-future "
        "plans. “I'm working tomorrow” is <span class='es'>Trabajo mañana</span>, "
        "not the progressive. Save <span class='es'>estoy -ando</span> for "
        "“right this second.”</p>"))

    # ---------- Ch 11: Past ----------
    b.append(chapter(11, "Stepping into the past", "Chapter 11 · Your first past tense"))
    b.append('<p>Big moment: your first tense beyond the present. Spanish has two '
             'everyday past tenses, and the trick is knowing which job each one does.</p>')
    b.append(box("trick", "Two pasts, two jobs",
        "<p><b>Preterite</b> = a <i>snapshot</i>. One finished action, done and over. "
        "“I swam.”<br>"
        "<b>Imperfect</b> = a <i>video / background</i>. What used to happen, or what was "
        "going on. “I used to swim / I was swimming.”</p>"))

    b.append('<h2><span class="tense-tag tt-past">Past</span>The preterite '
             '(finished actions)</h2>')
    b.append('<p>Regular verbs — take off the ending and add:</p>')
    b.append(grid_conj([(inf, forms) for inf, fam, forms in vb.PRET_REGULAR_MODELS]))
    b.append(box("tip", "Notice the accents",
        "<p>The <span class='es'>yo</span> and <span class='es'>él</span> forms carry a "
        "stressed accent: <span class='es'>hablé, habló</span>. And -er/-ir share the "
        "exact same endings here — one set to learn, not two.</p>"))
    b.append("<h3>The preterite irregulars you'll meet first</h3>")
    b.append('<p>A handful are irregular but incredibly common. Note that '
             '<b>ser</b> and <b>ir</b> are <i>identical</i> in the preterite — context '
             'tells you which:</p>')
    b.append(grid_conj([(name, forms) for name, en, forms in vb.PRET_IRREGULAR]))
    b.append(examples(vb.PRET_EXAMPLES))

    b.append('<h2><span class="tense-tag tt-past">Past</span>The imperfect '
             '(background & habits)</h2>')
    b.append('<p>This is the “used to / was ___-ing” past. It\'s beautifully '
             'regular — and it has only <b>three</b> irregular verbs in the whole '
             'language.</p>')
    b.append(grid_conj([(inf, forms) for inf, fam, forms in vb.IMPERF_REGULAR_MODELS]))
    b.append(box("tip", "The only three irregulars: ser, ir, ver",
        "<p>That's the entire list. Master these three and the imperfect is done.</p>"))
    b.append(grid_conj([(name, forms) for name, en, forms in vb.IMPERF_IRREGULAR]))
    b.append(examples(vb.IMPERF_EXAMPLES))

    b.append("<h3>Which past do I use? A decision guide</h3>")
    b.append('<table class="grid-conj"><thead><tr><th>If you mean…</th><th>Use</th>'
             '<th>Example</th></tr></thead><tbody>')
    for meaning, tense, es, en in vb.PRET_VS_IMPERF:
        tag = "tt-past"
        b.append(f'<tr><td>{esc(meaning)}</td>'
                 f'<td><span class="tense-tag {tag}">{esc(tense)}</span></td>'
                 f'<td><span class="es">{esc(es)}</span><br>'
                 f'<span class="en">{esc(en)}</span></td></tr>')
    b.append("</tbody></table>")
    b.append(box("cuba", "The classic combo",
        "<p>They often appear together: the imperfect sets the scene, the preterite "
        "drops the event in. <span class='es'>Yo cocinaba (background) cuando mi novio "
        "llegó (event).</span> — “I was cooking when my boyfriend arrived.”</p>"))

    # ---------- Ch 12: Future ----------
    b.append(chapter(12, "Stepping into the future", "Chapter 12 · Two ways to say tomorrow"))
    b.append('<p>Two ways forward, and the first one is the easiest tense in the whole '
             'book — you already know it.</p>')
    b.append('<h2><span class="tense-tag tt-fut">Future</span>The easy way: '
             'ir a + infinitive</h2>')
    b.append(box("trick", "You already have this",
        "<p>Conjugate <span class='es'>ir</span> (voy, vas, va, vamos, van), add "
        "<span class='es'>a</span>, then drop in <b>any infinitive</b> — no new "
        "endings to learn.<br>"
        "<span class='es'>Voy a nadar</span> = “I'm going to swim.”</p>"))
    b.append(examples(vb.IR_A_EXAMPLES))
    b.append(box("tip", "This is how people actually talk",
        "<p>In everyday Cuban and Latin-American speech, <span class='es'>ir a + "
        "infinitivo</span> is the go-to future. If you only learn one, learn this.</p>"))

    b.append('<h2><span class="tense-tag tt-fut">Future</span>The future tense '
             '(will …)</h2>')
    b.append('<p>The neat one: you don\'t chop the infinitive — you add endings to the '
             '<b>whole thing</b>. The same endings for -ar, -er, and -ir:</p>')
    _fe = ["-é", "-ás", "-á", "-emos", "-éis", "-án"]
    b.append(endings_table("Future endings (added to the infinitive)",
        [(vb.PRON_SHORT[i], _fe[i]) for i in vb.SHOW]))
    b.append(grid_conj([(inf, forms) for inf, forms in vb.FUT_REGULAR_MODEL]))
    b.append("<h3>Irregular futures — same endings, changed stem</h3>")
    b.append('<p>A short list changes the stem but keeps the identical endings:</p>')
    b.append('<table class="grid-conj"><thead><tr><th>Verb</th><th>Future stem</th>'
             '<th>yo form</th></tr></thead><tbody>')
    for inf, st, yo in vb.FUT_IRREGULAR_STEMS:
        b.append(f'<tr><td>{esc(inf)}</td><td class="v">{esc(st)}</td>'
                 f'<td class="en">{esc(yo)}</td></tr>')
    b.append("</tbody></table>")
    b.append(examples(vb.FUT_EXAMPLES))

    # ---------- Ch 13: Timeline ----------
    b.append(chapter(13, "One verb, three times", "Chapter 13 · Putting it together"))
    b.append('<p>Here\'s the payoff. The same verb, walked across time. Read each row '
             'left to right and feel the shape of past → present → future.</p>')
    for inf, p_es, p_en, n_es, n_en, f_es, f_en in vb.TIMELINE:
        b.append(f'<div class="timeline"><table class="grid-conj"><thead><tr>'
                 f'<th colspan="3">{esc(inf)}</th></tr></thead><tbody>'
                 f'<tr><td><span class="tense-tag tt-past">Past</span></td>'
                 f'<td class="v">{esc(p_es)}</td><td class="en">{esc(p_en)}</td></tr>'
                 f'<tr><td><span class="tense-tag tt-pres">Now</span></td>'
                 f'<td class="v">{esc(n_es)}</td><td class="en">{esc(n_en)}</td></tr>'
                 f'<tr><td><span class="tense-tag tt-fut">Future</span></td>'
                 f'<td class="v">{esc(f_es)}</td><td class="en">{esc(f_en)}</td></tr>'
                 f'</tbody></table></div>')
    b.append(box("tip", "Your practice habit from here",
        "<p>Pick any verb you know and say it three ways out loud: what you did "
        "yesterday, what you do today, what you'll do tomorrow. Do it with five verbs "
        "and you're conjugating across all three tenses.</p>"))
    b.append('<p class="center muted" style="margin-top:30px">Now open the '
             '<a href="practice.html">Practice</a> book — that\'s where verbs move from '
             'your eyes into your mouth. ¡Vamos! 🌊</p>')

    w("book.html", shell_v("The Verb Book · Learn", "".join(b), subtitle="Learn"))


# ══════════════════════════════════════════════════════════════════════════
#  EXERCISE DATA  (shared by Practice + Answers so they stay in sync)
# ══════════════════════════════════════════════════════════════════════════
# Each section: (title, intro, list of exercise-groups)
# An exercise-group: ("kind", instruction, items)
#   kind "fill"      → items are (prompt_with____, answer, why)
#   kind "conjugate" → items are (verb, pronoun, answer, why)   (rendered as prompt)
#   kind "translate" → items are (english, spanish)
#   kind "choose"    → items are (prompt, options, answer, why)
#   kind "write"     → items are prompts (free writing; no single answer)

def _P(*a):  # pack helper
    return a


PRACTICE = [
 ("Set 1 · Regular present tense", "Warm up on the three families. Fill each blank with the correct present-tense form.", [
   ("fill", "Fill in the present tense.", [
     ("Yo ___ español todos los días. (hablar)", "hablo", "Regular -ar, yo ending -o."),
     ("Nosotros ___ en la playa. (nadar)", "nadamos", "Regular -ar, nosotros ending -amos."),
     ("Ella ___ fruta antes del gimnasio. (comer)", "come", "Regular -er, él/ella ending -e."),
     ("¿Tú ___ cerca del mar? (vivir)", "vives", "Regular -ir, tú ending -es."),
     ("Ellos ___ música cubana. (escuchar)", "escuchan", "Regular -ar, ellos ending -an."),
     ("Yo ___ un libro en español. (leer)", "leo", "Regular -er, yo ending -o."),
     ("Nosotros ___ cartas cuando llueve. (escribir)", "escribimos", "Regular -ir, nosotros ending -imos."),
     ("El perro ___ mucho. (correr)", "corre", "Regular -er, él ending -e."),
   ]),
   ("translate", "Translate to Spanish (present tense).", [
     ("I cook dinner every night.", "Cocino la cena todas las noches."),
     ("We swim in the sea.", "Nadamos en el mar."),
     ("She drinks Cuban coffee.", "Ella bebe café cubano."),
     ("They live in Florida.", "Ellos viven en Florida."),
   ]),
 ]),
 ("Set 2 · Identify the pattern", "For each verb, name its irregular pattern (like your original quiz).", [
   ("choose", "Choose: A) Regular · B) Yo-form irregular · C) Stem-changing · D) Completely irregular · E) Combination.", [
     ("hablar", "A B C D E", "A", "Fully regular -ar verb."),
     ("hacer", "A B C D E", "B", "Only the yo form (hago) is irregular."),
     ("querer", "A B C D E", "C", "Stem changes e→ie (quiero)."),
     ("ser", "A B C D E", "D", "Completely irregular (soy, eres, es…)."),
     ("tener", "A B C D E", "E", "Combination: irregular yo (tengo) + e→ie stem change."),
     ("poder", "A B C D E", "C", "Stem changes o→ue (puedo)."),
     ("conocer", "A B C D E", "B", "Only the yo form (conozco) is irregular."),
     ("ir", "A B C D E", "D", "Completely irregular (voy, vas, va…)."),
     ("venir", "A B C D E", "E", "Combination: irregular yo (vengo) + e→ie (vienes)."),
     ("comer", "A B C D E", "A", "Fully regular -er verb."),
   ]),
 ]),
 ("Set 3 · Yo-form & stem-changing verbs", "Conjugate carefully — these are the patterns that trip people up.", [
   ("fill", "Fill in the present tense.", [
     ("Yo ___ ejercicio en la playa. (hacer)", "hago", "Only yo is irregular: hago."),
     ("Yo ___ música cuando cocino. (poner)", "pongo", "Yo-go verb: pongo."),
     ("Yo ___ a un café increíble. (conocer)", "conozco", "-cer verb → conozco."),
     ("Yo ___ nadar muy bien. (saber)", "sé", "Irregular yo: sé (with accent)."),
     ("Yo ___ delfines desde la tabla. (ver)", "veo", "Yo form veo."),
     ("¿Tú ___ ir a la playa? (querer)", "quieres", "e→ie in the boot: quieres."),
     ("Ella ___ hasta las nueve. (dormir)", "duerme", "o→ue in the boot: duerme."),
     ("Yo ___ un café con leche. (pedir)", "pido", "e→i: pido."),
     ("Nosotros ___ a las siete. (empezar)", "empezamos", "nosotros is OUTSIDE the boot — no change."),
     ("Yo ___ con el perro en el jardín. (jugar)", "juego", "u→ue: juego."),
   ]),
 ]),
 ("Set 4 · Completely irregular & combination", "The heavy hitters. Fill in the present tense.", [
   ("fill", "Fill in the present tense.", [
     ("Yo ___ de Florida. (ser)", "soy", "ser: soy."),
     ("Mi novio ___ cubano. (ser)", "es", "ser: es."),
     ("Yo ___ en la playa ahora. (estar)", "estoy", "estar: estoy."),
     ("¿Cómo ___ tú? (estar)", "estás", "estar: estás (accent)."),
     ("Nosotros ___ a bailar salsa. (ir)", "vamos", "ir: vamos."),
     ("Yo ___ un perro cariñoso. (tener)", "tengo", "combo: irregular yo tengo."),
     ("¿Cuántos años ___ tú? (tener)", "tienes", "combo: e→ie → tienes."),
     ("Yo ___ de la playa. (venir)", "vengo", "combo: irregular yo vengo."),
     ("Ella ___ la verdad. (decir)", "dice", "combo: e→i → dice."),
     ("___ mucha gente en la playa. (haber → hay)", "Hay", "haber's special form: hay = there is/are."),
   ]),
 ]),
 ("Set 5 · Ser vs. Estar", "Choose the right “to be.” Then write the correct form.", [
   ("choose", "Choose SER or ESTAR and give the form.", [
     ("Yo ___ de los Estados Unidos.", "ser / estar", "soy", "Origin → ser."),
     ("El café ___ caliente.", "ser / estar", "está", "Temporary state → estar."),
     ("Mi novio ___ simpático.", "ser / estar", "es", "Permanent trait → ser."),
     ("Nosotros ___ en el gimnasio.", "ser / estar", "estamos", "Location → estar."),
     ("___ las ocho de la mañana.", "ser / estar", "Son", "Time → ser."),
     ("Yo ___ cansada después de correr.", "ser / estar", "estoy", "Feeling → estar."),
     ("La tabla ___ de fibra de vidrio.", "ser / estar", "es", "Material → ser."),
     ("El agua ___ fría hoy.", "ser / estar", "está", "Temporary condition → estar."),
   ]),
 ]),
 ("Set 6 · Reflexives & gustar", "Everyday life. Fill in the correct form.", [
   ("fill", "Reflexive verbs — fill in the pronoun + verb.", [
     ("Yo ___ a las seis. (despertarse)", "me despierto", "me + despierto (e→ie)."),
     ("Yo ___ después de la playa. (ducharse)", "me ducho", "me + ducho."),
     ("¿A qué hora ___ tú? (acostarse)", "te acuestas", "te + acuestas (o→ue)."),
     ("Nosotros ___ temprano. (levantarse)", "nos levantamos", "nos + levantamos."),
   ]),
   ("fill", "Gustar & friends — gusta or gustan? (plus the pronoun)", [
     ("A mí ___ la playa. (gustar)", "me gusta", "One thing → gusta."),
     ("A mí ___ los perros. (gustar)", "me gustan", "Plural → gustan."),
     ("A ti ___ el café cubano. (encantar)", "te encanta", "One thing → encanta."),
     ("A mí ___ los pies después de correr. (doler)", "me duelen", "Plural (feet) → duelen."),
   ]),
 ]),
 ("Set 7 · Right now (present progressive)", "Rewrite as “right now” using estar + gerund.", [
   ("fill", "Fill with estar + the -ando/-iendo form.", [
     ("Yo ___ en el mar. (nadar)", "estoy nadando", "estoy + nadando."),
     ("Ella ___ arroz. (cocinar)", "está cocinando", "está + cocinando."),
     ("Nosotros ___ música. (escuchar)", "estamos escuchando", "estamos + escuchando."),
     ("El perro ___ en el sofá. (dormir)", "está durmiendo", "-ir stem change o→u: durmiendo."),
     ("Yo ___ un libro. (leer)", "estoy leyendo", "vowel+iendo → leyendo."),
   ]),
 ]),
 ("Set 8 · Into the past (preterite)", "Finished actions. Fill in the preterite.", [
   ("fill", "Fill in the preterite (completed past).", [
     ("Ayer yo ___ una hora. (nadar)", "nadé", "Regular -ar preterite yo: -é."),
     ("Anoche yo ___ arroz con pollo. (cocinar)", "cociné", "Regular -ar preterite yo: -é."),
     ("Ella ___ café esta mañana. (hacer → irregular)", "hizo", "Irregular: hizo (note the z)."),
     ("Nosotros ___ un día perfecto. (tener → irregular)", "tuvimos", "Irregular stem tuv-: tuvimos."),
     ("Yo ___ a la playa el sábado. (ir → irregular)", "fui", "ir/ser preterite: fui."),
     ("¿Tú ___ en la fiesta anoche? (estar → irregular)", "estuviste", "Irregular stem estuv-."),
     ("Ellos ___ la verdad. (decir → irregular)", "dijeron", "Irregular stem dij- → dijeron."),
     ("Yo ___ un beso a mi novio. (dar → irregular)", "di", "Irregular: di."),
   ]),
 ]),
 ("Set 9 · Into the past (imperfect)", "Background & habits. Fill in the imperfect.", [
   ("fill", "Fill in the imperfect (used to / was ___-ing).", [
     ("De niña, yo ___ cerca del mar. (vivir)", "vivía", "Regular -ir imperfect: -ía."),
     ("Todos los veranos nosotros ___ a la playa. (ir → irregular)", "íbamos", "Irregular imperfect: íbamos."),
     ("Mi abuela ___ comida cubana. (cocinar)", "cocinaba", "Regular -ar imperfect: -aba."),
     ("Antes yo no ___ nada de español. (hablar)", "hablaba", "Regular -ar imperfect: -aba."),
     ("El cielo ___ gris. (estar)", "estaba", "Regular imperfect: estaba."),
     ("Cuando ___ niña, me gustaba nadar. (ser → irregular)", "era", "Irregular imperfect: era."),
   ]),
   ("choose", "Preterite or imperfect? Choose the tense that fits.", [
     ("Ayer ___ a la playa. (ir)", "fui / iba", "fui", "Single finished action → preterite."),
     ("De niña ___ todos los días. (nadar)", "nadé / nadaba", "nadaba", "Habit in the past → imperfect."),
     ("___ las ocho y hacía calor. (ser)", "Fue / Era", "Era", "Time/background → imperfect."),
     ("Yo cocinaba cuando él ___. (llegar)", "llegó / llegaba", "llegó", "The interrupting event → preterite."),
   ]),
 ]),
 ("Set 10 · Into the future", "Both futures. Fill in the form asked for.", [
   ("fill", "Near future — ir a + infinitive.", [
     ("Esta tarde yo ___ nadar. (ir a)", "voy a", "voy + a + infinitive."),
     ("¿Tú ___ venir a la playa? (ir a)", "vas a", "vas + a."),
     ("Nosotros ___ cocinar juntos. (ir a)", "vamos a", "vamos + a."),
   ]),
   ("fill", "Future tense — add the endings to the infinitive (watch irregular stems).", [
     ("Algún día yo ___ español con fluidez. (hablar)", "hablaré", "Regular: infinitive + é."),
     ("El año que viene yo ___ a Cuba. (ir)", "iré", "Regular future: iré."),
     ("Nosotros ___ una casa cerca del mar. (tener → irregular)", "tendremos", "Irregular stem tendr-."),
     ("¿Qué ___ tú este verano? (hacer → irregular)", "harás", "Irregular stem har-."),
     ("Mañana ___ sol. (hacer → irregular)", "hará", "Irregular stem har-: hará."),
   ]),
 ]),
 ("Set 11 · One verb across time", "Conjugate the same verb in all three tenses (yo form).", [
   ("fill", "Give the yo form: past (preterite) / present / future.", [
     ("nadar — ayer, hoy, mañana", "nadé / nado / nadaré", "Preterite nadé, present nado, future nadaré."),
     ("comer — anoche, ahora, luego", "comí / como / comeré", "Preterite comí, present como, future comeré."),
     ("hacer — ayer, hoy, mañana", "hice / hago / haré", "Irregular in all three: hice / hago / haré."),
     ("ir — ayer, hoy, mañana", "fui / voy / iré", "Preterite fui, present voy, future iré."),
   ]),
 ]),
 ("Set 12 · Free writing", "No single right answer — write real sentences about your life. Say them out loud too.", [
   ("write", "Write full sentences.", [
     "Describe your morning routine using 5 reflexive verbs (me despierto…).",
     "Write 3 things you like and 1 thing you love using gusta/gustan/encanta.",
     "Write what you did yesterday in 3 preterite sentences.",
     "Write what you used to do as a child in 2 imperfect sentences.",
     "Write 3 plans for tomorrow using voy a + infinitive.",
     "Write one long sentence that uses ser AND estar correctly.",
   ]),
 ]),
]


# ── practice / answer renderers ─────────────────────────────────────────────
def _render_group(g, mode):
    """mode: 'practice' or 'answers'. Returns HTML for one exercise group."""
    kind, instr, items = g
    h = [f'<p class="small" style="margin-top:10px"><b>{esc(instr)}</b></p>']
    if kind == "fill":
        rows = []
        for i, it in enumerate(items, 1):
            prompt, ans, why = it
            if mode == "practice":
                shown = esc(prompt).replace("___", blank(90))
                rows.append(f'<div class="q"><span class="num">{i}.</span>{shown}</div>')
            else:
                shown = esc(prompt).replace("___", f'<span class="es">{esc(ans)}</span>')
                rows.append(f'<div class="q"><span class="num">{i}.</span>{shown}'
                            f'<div class="small" style="margin-left:4px">↳ {esc(why)}</div></div>')
        h.append("".join(rows))
    elif kind == "translate":
        rows = []
        for i, (en, es) in enumerate(items, 1):
            if mode == "practice":
                rows.append(f'<div class="q"><span class="num">{i}.</span>{esc(en)}'
                            f'{write_lines(1)}</div>')
            else:
                rows.append(f'<div class="q"><span class="num">{i}.</span>'
                            f'<span class="en">{esc(en)}</span><br>'
                            f'<span class="es">{esc(es)}</span></div>')
        h.append("".join(rows))
    elif kind == "choose":
        rows = []
        for i, it in enumerate(items, 1):
            prompt, opts, ans, why = it
            if mode == "practice":
                rows.append(f'<div class="q"><span class="num">{i}.</span>{esc(prompt)}'
                            f' &nbsp;<span class="small">[{esc(opts)}]</span> '
                            f'{blank(70)}</div>')
            else:
                rows.append(f'<div class="q"><span class="num">{i}.</span>{esc(prompt)} '
                            f'&nbsp;→ <span class="es">{esc(ans)}</span>'
                            f'<div class="small" style="margin-left:4px">↳ {esc(why)}</div></div>')
        h.append("".join(rows))
    elif kind == "write":
        if mode == "practice":
            rows = []
            for i, prompt in enumerate(items, 1):
                rows.append(f'<div class="q"><span class="num">{i}.</span>{esc(prompt)}'
                            f'{write_lines(2)}</div>')
            h.append("".join(rows))
        else:
            h.append('<p class="small">Free writing — no answer key. Check that every '
                     'verb agrees with its subject and sits in the right tense. Read each '
                     'sentence aloud.</p>')
    return "".join(h)


def build_practice():
    b = [eyebrow("Practice workbook"),
         "<h1>Practice</h1>",
         '<p class="muted">Write directly in here — by hand is best. Each set matches '
         'a chapter in <a href="book.html">Learn</a>. Check yourself in '
         '<a href="answers.html">Answers</a> when you finish a set.</p>']
    for n, (title, intro, groups) in enumerate(PRACTICE, 1):
        if n > 1:
            b.append('<div class="page-break"></div>')
        b.append(f'<h2>{esc(title)}</h2>')
        b.append(f'<p class="muted">{esc(intro)}</p>')
        inner = "".join(_render_group(g, "practice") for g in groups)
        b.append(drill("Exercises", inner))
    w("practice.html", shell_v("The Verb Book · Practice", "".join(b), subtitle="Practice"))


def build_answers():
    b = [eyebrow("Answer key"),
         "<h1>Answers</h1>",
         '<p class="muted">Every answer, with a one-line <em>why</em>. Don\'t just check '
         'the letter — read the reason, because the reason is the learning.</p>']
    for n, (title, intro, groups) in enumerate(PRACTICE, 1):
        if n > 1:
            b.append('<div class="page-break"></div>')
        b.append(f'<h2>{esc(title)}</h2>')
        inner = "".join(_render_group(g, "answers") for g in groups)
        b.append(drill("Worked answers", inner))
    w("answers.html", shell_v("The Verb Book · Answers", "".join(b), subtitle="Answers"))


# ══════════════════════════════════════════════════════════════════════════
#  PAGE — QUIZZES  (expanded from the original PDF quiz)
# ══════════════════════════════════════════════════════════════════════════
QUIZZES = [
 ("Quiz 1 · Identify the pattern", "Choose the category for each verb. "
  "A) Regular · B) Yo-form irregular · C) Stem-changing · D) Completely irregular · "
  "E) Combination (yo + stem).", [
    ("hablar", "A"), ("hacer", "B"), ("querer", "C"), ("ser", "D"), ("tener", "E"),
    ("comer", "A"), ("venir", "E"), ("ir", "D"), ("poner", "B"), ("poder", "C"),
    ("conocer", "B"), ("dormir", "C"), ("estar", "D"), ("decir", "E"), ("vivir", "A"),
 ]),
 ("Quiz 2 · Present tense fill-in", "Write the correct present-tense form.", [
    ("Yo ___ (hacer)", "hago"), ("Nosotros ___ (querer)", "queremos"),
    ("Tú ___ (tener)", "tienes"), ("Ellos ___ (ir)", "van"),
    ("Yo ___ (poner)", "pongo"), ("Nosotros ___ (venir)", "venimos"),
    ("Él ___ (ser)", "es"), ("Yo ___ (poder)", "puedo"),
    ("Nosotros ___ (poder)", "podemos"), ("Tú ___ (hacer)", "haces"),
    ("Yo ___ (conocer)", "conozco"), ("Ella ___ (dormir)", "duerme"),
    ("Yo ___ (saber)", "sé"), ("Nosotros ___ (empezar)", "empezamos"),
    ("Yo ___ (dar)", "doy"),
 ]),
 ("Quiz 3 · Ser vs. Estar", "Write the correct form of ser or estar.", [
    ("Yo ___ de Florida.", "soy"), ("El café ___ caliente.", "está"),
    ("Nosotros ___ en la playa.", "estamos"), ("Mi novio ___ cubano.", "es"),
    ("___ las tres de la tarde.", "Son"), ("Ella ___ cansada hoy.", "está"),
    ("Las plantas ___ tropicales.", "son"), ("¿Cómo ___ tú?", "estás"),
 ]),
 ("Quiz 4 · The past", "Write the form in the tense named in parentheses.", [
    ("Ayer yo ___ a la playa. (ir — preterite)", "fui"),
    ("Anoche yo ___ arroz. (cocinar — preterite)", "cociné"),
    ("Ella ___ café. (hacer — preterite)", "hizo"),
    ("Nosotros ___ un buen día. (tener — preterite)", "tuvimos"),
    ("De niña yo ___ cerca del mar. (vivir — imperfect)", "vivía"),
    ("Nosotros ___ a la playa cada verano. (ir — imperfect)", "íbamos"),
    ("Mi abuela ___ comida cubana. (cocinar — imperfect)", "cocinaba"),
    ("Cuando ___ niña… (ser — imperfect)", "era"),
 ]),
 ("Quiz 5 · The future", "Write the form in the tense named in parentheses.", [
    ("Esta tarde yo ___ nadar. (ir a)", "voy a"),
    ("Nosotros ___ cocinar. (ir a)", "vamos a"),
    ("Algún día yo ___ español bien. (hablar — future)", "hablaré"),
    ("El año que viene yo ___ a Cuba. (ir — future)", "iré"),
    ("Nosotros ___ una casa. (tener — future)", "tendremos"),
    ("¿Qué ___ tú mañana? (hacer — future)", "harás"),
 ]),
]

QUIZ_EXPLAIN = [
    ("Quiero", "Stem-changing e→ie (querer). The stem 'quer' becomes 'quier' inside the boot."),
    ("Somos", "Completely irregular (ser). It has no pattern — memorized: soy, eres, es, somos, son."),
    ("Traigo", "Yo-form irregular (traer). Only the yo form adds -igo; the rest are regular."),
    ("Podemos", "The stem does NOT change because nosotros sits OUTSIDE the boot — so o→ue doesn't apply."),
    ("Vienes", "Combination verb (venir): the boot gives e→ie (vienes); the yo form is separately irregular (vengo)."),
    ("Hago", "Yo-form irregular (hacer): the yo form grows a g. The other forms (haces, hace…) are regular."),
]


def build_quizzes():
    b = [eyebrow("Quizzes"),
         "<h1>Quizzes</h1>",
         '<p class="muted">Five quizzes and a cumulative final, in the same style as your '
         'original — but bigger, and reaching into the past and future. Cover the answer '
         'key at the bottom until you\'re done.</p>',
         box("tip", "How to score yourself",
             "<p>Do a quiz in one sitting without notes. Then check the key. Anything you "
             "miss, go re-read that chapter's section and redo the matching Practice set. "
             "Aim to retake each quiz until you get it clean.</p>")]

    letters = "abcdefghijklmnopqrstuvwxyz"
    key_blocks = []  # collect answers for the key section

    for qi, (title, instr, items) in enumerate(QUIZZES, 1):
        b.append('<div class="page-break"></div>')
        b.append(f'<h2>{esc(title)}</h2>')
        b.append(f'<p class="muted">{esc(instr)}</p>')
        rows = []
        ans = []
        for i, (prompt, a) in enumerate(items, 1):
            rows.append(f'<div class="q"><span class="num">{i}.</span>{esc(prompt)} '
                        f'{blank(80)}</div>')
            ans.append(f"{i}. {a}")
        b.append(drill("Questions", "".join(rows)))
        key_blocks.append((title, ans))

    # Part 3 style — explain the pattern (from the PDF)
    b.append('<div class="page-break"></div>')
    b.append("<h2>Quiz 6 · Explain the pattern</h2>")
    b.append('<p class="muted">In your own words, say <em>why</em> each form looks the way '
             'it does. (Model explanations are in the key.)</p>')
    exp_rows = []
    for i, (form, _why) in enumerate(QUIZ_EXPLAIN, 1):
        exp_rows.append(f'<div class="q"><span class="num">{i}.</span>'
                        f'<span class="es">{esc(form)}:</span>{write_lines(1)}</div>')
    b.append(drill("Explain", "".join(exp_rows)))

    # Bonus challenge (from the PDF) — expanded to all three tenses
    b.append('<div class="page-break"></div>')
    b.append("<h2>Bonus Challenge</h2>")
    b.append('<p class="muted">Without looking anything up, conjugate <b>TENER</b> in the '
             'present tense — then push yourself into the past and future.</p>')
    bonus = []
    for pro in ["Yo", "Tú", "Él / Ella", "Nosotros", "Ellos / Ellas"]:
        bonus.append(f'<div class="q">{esc(pro)} {blank(150)}</div>')
    b.append(drill("Present tense of tener", "".join(bonus)))
    b.append(drill("Stretch (say them aloud)",
        '<div class="q">Preterite “I had” (yo): ' + blank(150) + '</div>'
        '<div class="q">Imperfect “I used to have” (yo): ' + blank(150) + '</div>'
        '<div class="q">Future “I will have” (yo): ' + blank(150) + '</div>'))

    # ---- ANSWER KEY ----
    b.append('<div class="page-break"></div>')
    b.append(eyebrow("Answer key"))
    b.append("<h2>Answer key</h2>")
    for title, ans in key_blocks:
        b.append(f'<h4>{esc(title)}</h4>')
        b.append('<p class="small" style="line-height:2">'
                 + " &nbsp;·&nbsp; ".join(esc(a) for a in ans) + "</p>")
    b.append('<h4>Quiz 6 · Explain the pattern (model answers)</h4>')
    for i, (form, why) in enumerate(QUIZ_EXPLAIN, 1):
        b.append(f'<p class="small"><b>{i}. {esc(form)}</b> — {esc(why)}</p>')
    b.append('<h4>Bonus · tener across time</h4>')
    b.append('<p class="small">Present: tengo, tienes, tiene, tenemos, tenéis, tienen. '
             '&nbsp;·&nbsp; Preterite (yo): tuve. &nbsp;·&nbsp; Imperfect (yo): tenía. '
             '&nbsp;·&nbsp; Future (yo): tendré.</p>')

    w("quizzes.html", shell_v("The Verb Book · Quizzes", "".join(b), subtitle="Quizzes"))


# ══════════════════════════════════════════════════════════════════════════
#  PAGE — CHEAT SHEETS
# ══════════════════════════════════════════════════════════════════════════
def build_cheatsheets():
    b = [eyebrow("Cheat sheets"),
         "<h1>Cheat Sheets</h1>",
         '<p class="muted">Keep these open while you work. Everything you need to '
         'conjugate, on a few pages.</p>']

    # Endings for all four tenses
    b.append("<h2>1 · Endings for every tense</h2>")
    b.append('<div class="legend"><span><span class="tense-tag tt-pres">Now</span> '
             'present</span><span><span class="tense-tag tt-past">Before</span> '
             'preterite & imperfect</span><span><span class="tense-tag tt-fut">Later'
             '</span> future</span></div>')
    b.append("<h4>Present</h4>")
    b.append(grid_conj([("-ar", ["-o", "-as", "-a", "-amos", "-áis", "-an"]),
                        ("-er", ["-o", "-es", "-e", "-emos", "-éis", "-en"]),
                        ("-ir", ["-o", "-es", "-e", "-imos", "-ís", "-en"])]))
    b.append("<h4>Preterite (finished actions)</h4>")
    b.append(grid_conj([("-ar", ["-é", "-aste", "-ó", "-amos", "-asteis", "-aron"]),
                        ("-er / -ir", ["-í", "-iste", "-ió", "-imos", "-isteis", "-ieron"])]))
    b.append("<h4>Imperfect (used to / was ___-ing)</h4>")
    b.append(grid_conj([("-ar", ["-aba", "-abas", "-aba", "-ábamos", "-abais", "-aban"]),
                        ("-er / -ir", ["-ía", "-ías", "-ía", "-íamos", "-íais", "-ían"])]))
    b.append("<h4>Future (add to the whole infinitive)</h4>")
    b.append(grid_conj([("all verbs", ["-é", "-ás", "-á", "-emos", "-éis", "-án"])]))

    # Irregular yo list
    b.append('<div class="page-break"></div>')
    b.append("<h2>2 · The irregular “yo” list</h2>")
    b.append('<p class="muted">Only the yo form changes — everything else is regular.</p>')
    b.append(chips([("hacer → hago", ""), ("poner → pongo", ""), ("salir → salgo", ""),
                    ("tener → tengo", ""), ("venir → vengo", ""), ("traer → traigo", ""),
                    ("decir → digo", ""), ("oír → oigo", ""), ("conocer → conozco", ""),
                    ("ver → veo", ""), ("dar → doy", ""), ("saber → sé", ""),
                    ("ir → voy", ""), ("estar → estoy", ""), ("ser → soy", "")]))

    # Boot diagram
    b.append("<h2>3 · The boot (stem-changers)</h2>")
    b.append('<p class="muted">The stem changes in the shaded forms — everywhere except '
             'the <span class="es">nosotros</span> form.</p>')
    b.append(grid_conj([("querer (e→ie)", vb.STEM_CHANGING["e→ie"][0]["forms"]),
                        ("poder (o→ue)", vb.STEM_CHANGING["o→ue"][0]["forms"]),
                        ("pedir (e→i)", vb.STEM_CHANGING["e→i"][0]["forms"])], boot=True))
    b.append('<p class="small">Common e→ie: querer, pensar, empezar, preferir, entender, '
             'tener, venir. &nbsp; o→ue: poder, dormir, volver, contar, encontrar. '
             '&nbsp; e→i: pedir, servir, repetir. &nbsp; u→ue: jugar.</p>')

    # Ser vs estar
    b.append('<div class="page-break"></div>')
    b.append("<h2>4 · Ser vs. Estar at a glance</h2>")
    b.append('<div class="grid" style="grid-template-columns:1fr 1fr;gap:12px">')
    b.append(box("sea", "Use SER for…",
        "<p>identity · origin · profession · permanent traits · time & dates · "
        "material. <br><span class='small'>DOCTOR: Description, Occupation, "
        "Characteristic, Time, Origin, Relationship.</span></p>"))
    b.append(box("cuba", "Use ESTAR for…",
        "<p>location · feelings · health · temporary states · the -ando/-iendo "
        "progressive. <br><span class='small'>PLACE: Position, Location, Action "
        "(-ing), Condition, Emotion.</span></p>"))
    b.append("</div>")

    # Time-word signals
    b.append("<h2>5 · Time words that signal the tense</h2>")
    b.append('<div class="grid" style="grid-template-columns:1fr 1fr 1fr;gap:12px">')
    b.append(box("trick", "Preterite signals",
        "<p>ayer · anoche · el lunes pasado · la semana pasada · el año pasado · "
        "de repente · una vez</p>"))
    b.append(box("trick", "Imperfect signals",
        "<p>siempre · todos los días · cada verano · de niña · mientras · "
        "generalmente · a menudo</p>"))
    b.append(box("trick", "Future signals",
        "<p>mañana · esta tarde · esta noche · el año que viene · algún día · "
        "la próxima semana · pronto</p>"))
    b.append("</div>")

    # Reflexive + gustar pronouns
    b.append("<h2>6 · Little pronoun tables</h2>")
    b.append('<div class="grid" style="grid-template-columns:1fr 1fr;gap:12px">')
    b.append(box("tip", "Reflexive (levantarse)",
        "<p>me · te · se · nos · se<br>"
        "<span class='es'>me levanto, te levantas, se levanta…</span></p>"))
    b.append(box("tip", "Gustar-type",
        "<p>me · te · le · nos · les<br>"
        "<span class='es'>me gusta</span> (one) / "
        "<span class='es'>me gustan</span> (many)</p>"))
    b.append("</div>")

    w("cheatsheets.html", shell_v("The Verb Book · Cheat Sheets", "".join(b),
                                  subtitle="Cheat Sheets"))


# ══════════════════════════════════════════════════════════════════════════
#  PAGE — REFERENCE  (full conjugation tables)
# ══════════════════════════════════════════════════════════════════════════
# A curated list of verbs to show in full across present (+ key ones with all tenses).
def build_reference():
    b = [eyebrow("Conjugation reference"),
         "<h1>Reference</h1>",
         '<p class="muted">Full present-tense tables for the verbs from your real life, '
         'grouped by pattern. The most important verbs also show their past and future '
         'forms so you can watch one verb move through time.</p>']

    # Present tables by pattern
    b.append("<h2>Present tense — regular models</h2>")
    b.append(grid_conj([(m["inf"], vb.present(m["inf"])) for m in vb.REGULAR_MODELS]))
    b.append('<p class="small">Every verb in the regular bank below follows one of these '
             'three exactly.</p>')
    b.append(chips([(inf, "") for inf, en, fam in vb.REGULAR_BANK]))

    b.append('<div class="page-break"></div>')
    b.append("<h2>Present tense — yo-form irregular</h2>")
    b.append('<p class="small">Only the yo form is irregular; the rest are regular.</p>')
    yo = vb.YO_IRREGULAR
    b.append(grid_conj([(v["inf"], v["forms"]) for v in yo[:4]]))
    b.append(grid_conj([(v["inf"], v["forms"]) for v in yo[4:]]))

    b.append("<h2>Present tense — stem-changing</h2>")
    for key in ["e→ie", "o→ue", "e→i", "u→ue"]:
        b.append(f'<h4>{esc(key)}</h4>')
        b.append(grid_conj([(v["inf"], v["forms"]) for v in vb.STEM_CHANGING[key]], boot=True))

    b.append('<div class="page-break"></div>')
    b.append("<h2>Present tense — completely irregular & combination</h2>")
    b.append(grid_conj([(v["inf"], v["forms"]) for v in vb.FULLY_IRREGULAR]))
    b.append(grid_conj([(v["inf"], v["forms"]) for v in vb.COMBINATION]))

    # A few key verbs across all four tenses
    b.append('<div class="page-break"></div>')
    b.append("<h2>Key verbs across all four tenses</h2>")
    b.append('<p class="muted">These are the verbs you\'ll use most. Study them '
             'vertically (one person, four tenses) and horizontally (one tense, six '
             'people).</p>')

    key_verbs = [
        ("ser", ["soy", "eres", "es", "somos", "sois", "son"],
                ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
                ["era", "eras", "era", "éramos", "erais", "eran"],
                ["seré", "serás", "será", "seremos", "seréis", "serán"]),
        ("estar", ["estoy", "estás", "está", "estamos", "estáis", "están"],
                  ["estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron"],
                  ["estaba", "estabas", "estaba", "estábamos", "estabais", "estaban"],
                  ["estaré", "estarás", "estará", "estaremos", "estaréis", "estarán"]),
        ("tener", ["tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen"],
                  ["tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"],
                  ["tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"],
                  ["tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán"]),
        ("ir", ["voy", "vas", "va", "vamos", "vais", "van"],
               ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
               ["iba", "ibas", "iba", "íbamos", "ibais", "iban"],
               ["iré", "irás", "irá", "iremos", "iréis", "irán"]),
        ("hacer", ["hago", "haces", "hace", "hacemos", "hacéis", "hacen"],
                  ["hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron"],
                  ["hacía", "hacías", "hacía", "hacíamos", "hacíais", "hacían"],
                  ["haré", "harás", "hará", "haremos", "haréis", "harán"]),
    ]
    for inf, pres, pret, imp, fut in key_verbs:
        b.append(f'<h3>{esc(inf)}</h3>')
        b.append(grid_conj([("Present", pres), ("Preterite", pret),
                            ("Imperfect", imp), ("Future", fut)]))

    w("reference.html", shell_v("The Verb Book · Reference", "".join(b),
                                subtitle="Reference"))


# ══════════════════════════════════════════════════════════════════════════
#  COMBINED SINGLE-PAGE ARTIFACT  (self-contained, tabbed, light+dark, audio)
# ══════════════════════════════════════════════════════════════════════════
import re
from content.theme import CSS as THEME_CSS
from build import ARTIFACT_EXTRA_CSS  # dark-mode tokens + sticky header/tabs + audio styles

# tab key, label, source file
ART_TABS = [
    ("home", "Home", "index.html"),
    ("learn", "Learn", "book.html"),
    ("practice", "Practice", "practice.html"),
    ("answers", "Answers", "answers.html"),
    ("quizzes", "Quizzes", "quizzes.html"),
    ("cheat", "Cheat Sheets", "cheatsheets.html"),
    ("reference", "Reference", "reference.html"),
]
_LINK_MAP = [  # order matters: longer/leading paths first
    ('href="../index.html"', 'href="#home" data-tab="home"'),
    ('href="index.html"', 'href="#home" data-tab="home"'),
    ('href="book.html"', 'href="#learn" data-tab="learn"'),
    ('href="practice.html"', 'href="#practice" data-tab="practice"'),
    ('href="answers.html"', 'href="#answers" data-tab="answers"'),
    ('href="quizzes.html"', 'href="#quizzes" data-tab="quizzes"'),
    ('href="cheatsheets.html"', 'href="#cheat" data-tab="cheat"'),
    ('href="reference.html"', 'href="#reference" data-tab="reference"'),
]


def _extract_page_body(html):
    """Pull the content that lived inside <div class="page"> …, minus our
    per-page NAV, the injected EXTRA_CSS <style>, and the footer."""
    start = html.index('<div class="page">') + len('<div class="page">')
    end = html.index('<div class="foot">', start)
    inner = html[start:end]
    inner = inner.replace(NAV, "")
    inner = inner.replace(EXTRA_CSS, "")
    for a, b in _LINK_MAP:
        inner = inner.replace(a, b)
    return inner.strip()


def build_combined_artifact():
    # read the freshly-built pages and turn each into a tab section
    sections, nav = [], []
    for key, label, fname in ART_TABS:
        nav.append(f'<button class="wb-tab" data-tab="{key}">{esc(label)}</button>')
        with open(os.path.join(OUT, fname), encoding="utf-8") as f:
            inner = _extract_page_body(f.read())
        sections.append(f'<section class="tab" id="tab-{key}">'
                        f'<div class="page">{inner}</div></section>')

    extra_inner = EXTRA_CSS.replace("<style>", "").replace("</style>", "")
    js = _ARTIFACT_JS

    body = (f'<style>{THEME_CSS}{ARTIFACT_EXTRA_CSS}{extra_inner}</style>'
            '<div class="wb-header"><div class="wb-bar">'
            '<span class="wb-brand">The Verb Book<span class="dot">.</span></span>'
            '<button id="enBtn" class="slow-btn on" title="Show or hide English" '
            'aria-pressed="true">🌐 English</button>'
            '<button id="slowBtn" class="slow-btn" title="Slow speech" '
            'aria-pressed="false">🐢 Slow</button>'
            f'<nav class="wb-tabs">{"".join(nav)}</nav></div></div>'
            '<div class="say-bar" id="sayBar"><span class="ic">🔊</span>'
            '<span>Tap any <b>green Spanish</b> word or sentence to hear it '
            '&amp; see the stressed syllable.</span>'
            '<button class="x" id="hintX" title="Dismiss" aria-label="Dismiss">'
            '&times;</button></div>'
            + "".join(sections)
            + f'<script>{js}</script>')

    path = os.path.join(OUT, "verb-book.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    print("wrote verbs/verb-book.html (%d KB) — self-contained artifact" % (len(body) // 1024))
    return path


# tab switching + tap-to-hear (phone's Spanish voice) + stressed-syllable popup
_ARTIFACT_JS = r"""
(function(){
  function show(name){
    document.querySelectorAll('.tab').forEach(function(s){
      s.classList.toggle('on', s.id==='tab-'+name); });
    document.querySelectorAll('.wb-tab').forEach(function(b){
      b.classList.toggle('on', b.dataset.tab===name); });
    window.scrollTo({top:0,behavior:'instant'}); hidePop();
  }
  var VOWELS='aeiouáéíóúü', ACCENTED='áéíóú', STRONG='aeoáéó';
  var CLUSTERS=['ch','ll','rr','pr','pl','br','bl','cr','cl','dr','tr','gr','gl','fr','fl'];
  function isV(c){return VOWELS.indexOf(c)>=0;}
  function syllabify(word){
    var w=word.toLowerCase(), nuclei=[], i=0;
    while(i<w.length){
      if(isV(w[i])){ var j=i;
        while(j+1<w.length && isV(w[j+1])){
          var a=w[j], b=w[j+1];
          var hiatus=(STRONG.indexOf(a)>=0&&STRONG.indexOf(b)>=0)||('íú'.indexOf(a)>=0)||('íú'.indexOf(b)>=0);
          if(hiatus) break; j++; }
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
  var SEL='.ex .es,.dlg .es,p.es,li.es,span.es,.vocab td:first-child,.conj .v,.grid-conj .v,.chip,.card .front';
  document.addEventListener('click', function(e){
    if(e.target.closest('[data-tab]')){ e.preventDefault(); show(e.target.closest('[data-tab]').getAttribute('data-tab')); return; }
    if(e.target.closest('.slow-btn')||e.target.closest('.say-bar')) return;
    var t=e.target.closest(SEL);
    if(!t){ hidePop(); return; }
    var text=esText(t);
    if(!text) return;
    speak(text, t);
    var words=text.split(/\s+/);
    if(words.length<=3 && /[a-záéíóúñü]/i.test(text)) showPop(markPhrase(text), t.getBoundingClientRect());
    else hidePop();
  });
  window.addEventListener('scroll', hidePop, {passive:true});
  var sb=document.getElementById('slowBtn');
  if(sb) sb.addEventListener('click', function(){ SLOW=!SLOW; sb.classList.toggle('on',SLOW);
    sb.setAttribute('aria-pressed', SLOW?'true':'false'); });
  var eb=document.getElementById('enBtn');
  if(eb) eb.addEventListener('click', function(){
    var off=document.body.classList.toggle('en-off');
    eb.classList.toggle('on', !off);
    eb.setAttribute('aria-pressed', off?'false':'true'); });
  var hx=document.getElementById('hintX');
  if(hx) hx.addEventListener('click', function(){ var b=document.getElementById('sayBar'); if(b) b.style.display='none'; });
  show('home');
})();
"""


# ══════════════════════════════════════════════════════════════════════════
def main():
    build_index()
    build_book()
    build_practice()
    build_answers()
    build_quizzes()
    build_cheatsheets()
    build_reference()
    build_combined_artifact()
    print("\nVerb workbook built into", OUT)


if __name__ == "__main__":
    main()
