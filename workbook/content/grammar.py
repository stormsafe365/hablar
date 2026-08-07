# -*- coding: utf-8 -*-
"""Everyday verb forms + conversation content, merged in from Jenna's own
learning materials (Taller de Español Vol. 1 & 2, the past-tense playbook).

Covers the pieces the first draft was missing:
  - the near future (ir a + verb) and the two-verb rule
  - the present progressive (estar + -ando/-iendo)
  - reflexive verbs (daily routine)
  - stem-changing verbs (the "boot")
  - the #1 habit: answer in a full sentence + porque
  - grow-an-answer ladders, the 30 conversation cards, and the about-you script
"""
from .theme import (box, examples, dialogue, vocab_table, conj_table, chips,
                    write_lines, questions, drill, blank, esc)

P5 = ["yo", "tú", "él / ella / usted", "nosotros", "ellos / ellas / ustedes"]

def _c(*forms):
    return list(zip(P5, forms))


# ─────────────────────────────────────────────────────────────────────────
# PART · EVERYDAY VERB FORMS
# ─────────────────────────────────────────────────────────────────────────
def part_verb_forms():
    h = []
    h.append('<div class="eyebrow">Part III</div>')
    h.append('<h1>The Everyday Verb Forms</h1>')
    h.append('<p class="muted">You already have the present tense. These few small '
             'tools instantly double what you can say — and each takes about ten '
             'minutes. The best news is hidden in all of them: <strong>only the '
             'first verb ever changes.</strong></p>')

    # the four forms at a glance
    h.append('<h2>1 · The four things a verb can do</h2>')
    h.append('<p>Same verb (<span class="es">trabajar</span>, to work), four forms. '
             'Two you know, two are new:</p>')
    h.append(vocab_table([
        ("Trabajo hoy.", "I work today.", "present"),
        ("Voy a trabajar mañana.", "I'm going to work tomorrow.", "near future — NEW"),
        ("Estoy trabajando.", "I'm working (right now).", "progressive — NEW"),
        ("Trabajé ayer.", "I worked yesterday.", "past"),
    ]))
    h.append(box('tip', 'The rule that ties them together', (
        '<p>In <span class="es">voy a <u style="text-decoration:none">trabajar</u></span>, '
        'only <span class="es">voy</span> is conjugated — <span class="es">trabajar</span> '
        'stays in its plain dictionary form. Learn five “openers” and you can say '
        'hundreds of things while only ever changing these five:</p>')
        + chips([("quiero…", "I want to…"), ("puedo…", "I can…"),
                 ("necesito…", "I need to…"), ("voy a…", "I'm going to…"),
                 ("me gusta…", "I like to…"), ("tengo que…", "I have to…")])))

    # near future
    h.append('<h2>2 · The near future — <span class="es">ir a</span> + verb</h2>')
    h.append('<p>This is how people <em>actually</em> talk about the future. Three '
             'pieces, and only the first one changes. The <span class="es">a</span> '
             'never changes.</p>')
    h.append(conj_table("Going to + verb", _c(
        "voy a…", "vas a…", "va a…", "vamos a…", "van a…")))
    h.append(box('warn', 'Careful with “to the”', (
        '<p><span class="es">a + el = al</span>. So <span class="es">Voy '
        '<strong>al</strong> gimnasio</span> — not “a el.” With feminine words '
        'it stays apart: <span class="es">Voy <strong>a la</strong> playa</span>.</p>')))
    h.append(examples([
        ("Voy a la playa este fin de semana.", "I'm going to the beach this weekend."),
        ("Voy a hacer paddleboard con Joshua.", "I'm going to paddleboard with Joshua."),
        ("Mañana voy a regar las plantas.", "Tomorrow I'm going to water the plants."),
        ("Vamos a cenar con su familia.", "We're going to have dinner with his family."),
        ("Voy al gimnasio después del trabajo.", "I'm going to the gym after work."),
        ("¿Vas a estudiar español esta noche?", "Are you going to study Spanish tonight?"),
    ]))

    # progressive
    h.append('<h2>3 · “I am ___-ing” — <span class="es">estar</span> + '
             '<span class="es">-ando/-iendo</span></h2>')
    h.append('<p>For what\'s happening <strong>right this second</strong>. Conjugate '
             '<span class="es">estar</span>, then change the second verb\'s ending: '
             '<span class="es">-ar → -ando</span>, <span class="es">-er/-ir → '
             '-iendo</span>.</p>')
    h.append(vocab_table([
        ("hablar → hablando", "talking", "-ar → -ando"),
        ("comer → comiendo", "eating", "-er → -iendo"),
        ("escribir → escribiendo", "writing", "-ir → -iendo"),
        ("leer → leyendo", "reading", "irregular"),
        ("dormir → durmiendo", "sleeping", "irregular"),
        ("decir → diciendo", "saying", "irregular"),
    ]))
    h.append(box('warn', "Don't overuse it", (
        '<p>English says “I\'m working tomorrow” for plans — Spanish does '
        '<em>not</em>. The progressive is strictly for <strong>right now</strong>. '
        'For tomorrow, use <span class="es">voy a trabajar</span>.</p>')))
    h.append(examples([
        ("Estoy aprendiendo español.", "I'm learning Spanish. (your most useful sentence!)"),
        ("Estoy cocinando arroz con pollo.", "I'm cooking chicken and rice."),
        ("Maggie está durmiendo en el sofá.", "Maggie is sleeping on the couch."),
        ("Lo estoy intentando.", "I'm trying it. (say this to yourself often!)"),
        ("Estamos caminando por la playa.", "We're walking on the beach."),
    ]))
    h.append(box('tip', 'The little word “lo” (it)', (
        '<p>It goes <strong>before</strong> <span class="es">estar</span>: '
        '<span class="es">Lo estoy aprendiendo</span> (I\'m learning it) · '
        '<span class="es">Lo estoy haciendo</span> (I\'m doing it).</p>')))

    # reflexives
    h.append('<h2>4 · Your daily routine — reflexive verbs</h2>')
    h.append('<p>Some verbs point the action back at <em>you</em> — “I wake '
             '<em>myself</em> up,” “I get <em>myself</em> dressed.” You add a '
             'small word before the verb. You already say one every day: '
             '<span class="es">¿Cómo te llamas?</span> → <span class="es">Me llamo '
             'Jenna.</span></p>')
    h.append(conj_table("levantarse → to get up", _c(
        "me levanto", "te levantas", "se levanta", "nos levantamos", "se levantan")))
    h.append('<p class="small">The little word: yo → <span class="es">me</span> · '
             'tú → <span class="es">te</span> · él/ella → <span class="es">se</span> · '
             'nosotros → <span class="es">nos</span> · ellos → <span class="es">se</span>.</p>')
    h.append(chips([("levantarse", "get up"), ("despertarse", "wake up"),
                    ("ducharse", "shower"), ("vestirse", "get dressed"),
                    ("acostarse", "go to bed"), ("sentirse", "feel"),
                    ("llamarse", "be named")]))
    h.append(examples([
        ("Me levanto a las seis, me ducho y voy al trabajo.", "I get up at six, shower, and go to work."),
        ("Me acuesto temprano cuando trabajo mucho.", "I go to bed early when I work a lot."),
        ("Mi novio se llama Joshua.", "My boyfriend's name is Joshua."),
        ("Los domingos me quedo en casa.", "On Sundays I stay home."),
    ]))

    # stem-changers
    h.append('<h2>5 · Stem-changing verbs (the “boot”)</h2>')
    h.append('<p>Some verbs change their middle vowel — but <strong>only in the '
             'present</strong>, and <strong>only in four of the five forms</strong>. '
             'Draw a line around the changed forms and you get a boot shape: '
             '<span class="es">nosotros</span> is the one left outside.</p>')
    h.append('<div style="display:flex;gap:14px;flex-wrap:wrap">')
    h.append('<div style="flex:1;min-width:210px">' + conj_table("o → ue · poder (can)", _c(
        "puedo", "puedes", "puede", "podemos", "pueden")) + '</div>')
    h.append('<div style="flex:1;min-width:210px">' + conj_table("e → ie · querer (want)", _c(
        "quiero", "quieres", "quiere", "queremos", "quieren")) + '</div>')
    h.append('</div>')
    h.append('<p class="small">See how <span class="es">podemos</span> and '
             '<span class="es">queremos</span> keep the plain vowel? That\'s '
             'nosotros standing outside the boot.</p>')
    h.append(box('trick', 'The three changes', (
        '<ul>'
        '<li><strong>o → ue:</strong> poder→puedo, dormir→duermo, volver→vuelvo, costar→cuesta</li>'
        '<li><strong>e → ie:</strong> querer→quiero, pensar→pienso, empezar→empiezo, entender→entiendo</li>'
        '<li><strong>e → i:</strong> pedir→pido, servir→sirvo, repetir→repito</li>'
        '</ul>'
        '<p><strong>Watch out</strong> for the sneaky one: <span class="es">regar '
        '→ riego</span> (to water) is a stem-changer too — “I water the plants” '
        'is <span class="es">Riego las plantas</span>, not “rego.”</p>')))
    h.append(box('tip', 'In the past, the boot disappears', (
        '<p>None of this happens in the preterite: <span class="es">volví, quise, '
        'entendí</span>. The stem goes back to normal. That\'s why the past felt '
        'easier — it is.</p>')))
    h.append(examples([
        ("Quiero aprender a cocinar comida cubana.", "I want to learn to cook Cuban food."),
        ("No puedo dormir cuando hace calor.", "I can't sleep when it's hot."),
        ("Riego las plantas todos los días.", "I water the plants every day."),
        ("Empiezo a trabajar a las nueve.", "I start work at nine."),
        ("Prefiero la playa por la mañana.", "I prefer the beach in the morning."),
    ]))
    return "".join(h)


# ─────────────────────────────────────────────────────────────────────────
# SPEAKING: the #1 habit + grow ladders + conversation cards + about you
# ─────────────────────────────────────────────────────────────────────────
def one_word_fix():
    h = []
    h.append('<h2>The one habit that changes everything</h2>')
    h.append('<p>The single most useful thing you can do isn\'t more vocabulary — '
             'it\'s two small habits that turn a one-word answer into a real '
             'sentence. Do these every time, even when it slows you down.</p>')
    h.append(box('tip', '1 · Always put the verb back in', (
        '<p>Someone asks <span class="es">¿Qué comiste?</span> — don\'t answer '
        '“pollo.” Answer <span class="es">Comí pollo.</span> One extra word turns '
        'a fragment into a sentence.</p>')))
    h.append(box('tip', '2 · Lean on <span class="es">porque</span>', (
        '<p>Any answer + <span class="es">porque</span> + a reason is instantly a '
        'real contribution — and it buys you time to think. Say '
        '<span class="es">porque</span> out loud ten times right now; when you\'re '
        'stuck mid-sentence, it\'s the handle you grab.</p>')))
    h.append('<p class="small"><strong>Connectors</strong> are the cheapest way to '
             'double your sentence length:</p>')
    h.append(chips([("y", "and"), ("pero", "but"), ("porque", "because"),
                    ("también", "also"), ("después", "then"), ("entonces", "so"),
                    ("por eso", "that's why"), ("aunque", "although")]))
    return "".join(h)


GROW = [
    ("¿Qué comiste ayer?", "What did you eat yesterday?", [
        "Pollo.", "Comí pollo.", "Ayer comí pollo.",
        "Ayer comí pollo con arroz.",
        "Ayer comí pollo con arroz porque Joshua cocinó."]),
    ("¿Cómo estás?", "How are you?", [
        "Bien.", "Estoy bien.", "Estoy bien, gracias.",
        "Estoy bien, gracias. Un poco cansada.",
        "Estoy bien, gracias. Un poco cansada porque trabajé mucho hoy."]),
    ("¿Te gusta la comida cubana?", "Do you like Cuban food?", [
        "Sí.", "Sí, me gusta.", "Sí, me gusta mucho.",
        "Sí, me gusta mucho el arroz con frijoles.",
        "Sí, me gusta mucho el arroz con frijoles, pero no cocino muy bien todavía."]),
    ("¿Qué vas a hacer mañana?", "What are you going to do tomorrow?", [
        "Trabajar.", "Voy a trabajar.", "Mañana voy a trabajar.",
        "Mañana voy a trabajar y después voy a estudiar español.",
        "Mañana voy a trabajar y después voy a estudiar español con Joshua."]),
    ("¿Adónde vas los fines de semana?", "Where do you go on weekends?", [
        "La playa.", "Voy a la playa.", "Voy a la playa los fines de semana.",
        "Voy a la playa con mi novio los fines de semana.",
        "Voy a la playa con mi novio los fines de semana porque me gusta nadar."]),
]

def grow_ladders():
    h = []
    h.append('<h2>Grow-an-answer ladders</h2>')
    h.append('<p>Start with the one-word answer, then add one piece at a time until '
             'it\'s a full, natural sentence. Say each rung out loud.</p>')
    for q, en, rungs in GROW:
        inner = [f'<p class="small">{esc(en)}</p><ol class="ex" style="list-style:decimal;margin-left:20px">']
        for r in rungs:
            inner.append(f'<li><span class="es">{esc(r)}</span></li>')
        inner.append('</ol>')
        h.append(drill(q, "".join(inner)))
    return "".join(h)


CARDS = [
    ("Quién eres — ser, estar, tener", [
        ("¿Cómo te llamas?", "Me llamo Jenna."),
        ("¿De dónde eres?", "Soy de Massachusetts, pero vivo en Florida."),
        ("¿Dónde estás ahora?", "Estoy en casa, en Boynton Beach."),
        ("¿Cuántos años tienes?", "Tengo treinta y tres años."),
        ("¿Tienes mascotas?", "Sí, tengo una perra. Se llama Maggie."),
        ("¿Quién eres?", "Soy Jenna. Soy de Massachusetts y estoy aprendiendo español."),
        ("¿Cómo estás hoy?", "Estoy bien, gracias. Un poco cansada, pero contenta."),
        ("¿Cómo está tu familia?", "Está muy bien, gracias."),
        ("¿Dónde está tu perra?", "Está en la casa, durmiendo en el sofá."),
        ("¿Qué tienes en tu bolso?", "Tengo mi teléfono, mis llaves y agua."),
    ]),
    ("Qué haces — ir, hacer, querer, poder, salir", [
        ("¿Adónde vas los fines de semana?", "Voy a la playa casi todos los fines de semana."),
        ("¿Con quién vas a la playa?", "Voy con mi novio y con Maggie."),
        ("¿Qué haces después del trabajo?", "Hago ejercicio en el gimnasio y después camino con mi perra."),
        ("¿Qué haces los domingos?", "Hago jardinería. Riego las plantas y cuido las flores."),
        ("¿Qué quieres hacer este fin de semana?", "Quiero ir a la playa y hacer paddleboard."),
        ("¿Puedes nadar?", "Sí, puedo nadar bien."),
        ("¿Puedes hablar español?", "Puedo hablar un poco, pero todavía estoy aprendiendo."),
        ("¿A qué hora sales del trabajo?", "Salgo a las cinco."),
        ("¿Haces ejercicio todos los días?", "Hago ejercicio casi todos los días."),
        ("¿Qué música escuchas?", "Escucho música latina. Me gusta bailar."),
    ]),
    ("Todo lo demás — decir, ver, venir, poner, saber, conocer", [
        ("¿Qué dices cuando conoces a alguien?", "Digo “Mucho gusto.”"),
        ("¿Qué ves desde tu ventana?", "Veo palmeras y el jardín."),
        ("¿Vienes aquí todos los días?", "No, vengo tres veces por semana."),
        ("¿Dónde pones las llaves?", "Pongo las llaves en la mesa."),
        ("¿Qué sabes cocinar?", "Sé cocinar pasta. Quiero aprender a cocinar comida cubana."),
        ("¿Conoces Miami?", "Sí, conozco Miami."),
        ("¿Conoces a la familia de tu novio?", "Sí, los conozco. Son de Cuba y de Colombia."),
        ("¿Qué quieres comer hoy?", "Quiero arroz con pollo."),
        ("¿Qué quieres aprender?", "Quiero aprender español para hablar con su familia."),
        ("¿Qué hiciste ayer?", "Ayer trabajé, hice ejercicio y caminé con Maggie."),
    ]),
]

def conversation_cards():
    h = []
    h.append('<h2>Your 30 conversation cards</h2>')
    h.append('<p>These are <strong>your</strong> real questions with <strong>your</strong> '
             'real answers. Cover the answer, ask yourself the question out loud, then '
             'check. Tap any answer in the app to hear it.</p>')
    for deck, pairs in CARDS:
        rows = [(q, a, "") for q, a in pairs]
        h.append(f'<h3>{esc(deck)}</h3>')
        out = ['<table class="vocab"><thead><tr><th>Pregunta</th>'
               '<th>Tu respuesta</th></tr></thead><tbody>']
        for q, a in pairs:
            out.append(f'<tr><td>{esc(q)}</td>'
                       f'<td><span class="es">{esc(a)}</span></td></tr>')
        out.append('</tbody></table>')
        h.append("".join(out))
    return "".join(h)


def about_you():
    h = []
    h.append('<h2>Your about-you script</h2>')
    h.append('<p>Rehearse this out loud until it\'s automatic. When Joshua\'s family '
             'asks, you\'ll be ready. Tap any line in the app to hear it.</p>')
    h.append(box('', 'Preséntate — introduce yourself', (
        '<p class="es" style="font-size:16.5px">Hola, me llamo Jenna. Soy de '
        'Massachusetts, pero vivo en Florida. Tengo una perra que se llama Maggie. '
        'Me gusta la playa, la jardinería, la música y hacer paddleboard. También '
        'hago ejercicio casi todos los días. Estoy aprendiendo español porque quiero '
        'hablar con mi novio y con su familia. Su familia es de Cuba y de Colombia. '
        'No hablo muy bien todavía, pero puedo entender un poco.</p>'
        '<p class="en small" style="margin-top:8px">Hi, my name is Jenna. I\'m from '
        'Massachusetts, but I live in Florida. I have a dog named Maggie. I like the '
        'beach, gardening, music, and paddleboarding. I also exercise almost every '
        'day. I\'m learning Spanish because I want to talk with my boyfriend and his '
        'family. His family is from Cuba and Colombia. I don\'t speak very well yet, '
        'but I can understand a little.</p>')))
    h.append(box('tip', 'Four sentences that carry any family dinner', chips([
        ("Estoy aprendiendo español.", "I'm learning Spanish."),
        ("Más despacio, por favor.", "Slower, please."),
        ("¿Cómo se dice eso?", "How do you say that?"),
        ("Entendí un poco.", "I understood a little."),
    ]) + '<p class="small">Nobody expects fluency. They notice that you\'re trying — '
         'and that\'s the part that matters to them.</p>'))
    return "".join(h)
