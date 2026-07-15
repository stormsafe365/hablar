# -*- coding: utf-8 -*-
"""Parts I, IV, V, VI, VII, cheat sheets, and tests.

These sections are mostly prose + reference tables, so they're written as
functions that return HTML using the shared helpers in theme.py.
"""
from .theme import (box, examples, dialogue, vocab_table, conj_table, chips,
                    write_lines, questions, drill, blank, esc)


# ─────────────────────────────────────────────────────────────────────────
# PART I — FOUNDATIONS
# ─────────────────────────────────────────────────────────────────────────
def part1_foundations():
    h = []
    h.append('<div class="eyebrow">Part I</div>')
    h.append('<h1>Foundations</h1>')
    h.append('<p class="muted">How Spanish works, how to say it, and how to '
             'start thinking in it — before we touch a single verb chart.</p>')

    h.append('<h2>1 · How Spanish Works</h2>')
    h.append('<p>Spanish is more <em>regular</em> than English. Once you learn a '
             'pattern, it repeats almost everywhere. Three big ideas will carry you '
             'a long way:</p>')
    h.append(box('tip', 'The three pillars', (
        '<ul>'
        '<li><strong>Gender.</strong> Every noun is masculine or feminine. '
        '<span class="es">el mar</span> (the sea, m.), <span class="es">la playa</span> '
        '(the beach, f.). The word for “the” changes to match.</li>'
        '<li><strong>Agreement.</strong> Adjectives copy the noun\'s gender and '
        'number: <span class="es">el perro cariñoso</span>, <span class="es">las flores '
        'coloridas</span>.</li>'
        '<li><strong>Verb endings carry the “who.”</strong> The ending of a verb '
        'already tells you who does it, so you can often drop the pronoun: '
        '<span class="es">hablo</span> = <em>I</em> speak. No “yo” needed.</li>'
        '</ul>')))

    h.append('<h3>Gender in one minute</h3>')
    h.append('<p>Most words ending in <strong>-o</strong> are masculine, most ending '
             'in <strong>-a</strong> are feminine. Exceptions exist '
             '(<span class="es">el día</span>, <span class="es">la mano</span>), but '
             'the rule wins the vast majority of the time.</p>')
    h.append(vocab_table([
        ("el", "the (masculine singular)", "el café, el perro"),
        ("la", "the (feminine singular)", "la playa, la casa"),
        ("los", "the (masculine plural)", "los perros"),
        ("las", "the (feminine plural)", "las olas"),
        ("un / una", "a / an", "un café, una toalla"),
    ]))

    h.append('<h2>2 · Pronunciation</h2>')
    h.append('<p>Good news: Spanish is spelled how it sounds. Learn these and you can '
             'pronounce almost any word on sight. Vowels are <em>pure and short</em> — '
             'they never glide the way English vowels do.</p>')
    # tappable example words (audio + auto stress) — direct answer to "hear it"
    _pron = [
        ("a", "ah — like 'father'", "casa", "KAH-sah"),
        ("e", "eh — like 'bed'", "café", "kah-FEH"),
        ("i", "ee — like 'see'", "sí", "SEE"),
        ("o", "oh — like 'go' (short)", "sol", "SOHL"),
        ("u", "oo — like 'food'", "luna", "LOO-nah"),
        ("h", "always silent", "hola", "OH-lah"),
        ("j", "harsh 'h' from the throat", "jardín", "har-DEEN"),
        ("ll / y", "like 'y' in yes", "playa", "PLAH-yah"),
        ("ñ", "'ny' like canyon", "mañana", "mah-NYAH-nah"),
        ("v", "soft, almost like 'b'", "vamos", "BAH-mos"),
        ("z / c(e,i)", "like 's' in Latin America", "azúcar", "ah-SOO-car"),
    ]
    rows = ['<table class="vocab"><thead><tr><th>Letter</th><th>Sound</th>'
            '<th>Example <span class="small">(tap&nbsp;🔊)</span></th></tr></thead><tbody>']
    for letter, sound, word, hint in _pron:
        rows.append(f'<tr><td>{esc(letter)}</td><td>{esc(sound)}</td>'
                    f'<td><span class="es">{esc(word)}</span> '
                    f'<span class="small">({esc(hint)})</span></td></tr>')
    rows.append('</tbody></table>')
    h.append("".join(rows))
    h.append(box('cuba', 'Cuban note', (
        '<p>In Cuban Spanish, the <strong>s</strong> at the end of a syllable often '
        'softens or disappears: <span class="es">¿Cómo estás?</span> can sound like '
        '“¿Cómo etá?” and <span class="es">los amigos</span> like '
        '“lo amigo.” You don\'t have to copy it, but knowing it helps you '
        '<em>understand</em> your boyfriend and his family.</p>')))

    h.append('<h2>3 · Accent Marks</h2>')
    h.append('<p>That little mark (´) does two simple jobs:</p>')
    h.append('<ul>'
             '<li><strong>It tells you where to stress the word.</strong> '
             '<span class="es">café</span> = ca-<u>FÉ</u>. Without the mark you\'d say '
             'CA-fe.</li>'
             '<li><strong>It separates look-alike words.</strong> '
             '<span class="es">sí</span> (yes) vs <span class="es">si</span> (if); '
             '<span class="es">tú</span> (you) vs <span class="es">tu</span> (your); '
             '<span class="es">él</span> (he) vs <span class="es">el</span> (the).</li>'
             '</ul>')
    h.append(box('tip', 'The stress rule (no accent needed)', (
        '<ul>'
        '<li>Word ends in a <strong>vowel, n, or s</strong> → stress the '
        '<strong>second-to-last</strong> syllable. <span class="es">playa, hablan, '
        'perros</span>.</li>'
        '<li>Word ends in any <strong>other consonant</strong> → stress the '
        '<strong>last</strong> syllable. <span class="es">hablar, feliz, jardín</span> '
        '(jardín breaks the rule, so it <em>gets</em> an accent).</li>'
        '<li>An accent mark overrides all of this and just says “stress '
        'here.”</li>'
        '</ul>')))
    h.append('<p>The upside-down <strong>¿</strong> and <strong>¡</strong> open '
             'questions and exclamations so you know the tone before you start '
             'reading: <span class="es">¿Cómo estás?</span> · <span class="es">¡Qué '
             'rico!</span></p>')

    h.append('<h2>4 · Rolling Your R\'s</h2>')
    h.append('<p>There are two R sounds, and the difference actually matters:</p>')
    h.append('<ul>'
             '<li><strong>Soft R</strong> (single <em>r</em> in the middle of a word): '
             'a quick tap of the tongue, like the <em>tt</em> in American '
             '“butter.” <span class="es">pero</span> (but), '
             '<span class="es">mar</span>, <span class="es">cariño</span>.</li>'
             '<li><strong>Rolled RR</strong> (double <em>rr</em>, or <em>r</em> at the '
             'start of a word): a trill, several taps in a row. '
             '<span class="es">perro</span> (dog), <span class="es">arroz</span> '
             '(rice), <span class="es">remar</span> (to paddle).</li>'
             '</ul>')
    h.append(box('trick', 'How to learn the trill', (
        '<ul>'
        '<li>Say “<strong>butter-butter-butter</strong>” fast in an American '
        'accent — that tongue bounce is the soft R.</li>'
        '<li>For the roll, relax your tongue and blow air so the tip flutters against '
        'the ridge behind your top teeth. Practice the phrase '
        '<span class="es">“erre con erre, cigarro”</span>.</li>'
        '<li>It takes weeks, not minutes. If you can\'t roll yet, use a soft tap — '
        'people will still understand you completely.</li>'
        '<li><strong>Watch out:</strong> <span class="es">pero</span> (but) vs '
        '<span class="es">perro</span> (dog) is your daily reminder to practice.</li>'
        '</ul>')))

    h.append('<h2>5 · Sentence Structure</h2>')
    h.append('<p>Basic Spanish word order is the same as English — '
             '<strong>Subject → Verb → Object</strong> — so you can start building '
             'sentences immediately. A few twists:</p>')
    h.append(examples([
        ("Celeste bebe café.", "Celeste drinks coffee. (same order as English)"),
        ("El perro cariñoso.", "The affectionate dog. (adjective comes AFTER the noun)"),
        ("No quiero café.", "I don't want coffee. ('no' goes right before the verb)"),
        ("¿Quieres café?", "Do you want coffee? (no 'do' — just raise your voice)"),
        ("Me gusta la playa.", "I like the beach. (lit. 'the beach pleases me')"),
    ]))
    h.append(box('tip', 'Two shortcuts you\'ll use constantly', (
        '<ul>'
        '<li><strong>Making it negative:</strong> just put <span class="es">no</span> '
        'before the verb. That\'s the whole rule.</li>'
        '<li><strong>Asking a yes/no question:</strong> keep the same words, add '
        '<span class="es">¿ ?</span>, and let your voice rise at the end.</li>'
        '</ul>')))

    h.append('<h2>6 · Thinking in Spanish</h2>')
    h.append('<p>The goal isn\'t to translate faster — it\'s to stop translating. A '
             'few habits make that happen sooner:</p>')
    h.append('<ul>'
             '<li><strong>Name things in your day.</strong> Walking the dogs? Think '
             '<span class="es">los perros, la correa, la playa</span>. You already '
             'live in Spanish-able moments.</li>'
             '<li><strong>Learn chunks, not words.</strong> Store '
             '<span class="es">¿Cómo estás?</span> as one piece, not three.</li>'
             '<li><strong>Talk to yourself.</strong> Narrate small actions: '
             '<span class="es">Voy a la cocina. Hago café.</span></li>'
             '<li><strong>Accept “baby Spanish.”</strong> <span class="es">Yo '
             'querer café</span> is wrong but understandable. Speaking wrong beats '
             'staying silent — you fix it by using it.</li>'
             '</ul>')

    h.append('<h2>7 · Common Beginner Mistakes</h2>')
    h.append(vocab_table([
        ("ser vs estar", "both mean 'to be'", "ser = permanent, estar = temporary/location"),
        ("saber vs conocer", "both mean 'to know'", "saber = facts/skills, conocer = people/places"),
        ("Estoy caliente", "means 'I'm turned on' 😳", "for temperature say: tengo calor"),
        ("Soy 30", "wrong for age", "tengo 30 años (you HAVE 30 years)"),
        ("por vs para", "both ~ 'for'", "por = reason/through, para = goal/destination"),
        ("tú (you) vs tu (your)", "one letter, big difference", "tú tienes tu casa"),
        ("gustar", "not 'I like'", "me gusta = 'it pleases me' — flip the sentence"),
    ]))
    h.append(box('warn', 'The one that gets everyone', (
        '<p>Don\'t say <span class="es">Estoy caliente</span> to mean “I\'m hot” '
        '(temperature) — it means something very different. For heat use '
        '<span class="es">tengo calor</span>. For the weather being hot, '
        '<span class="es">hace calor</span>.</p>')))

    h.append('<h2>8 · Memory Tricks That Actually Work</h2>')
    h.append('<ul>'
             '<li><strong>Hook new words to your life.</strong> '
             '<span class="es">la arena</span> (sand) → picture the “arena” of '
             'your beach. <span class="es">el pollo</span> (chicken) → a chicken saying '
             '“Polly.”</li>'
             '<li><strong>Group by the “g” yo-verbs.</strong> tengo, vengo, '
             'pongo, salgo, hago, digo, oigo — nearly all your irregular '
             '<em>yo</em> forms grow a G. Learn the club, not seven exceptions.</li>'
             '<li><strong>Say it out loud 3×.</strong> Muscle memory beats staring.</li>'
             '<li><strong>Spaced repetition.</strong> Use the flashcards in this pack: '
             'review a word today, tomorrow, in three days, then weekly.</li>'
             '</ul>')
    h.append(box('tip', 'Your daily 15 minutes', (
        '<p>5 min flashcards · 5 min read one story out loud · 5 min say what '
        'you\'re doing in Spanish. Consistency beats marathon sessions every time.</p>')))
    return "".join(h)


# ─────────────────────────────────────────────────────────────────────────
# PART IV — PAST TENSE
# ─────────────────────────────────────────────────────────────────────────
def part4_past():
    h = []
    h.append('<div class="eyebrow">Part IV</div>')
    h.append('<h1>Past Tense — Talking About Yesterday</h1>')
    h.append('<p class="muted">The <strong>pretérito</strong> is the “what '
             'happened” tense: finished actions with a clear end. It\'s how you '
             'tell someone about your day, your weekend, or your last trip.</p>')

    h.append('<h2>1 · Regular Verbs</h2>')
    h.append('<p>Chop off the ending (-ar / -er / -ir) and add these. Notice '
             '<strong>-er</strong> and <strong>-ir</strong> share the exact same '
             'endings — one less thing to learn.</p>')
    h.append('<div style="display:flex;gap:16px;flex-wrap:wrap">')
    h.append('<div style="flex:1;min-width:230px">' +
             conj_table("hablar → to speak", [
                ("yo", "hablé"), ("tú", "hablaste"), ("él/ella", "habló"),
                ("nosotros", "hablamos"), ("vosotros", "hablasteis"),
                ("ellos/ustedes", "hablaron")]) + '</div>')
    h.append('<div style="flex:1;min-width:230px">' +
             conj_table("comer → to eat", [
                ("yo", "comí"), ("tú", "comiste"), ("él/ella", "comió"),
                ("nosotros", "comimos"), ("vosotros", "comisteis"),
                ("ellos/ustedes", "comieron")]) + '</div>')
    h.append('</div>')
    h.append(conj_table("vivir → to live (-ir uses -er endings)", [
        ("yo", "viví"), ("tú", "viviste"), ("él/ella", "vivió"),
        ("nosotros", "vivimos"), ("vosotros", "vivisteis"),
        ("ellos/ustedes", "vivieron")]))
    h.append(box('trick', 'Hear the accent', (
        '<p>Regular preterite lives on its <em>final</em> syllable in the “I” and '
        '“he/she” forms: <span class="es">hablé, habló · comí, comió</span>. '
        'That stressed ending is the sound of the past.</p>')))
    h.append(examples([
        ("Ayer hablé español con la familia de mi novio.", "Yesterday I spoke Spanish with my boyfriend's family."),
        ("Comí arroz con pollo anoche.", "I ate chicken and rice last night."),
        ("Nadé en el mar por la mañana.", "I swam in the sea in the morning."),
        ("Mi novio cocinó una cena deliciosa.", "My boyfriend cooked a delicious dinner."),
        ("Paseamos a los perros por la playa.", "We walked the dogs on the beach."),
        ("¿Trabajaste ayer?", "Did you work yesterday?"),
    ]))

    h.append('<h2>2 · Irregular Verbs</h2>')
    h.append('<p>A handful of everyday verbs are irregular — but they\'re the ones '
             'you\'ll use most, so they stick fast. The big ones:</p>')
    h.append('<div style="display:flex;gap:16px;flex-wrap:wrap">')
    h.append('<div style="flex:1;min-width:220px">' +
             conj_table("ser / ir → was / went (identical!)", [
                ("yo", "fui"), ("tú", "fuiste"), ("él/ella", "fue"),
                ("nosotros", "fuimos"), ("ellos/ustedes", "fueron")]) + '</div>')
    h.append('<div style="flex:1;min-width:220px">' +
             conj_table("tener → had", [
                ("yo", "tuve"), ("tú", "tuviste"), ("él/ella", "tuvo"),
                ("nosotros", "tuvimos"), ("ellos/ustedes", "tuvieron")]) + '</div>')
    h.append('</div>')
    h.append('<div style="display:flex;gap:16px;flex-wrap:wrap">')
    h.append('<div style="flex:1;min-width:220px">' +
             conj_table("hacer → did / made", [
                ("yo", "hice"), ("tú", "hiciste"), ("él/ella", "hizo"),
                ("nosotros", "hicimos"), ("ellos/ustedes", "hicieron")]) + '</div>')
    h.append('<div style="flex:1;min-width:220px">' +
             conj_table("estar → was (state/place)", [
                ("yo", "estuve"), ("tú", "estuviste"), ("él/ella", "estuvo"),
                ("nosotros", "estuvimos"), ("ellos/ustedes", "estuvieron")]) + '</div>')
    h.append('</div>')
    h.append(box('tip', 'The best two-for-one in Spanish', (
        '<p><span class="es">ser</span> and <span class="es">ir</span> are '
        '<em>identical</em> in the past. <span class="es">Fui a la playa</span> = '
        'I <em>went</em> to the beach; <span class="es">Fui feliz</span> = I '
        '<em>was</em> happy. Context tells you which.</p>')))
    h.append(examples([
        ("Fui a la playa el sábado.", "I went to the beach on Saturday."),
        ("Tuve un día muy bueno.", "I had a very good day."),
        ("Hice paddleboard por la mañana.", "I paddleboarded in the morning."),
        ("Estuvimos en casa de su mamá.", "We were at his mom's house."),
        ("Mi novio hizo café cubano.", "My boyfriend made Cuban coffee."),
    ]))

    h.append('<h2>3 · Time Words for the Past</h2>')
    h.append(chips([
        ("ayer", "yesterday"), ("anoche", "last night"), ("anteayer", "day before yesterday"),
        ("la semana pasada", "last week"), ("el mes pasado", "last month"),
        ("el año pasado", "last year"), ("hace dos días", "two days ago"),
        ("esta mañana", "this morning"), ("el fin de semana", "the weekend"),
    ]))

    h.append('<h2>4 · Talking About a Trip</h2>')
    h.append(dialogue([
        ("Amiga", "¿Qué hiciste el fin de semana?", "What did you do this weekend?"),
        ("Celeste", "Fui a la playa con mi novio.", "I went to the beach with my boyfriend."),
        ("Amiga", "¿Qué tal?", "How was it?"),
        ("Celeste", "¡Muy bien! Hice paddleboard y vi delfines.", "Great! I paddleboarded and saw dolphins."),
        ("Celeste", "Después comimos en un restaurante cubano.", "Then we ate at a Cuban restaurant."),
    ]))

    h.append('<h2>5 · Story: “Mi fin de semana”</h2>')
    h.append(_story_block(
        "El sábado pasado fui a la playa muy temprano. Hizo sol todo el día y el mar "
        "estuvo tranquilo. Hice paddleboard por la mañana y vi dos delfines cerca de "
        "la orilla. Después, mi novio y yo comimos en un restaurante cubano. Yo comí "
        "arroz con pollo y él comió ropa vieja. Por la tarde, caminamos por la playa "
        "y vimos el atardecer. Fue un fin de semana perfecto.",
        "Last Saturday I went to the beach very early. It was sunny all day and the "
        "sea was calm. I paddleboarded in the morning and saw two dolphins near the "
        "shore. Afterward, my boyfriend and I ate at a Cuban restaurant. I had "
        "chicken and rice and he had ropa vieja. In the afternoon, we walked on the "
        "beach and watched the sunset. It was a perfect weekend."))
    return "".join(h)


def _story_block(es, en):
    return (f'<div class="box"><p class="es" style="font-size:17px">{esc(es)}</p>'
            f'<p class="en small" style="margin-top:10px">{esc(en)}</p></div>')


# ─────────────────────────────────────────────────────────────────────────
# PART V — READING (graded stories)
# ─────────────────────────────────────────────────────────────────────────
READING_LADDER = [
    {
      "level": "Level 1 · 5-word stories",
      "note": "Read each out loud. Every word is one you know.",
      "stories": [
        ("Voy a la playa hoy.", "I go to the beach today."),
        ("El perro corre en arena.", "The dog runs in sand."),
        ("Tengo hambre y sed.", "I'm hungry and thirsty."),
        ("Mi novio hace café.", "My boyfriend makes coffee."),
        ("Hace calor en Florida.", "It's hot in Florida."),
      ],
    },
    {
      "level": "Level 2 · One-line stories",
      "note": "A little longer. Notice the verbs you studied in Part II.",
      "stories": [
        ("Por la mañana, riego las plantas y doy de comer a los perros.",
         "In the morning, I water the plants and feed the dogs."),
        ("Mi novio pone música cubana y bailamos en la cocina.",
         "My boyfriend plays Cuban music and we dance in the kitchen."),
        ("Cuando hace sol, vamos a la playa y hago paddleboard.",
         "When it's sunny, we go to the beach and I paddleboard."),
      ],
    },
]


def _reading_story_full():
    return {
        "title": "Un domingo tranquilo",
        "es": ("Es domingo por la mañana y la casa está tranquila. Celeste se "
               "despierta temprano, antes que su novio. Va a la cocina y prepara "
               "un cafecito cubano, fuerte y dulce. Afuera, el jardín está verde y "
               "las flores del hibisco están abiertas. Los dos perros duermen en el "
               "sofá.\n\n"
               "Después de un rato, su novio se levanta. “Buenos días, mi "
               "amor”, dice, y le da un beso. Toman el café juntos en el jardín "
               "y hablan de sus planes. Hace buen tiempo, así que deciden ir a la "
               "playa.\n\n"
               "En la playa, Celeste hace paddleboard mientras su novio nada. El "
               "mar está tranquilo y ven un delfín a lo lejos. Al mediodía, vuelven "
               "a casa, cansados y felices. Su novio cocina arroz con pollo y "
               "escuchan salsa. “Me encanta nuestra vida aquí”, dice "
               "Celeste. Y es verdad."),
        "en": ("It's Sunday morning and the house is quiet. Celeste wakes up early, "
               "before her boyfriend. She goes to the kitchen and makes a Cuban "
               "cafecito, strong and sweet. Outside, the garden is green and the "
               "hibiscus flowers are open. The two dogs sleep on the couch.\n\n"
               "After a while, her boyfriend gets up. “Good morning, my love,” "
               "he says, and gives her a kiss. They have coffee together in the "
               "garden and talk about their plans. The weather is nice, so they "
               "decide to go to the beach.\n\n"
               "At the beach, Celeste paddleboards while her boyfriend swims. The "
               "sea is calm and they see a dolphin in the distance. At noon, they "
               "return home, tired and happy. Her boyfriend cooks chicken and rice "
               "and they listen to salsa. “I love our life here,” says "
               "Celeste. And it's true."),
        "vocab": [
            ("se despierta", "she wakes up", ""),
            ("un rato", "a while", ""),
            ("se levanta", "he gets up", ""),
            ("mientras", "while", ""),
            ("a lo lejos", "in the distance", ""),
            ("así que", "so / therefore", ""),
        ],
        "grammar": ("This story mixes <strong>present tense</strong> (está, "
                    "prepara, hacen) with reflexive verbs (<span class='es'>se "
                    "despierta</span>, <span class='es'>se levanta</span>) — verbs "
                    "where you do the action to yourself. You'll meet these fully "
                    "later; for now, just notice the little <span class='es'>se</span>."),
        "questions": [
            "¿A qué hora se despierta Celeste, temprano o tarde?",
            "¿Qué prepara en la cocina?",
            "¿Adónde deciden ir?",
            "¿Qué hace el novio mientras Celeste hace paddleboard?",
            "¿Qué cocina el novio al final?",
        ],
        "prompt": ("Write 4–5 sentences about your own perfect Sunday, in Spanish. "
                   "Use the present tense and at least three verbs from Part II."),
        "convo": [
            "¿Cómo es tu domingo típico?",
            "¿Prefieres la mañana o la tarde? ¿Por qué?",
            "¿Qué te gusta hacer para descansar?",
        ],
    }


def part5_reading():
    h = []
    h.append('<div class="eyebrow">Part V</div>')
    h.append('<h1>Reading</h1>')
    h.append('<p class="muted">We climb a ladder: from 5-word stories to a full '
             'page. Read each one <strong>out loud</strong> — reading aloud trains '
             'your ear and mouth at the same time.</p>')

    for block in READING_LADDER:
        h.append(f'<h2>{esc(block["level"])}</h2>')
        h.append(f'<p class="small">{block["note"]}</p>')
        h.append(examples(block["stories"]))

    st = _reading_story_full()
    h.append('<h2>Level 3 · A full story</h2>')
    h.append(f'<h3>{esc(st["title"])}</h3>')
    for para in st["es"].split("\n\n"):
        h.append(f'<p class="es" style="font-size:16.5px">{esc(para)}</p>')
    h.append('<details class="no-print"><summary class="small">Show English '
             'translation</summary>')
    for para in st["en"].split("\n\n"):
        h.append(f'<p class="en small">{esc(para)}</p>')
    h.append('</details>')
    # print version always shows English quietly
    h.append('<div style="display:none" class="print-only"></div>')

    h.append('<h4>Vocabulary</h4>')
    h.append(vocab_table(st["vocab"]))
    h.append('<h4>Grammar note</h4>')
    h.append(f'<p>{st["grammar"]}</p>')
    h.append('<h4>Comprehension questions</h4>')
    h.append(drill("Answer in Spanish", questions(
        [f'{esc(q)}<br>{write_lines(1)}' for q in st["questions"]])))
    h.append('<h4>Writing prompt</h4>')
    h.append(box('tip', 'Escribe', f'<p>{esc(st["prompt"])}</p>' + write_lines(5)))
    h.append('<h4>Conversation</h4>')
    h.append('<p class="small">Ask your tutor (or answer yourself):</p>')
    h.append('<ul>' + "".join(f'<li class="es">{esc(q)}</li>' for q in st["convo"]) + '</ul>')
    return "".join(h)


# ─────────────────────────────────────────────────────────────────────────
# PART VI — SPEAKING
# ─────────────────────────────────────────────────────────────────────────
SPEAKING_BANKS = [
    ("About you", [
        "¿Cómo te llamas y de dónde eres?",
        "¿Cuántos años tienes?",
        "¿Dónde vives? ¿Te gusta?",
        "¿Cómo eres? Describe tu personalidad.",
        "¿Qué te gusta hacer los fines de semana?",
        "¿Cuál es tu comida favorita?",
    ]),
    ("Daily life", [
        "¿A qué hora te despiertas normalmente?",
        "¿Qué haces por la mañana?",
        "¿Trabajas? ¿Qué haces en tu trabajo?",
        "¿Qué haces para descansar?",
        "¿Vas al gimnasio? ¿Qué ejercicios haces?",
        "¿Cocinas o prefieres comer fuera?",
    ]),
    ("Beach & Florida", [
        "¿Con qué frecuencia vas a la playa?",
        "¿Qué te gusta hacer en el mar?",
        "Describe un día perfecto en la playa.",
        "¿Cómo es el clima de Florida en verano?",
        "¿Qué haces cuando hay una tormenta?",
    ]),
    ("Love & family", [
        "¿Cómo conociste a tu novio?",
        "¿Qué te gusta hacer juntos?",
        "Describe a tu novio en cinco frases.",
        "¿Qué comidas cubanas te gustan?",
        "¿Por qué quieres aprender español?",
    ]),
    ("Opinions & the future", [
        "¿Qué quieres hacer este año?",
        "¿Adónde quieres viajar? ¿Por qué?",
        "¿Qué es lo más difícil del español para ti?",
        "¿Qué te gusta más: la mañana o la noche?",
        "Si tienes un día libre, ¿qué haces?",
    ]),
]

ROLE_PLAYS = [
    ("Ordering at a Cuban café",
     "You want a cortadito and a pastelito. Greet, order, ask the price, pay, "
     "and thank them. Partner plays the barista.",
     ["Buenas, ¿me da un cortadito, por favor?",
      "¿Cuánto es?", "Gracias, muy amable."]),
    ("Meeting your boyfriend's family",
     "It's your first dinner with his family. Introduce yourself, say where you're "
     "from, compliment the food, and ask a question.",
     ["Mucho gusto, soy Celeste.", "La comida está deliciosa.",
      "¿Cómo se hace este plato?"]),
    ("At the market",
     "Buy fruit for the week. Ask what's fresh, ask prices, choose, and pay.",
     ["¿Qué fruta está fresca hoy?", "¿A cuánto están los mangos?",
      "Me llevo tres, por favor."]),
    ("Making weekend plans",
     "Call your boyfriend and plan Saturday: beach in the morning, dinner at night. "
     "Agree on times.",
     ["¿Vamos a la playa el sábado?", "¿A qué hora salimos?",
      "Y por la noche, ¿cenamos fuera?"]),
]


def part6_speaking():
    h = []
    h.append('<div class="eyebrow">Part VI</div>')
    h.append('<h1>Speaking</h1>')
    h.append('<p class="muted">Speaking is a muscle. Here are hundreds of prompts, '
             'role-plays, and real conversations — bring them to your tutor, or '
             'answer them out loud on your own. There are no wrong answers, only '
             'reps.</p>')

    h.append('<h2>Conversation Question Banks</h2>')
    h.append('<p class="small">Answer each in full sentences. Push yourself to add '
             'a “because” (<span class="es">porque…</span>) to every answer.</p>')
    for title, qs in SPEAKING_BANKS:
        h.append(f'<h3>{esc(title)}</h3>')
        h.append('<ul>' + "".join(f'<li class="es">{esc(q)}</li>' for q in qs) + '</ul>')

    h.append('<h2>Role-Plays</h2>')
    h.append('<p class="small">Act these out with a partner or your tutor. Starter '
             'lines are given — improvise the rest.</p>')
    for title, setup, lines in ROLE_PLAYS:
        inner = (f'<p>{esc(setup)}</p><p class="small" style="margin-top:6px">'
                 'Try starting with:</p><ul>' +
                 "".join(f'<li class="es">{esc(l)}</li>' for l in lines) + '</ul>')
        h.append(drill(title, inner))

    h.append('<h2>The 20-Minute Conversation Ladder</h2>')
    h.append('<p>Build up to a real conversation with your tutor in stages. Add one '
             'rung each week:</p>')
    h.append('<ol>'
             '<li><strong>2 min:</strong> Greetings + how you are + the weather.</li>'
             '<li><strong>5 min:</strong> Describe your day today (present tense).</li>'
             '<li><strong>10 min:</strong> Talk about last weekend (past tense).</li>'
             '<li><strong>15 min:</strong> Describe your life — beach, dogs, work, '
             'boyfriend.</li>'
             '<li><strong>20+ min:</strong> Give opinions and plans '
             '(<span class="es">quiero, voy a, me gusta…</span>) and ask your tutor '
             'questions back.</li>'
             '</ol>')
    h.append(box('tip', 'Rescue phrases (memorize these first)', chips([
        ("¿Cómo se dice…?", "How do you say…?"),
        ("¿Puedes repetir?", "Can you repeat?"),
        ("Más despacio, por favor.", "Slower, please."),
        ("No entiendo.", "I don't understand."),
        ("¿Qué significa…?", "What does… mean?"),
        ("Un momento…", "One moment…"),
        ("¿Cómo?", "Sorry, what?"),
    ])))
    return "".join(h)


# ─────────────────────────────────────────────────────────────────────────
# PART VII — CUBAN SPANISH
# ─────────────────────────────────────────────────────────────────────────
def part7_cuban():
    h = []
    h.append('<div class="eyebrow">Part VII</div>')
    h.append('<h1>Cuban Spanish</h1>')
    h.append('<p class="muted">The Spanish your boyfriend actually speaks. Textbook '
             'Spanish gets you understood; this gets you <em>in</em>. Expressions, '
             'slang, sound, and a little culture.</p>')

    h.append('<h2>1 · Expressions Your Boyfriend Actually Says</h2>')
    h.append(vocab_table([
        ("¡Dale!", "Okay! / Go for it! / Cool!", "the all-purpose yes"),
        ("¿Qué bolá?", "What's up?", "the classic Cuban greeting"),
        ("asere / acere", "buddy, dude", "to a close friend"),
        ("mi amor / mi vida", "my love / my life", "used freely, even casually"),
        ("¡Qué rico!", "How delicious! / How nice!", "food, weather, anything good"),
        ("¡Coño!", "Ugh! / Wow! / Damn!", "mild, extremely common"),
        ("está en talla", "it's perfect / all good", ""),
        ("¡Tremendo…!", "What a huge…!", "tremendo calor = crazy heat"),
        ("¿Cómo anda la cosa?", "How's it going?", "lit. 'how walks the thing'"),
        ("estar arrebatado", "to be crazy/wild about", ""),
    ]))
    h.append(box('cuba', 'Dale — the word you\'ll hear most', (
        '<p><span class="es">Dale</span> does everything: “okay,” “go '
        'ahead,” “let\'s do it,” “bye then.” <span class="es">— ¿Vamos a '
        'la playa? — ¡Dale!</span> When in doubt, <span class="es">dale</span> '
        'fits.</p>')))

    h.append('<h2>2 · Slang & Everyday Words</h2>')
    h.append(vocab_table([
        ("la guagua", "the bus", "very Cuban"),
        ("la jama", "food", "¿hay jama? = is there food?"),
        ("jamar", "to eat", ""),
        ("el pincha", "the job/work", "voy pa' la pincha"),
        ("la fula", "money / the dollar", ""),
        ("chévere", "cool, great", "shared across the Caribbean"),
        ("la yuma", "the US / a foreigner", ""),
        ("consorte", "close friend, partner", ""),
        ("estar en la lucha", "to be hustling/getting by", "a way of life"),
        ("¡Qué va!", "No way!", ""),
    ]))

    h.append('<h2>3 · Pronunciation — How Cuban Sounds</h2>')
    h.append('<p>You don\'t need to imitate it, but recognizing these patterns is the '
             'difference between understanding your boyfriend\'s family and nodding '
             'politely:</p>')
    h.append('<ul>'
             '<li><strong>Dropped S.</strong> The <em>s</em> at the end of syllables '
             'fades: <span class="es">¿Cómo estás?</span> → “¿Cómo etá?”; '
             '<span class="es">más o menos</span> → “má o meno.”</li>'
             '<li><strong>Swallowed D.</strong> The <em>-ado</em> ending softens: '
             '<span class="es">pescado</span> → “pescao,” '
             '<span class="es">cansado</span> → “cansao.”</li>'
             '<li><strong>R → L (in some areas).</strong> <span class="es">por '
             'favor</span> can sound like “pol favol.”</li>'
             '<li><strong>Fast and musical.</strong> Words run together. Listen for '
             'the <em>chunks</em>, not every letter.</li>'
             '</ul>')
    h.append(box('tip', 'Train your ear', (
        '<p>Search YouTube for “Cuban Spanish conversation” or listen to Cuban '
        'salsa and reggaeton with the lyrics up. Your goal isn\'t to catch every '
        'word — it\'s to get comfortable with the <em>rhythm</em>.</p>')))

    h.append('<h2>4 · Culture Notes</h2>')
    h.append('<ul>'
             '<li><strong>Warmth is default.</strong> <span class="es">mi amor</span>, '
             '<span class="es">mi vida</span>, <span class="es">cariño</span> are '
             'sprinkled everywhere — even the lady at the counter may call you '
             '“mi amor.”</li>'
             '<li><strong>Coffee is connection.</strong> A <span class="es">cafecito</span> '
             'is an invitation, a pause, a sign of welcome. Never say no to one.</li>'
             '<li><strong>Family and food are the center.</strong> Expect big meals, '
             'loud tables, and lots of “<span class="es">come más</span>” '
             '(eat more!). Complimenting the cook is always right.</li>'
             '<li><strong>Music is everywhere.</strong> Salsa, son, timba, reggaetón — '
             'and dancing isn\'t optional at a party. It\'s okay to be a beginner; '
             'joining in matters more than getting it right.</li>'
             '</ul>')
    h.append('<h2>5 · A Cuban-flavored dialogue</h2>')
    h.append(dialogue([
        ("Novio", "¿Qué bolá, mi amor? ¿Cómo anda la cosa?", "What's up, my love? How's it going?"),
        ("Celeste", "Todo bien. ¿Vamos a la playa?", "All good. Shall we go to the beach?"),
        ("Novio", "¡Dale! Pero primero, un cafecito.", "For sure! But first, a little coffee."),
        ("Celeste", "¡Qué rico! Y después, ¿jamamos algo?", "Nice! And after, shall we eat something?"),
        ("Novio", "Claro, asere. Hay arroz con pollo en casa.", "Of course, girl. There's chicken and rice at home."),
    ]))
    return "".join(h)


# ─────────────────────────────────────────────────────────────────────────
# CHEAT SHEETS
# ─────────────────────────────────────────────────────────────────────────
def cheat_sheets():
    h = []
    h.append('<div class="eyebrow">Quick Reference</div>')
    h.append('<h1>Cheat Sheets</h1>')
    h.append('<p class="muted">Tear these out (or keep them on your phone). '
             'Everything you reach for most, in one place.</p>')

    h.append('<h2>Survival Phrases</h2>')
    h.append(vocab_table([
        ("Hola / Buenas", "Hi / Hello", ""),
        ("Buenos días", "Good morning", ""),
        ("Buenas tardes / noches", "Good afternoon / evening", ""),
        ("¿Cómo estás?", "How are you?", ""),
        ("Bien, gracias. ¿Y tú?", "Good, thanks. And you?", ""),
        ("Por favor / Gracias", "Please / Thank you", ""),
        ("De nada", "You're welcome", ""),
        ("Perdón / Disculpa", "Sorry / Excuse me", ""),
        ("Sí / No", "Yes / No", ""),
        ("No entiendo", "I don't understand", ""),
        ("¿Cómo se dice…?", "How do you say…?", ""),
        ("Más despacio, por favor", "Slower, please", ""),
        ("Nos vemos", "See you", ""),
        ("Hasta luego", "See you later", ""),
    ]))

    h.append('<h2>The 16 Verbs — Present Tense (yo / tú / él)</h2>')
    from .verbs import VERBS
    rows = []
    for v in VERBS:
        forms = dict(v["conj"])
        yo = v["conj"][0][1]; tu = v["conj"][1][1]; el = v["conj"][2][1]
        rows.append((v["inf"].lower(), f"{yo} · {tu} · {el}", v["meaning"].split("(")[0].strip()))
    h.append(vocab_table(rows))

    h.append('<h2>Ser vs Estar (both = “to be”)</h2>')
    h.append('<div style="display:flex;gap:16px;flex-wrap:wrap">')
    h.append('<div style="flex:1;min-width:230px">' + box('tip', 'SER — permanent',
        '<ul><li>Identity: soy Celeste</li><li>Origin: es de Cuba</li>'
        '<li>Traits: el café es fuerte</li><li>Time: son las ocho</li></ul>') + '</div>')
    h.append('<div style="flex:1;min-width:230px">' + box('sea', 'ESTAR — temporary',
        '<ul><li>Feelings: estoy cansada</li><li>Location: está en la playa</li>'
        '<li>Conditions: el café está frío</li><li>-ing: estoy cocinando</li></ul>') + '</div>')
    h.append('</div>')

    h.append('<h2>Numbers</h2>')
    h.append(vocab_table([
        ("0–10", "cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez", ""),
        ("11–15", "once, doce, trece, catorce, quince", ""),
        ("16–20", "dieciséis, diecisiete, dieciocho, diecinueve, veinte", ""),
        ("30 / 40 / 50", "treinta, cuarenta, cincuenta", ""),
        ("100 / 1000", "cien, mil", ""),
    ]))

    h.append('<h2>Days, Months & Time</h2>')
    h.append(chips([("lunes","Mon"),("martes","Tue"),("miércoles","Wed"),
        ("jueves","Thu"),("viernes","Fri"),("sábado","Sat"),("domingo","Sun")]))
    h.append(chips([("enero","Jan"),("febrero","Feb"),("marzo","Mar"),("abril","Apr"),
        ("mayo","May"),("junio","Jun"),("julio","Jul"),("agosto","Aug"),
        ("septiembre","Sep"),("octubre","Oct"),("noviembre","Nov"),("diciembre","Dec")]))
    h.append(vocab_table([
        ("¿Qué hora es?", "What time is it?", ""),
        ("Es la una", "It's one o'clock", "singular for 1"),
        ("Son las dos / tres…", "It's two / three…", "plural for 2+"),
        ("y media", "half past", "son las dos y media"),
        ("y cuarto / menos cuarto", "quarter past / to", ""),
        ("de la mañana / tarde / noche", "AM / afternoon / evening", ""),
    ]))

    h.append('<h2>Question Words</h2>')
    h.append(chips([("¿Qué?","What?"),("¿Quién?","Who?"),("¿Dónde?","Where?"),
        ("¿Cuándo?","When?"),("¿Por qué?","Why?"),("¿Cómo?","How?"),
        ("¿Cuánto?","How much?"),("¿Cuál?","Which?"),("¿Adónde?","Where to?")]))

    h.append('<h2>Connector Words (make sentences longer)</h2>')
    h.append(chips([("y","and"),("pero","but"),("porque","because"),("también","also"),
        ("entonces","so/then"),("después","after"),("primero","first"),
        ("por eso","that's why"),("aunque","although"),("cuando","when")]))
    return "".join(h)
