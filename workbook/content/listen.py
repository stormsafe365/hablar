# -*- coding: utf-8 -*-
"""Listen — ear training with a speed dial.

Three levels: single words (multiple choice), phrases (multiple choice),
and full sentences (type what you hear). Level 1 deliberately pairs
near-twins (comí/comió, hablo/habló, perro/pero) because hearing the
stressed syllable is the whole game. Audio is the phone's Spanish voice
at a speed the learner controls (55%–100%)."""
import random
from .theme import esc

# (correct answer, distractors, english gloss shown after answering)
LEVEL1 = [
    ("ayer", ["mañana", "ahora"], "yesterday"),
    ("comí", ["comió", "comemos"], "I ate — the í is stressed"),
    ("habló", ["hablo", "hablan"], "he talked — hear the final Ó (past!)"),
    ("hablamos", ["hablaron", "hablaste"], "we talk / we talked"),
    ("la abuela", ["la escuela", "la abeja"], "the grandmother"),
    ("trabajé", ["trabajó", "trabajas"], "I worked"),
    ("volvieron", ["volvimos", "volviste"], "they came back"),
    ("quiero", ["quiere", "quieren"], "I want"),
    ("cansada", ["casada", "enojada"], "tired — not casada (married)!"),
    ("perro", ["pero", "pera"], "dog — the rolled RR"),
    ("tiene", ["tienen", "tenemos"], "he/she has"),
    ("vamos", ["van", "va"], "we go / let's go"),
]

LEVEL2 = [
    ("¿Cómo estás?", ["¿Cómo te llamas?", "¿Dónde estás?"], "How are you?"),
    ("Estoy un poco cansada.", ["Estoy muy ocupada.", "Estoy en la casa."], "I'm a little tired."),
    ("¿Qué comiste anoche?", ["¿Qué comes ahora?", "¿Con quién comiste?"], "What did you eat last night?"),
    ("Más despacio, por favor.", ["Muchas gracias, señora.", "Más tarde, por favor."], "Slower, please."),
    ("No entendí muy bien.", ["No entiendo nada.", "No hablé con ella."], "I didn't understand very well."),
    ("¿Qué bolá, asere?", ["¿Qué pasa, amigo?", "¿Qué hora es?"], "What's up, buddy? (Cuban!)"),
    ("Tengo ganas de bailar.", ["Tengo ganas de comer.", "Tengo que trabajar."], "I feel like dancing."),
    ("Nos vemos mañana.", ["Nos vemos el lunes.", "Te veo ahora."], "See you tomorrow."),
]

LEVEL3 = [
    ("Ayer cociné arroz con pollo.", "Yesterday I cooked chicken and rice."),
    ("Mi novio se llama Joshua.", "My boyfriend's name is Joshua."),
    ("Estoy aprendiendo español porque su familia es de Cuba.",
     "I'm learning Spanish because his family is from Cuba."),
    ("Anoche hablamos con su abuela por teléfono.",
     "Last night we talked with his grandmother on the phone."),
    ("Los domingos comemos con su familia.", "On Sundays we eat with his family."),
    ("Maggie está durmiendo en el sofá.", "Maggie is sleeping on the couch."),
    ("Voy a la playa con mi novio este fin de semana.",
     "I'm going to the beach with my boyfriend this weekend."),
    ("Mañana voy a estudiar los verbos otra vez.",
     "Tomorrow I'm going to study the verbs again."),
]

_rng = random.Random(42)


def _mc_item(sec, correct, distractors, gloss):
    opts = [(correct, 1)] + [(d, 0) for d in distractors]
    _rng.shuffle(opts)
    btns = "".join(
        f'<button type="button" class="lopt" data-ok="{ok}">{esc(o)}</button>'
        for o, ok in opts)
    return (f'<div class="lq" data-sec="{sec}">'
            f'<button type="button" class="lplay" data-es="{esc(correct)}" '
            f'aria-label="Play">&#9654;</button>'
            f'<div class="lbody"><div class="lopts">{btns}</div>'
            f'<div class="len small">{esc(gloss)}</div></div></div>')


def build_tab():
    h = []
    h.append('<div class="eyebrow">Listen · entrena el oído</div>')
    h.append('<h1>Train your ear</h1>')
    h.append('<p class="muted">Cuban Spanish moves fast — this is where you '
             'get ready for it. Tap ▶, <strong>don\'t peek at the options '
             'first</strong>, and choose what you heard. Start slow with the '
             'dial, then push the speed up over time. Full speed is the real '
             'target.</p>')

    h.append('<div class="ldial"><span class="small">Speed</span>'
             '<input type="range" id="lrate" min="55" max="100" step="5" value="80">'
             '<span class="lrateval" id="lrateval">80%</span></div>')

    h.append('<div class="box tip"><span class="lead">How to use this</span>'
             '<p>Play it once. Try to catch <em>one</em> word you know. Play '
             'it again, then answer. When you miss one, replay it <em>after</em> '
             'seeing the answer — that\'s when your ear learns. The green '
             'answers speak when you get them right.</p></div>')

    h.append('<h2>Level 1 · One word <span class="lscore" id="lscore-l1"></span></h2>')
    h.append('<p class="small">These are near-twins on purpose — '
             '<span class="es">comí</span> vs <span class="es">comió</span> is '
             'the past tense hiding in one vowel.</p>')
    for c, d, g in LEVEL1:
        h.append(_mc_item("l1", c, d, g))

    h.append('<h2>Level 2 · Phrases <span class="lscore" id="lscore-l2"></span></h2>')
    for c, d, g in LEVEL2:
        h.append(_mc_item("l2", c, d, g))

    h.append('<h2>Level 3 · Type what you hear</h2>')
    h.append('<p class="small">The big leagues. Accents count as “almost” '
             '(gold) — spelling counts. Tap “Translation” after you answer.</p>')
    for es_, en_ in LEVEL3:
        h.append(
            '<div class="lq ltype">'
            f'<button type="button" class="lplay" data-es="{esc(es_)}" '
            'aria-label="Play">&#9654;</button>'
            '<div class="lbody">'
            f'<span class="blank" data-ans="{esc(es_)}" style="min-width:230px"></span>'
            f'<div class="rev"><button class="rev-btn" data-es="{esc(es_)}">Translation</button>'
            f'<span class="rev-ans">{esc(en_)}</span></div>'
            '</div></div>')

    h.append('<div class="box sea"><span class="lead">Leveling up</span>'
             '<p>When Level 3 feels easy at 100%, you\'re ready for the real '
             'thing: Cuban YouTube and Joshua\'s family dinners. Remember the '
             'rescue phrase: <span class="es">Más despacio, por favor.</span></p></div>')
    return "".join(h)
