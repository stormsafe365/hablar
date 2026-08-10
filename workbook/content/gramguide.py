# -*- coding: utf-8 -*-
"""Grammar Guide — a card grid of ~20 topics; each opens a slide-up sheet
with a plain-English explanation, a table, tap-to-hear examples, and
tap-to-check practice. Personalized to Jenna (Cuban & Colombian Spanish,
no vosotros)."""
from .theme import esc, examples

def _gtable(headers, rows):
    out = ['<table class="vocab"><thead><tr>']
    out += [f'<th>{esc(h)}</th>' for h in headers]
    out.append('</tr></thead><tbody>')
    for r in rows:
        out.append('<tr>' + "".join(
            f'<td>{c}</td>' for c in r) + '</tr>')
    out.append('</tbody></table>')
    return "".join(out)

def _es(w):
    return f'<span class="es">{esc(w)}</span>'

def _rev(q, a):
    return (f'<div class="rev"><span class="rev-q">{q}</span>'
            f'<button class="rev-btn" data-es="{esc(a)}">Show</button>'
            f'<span class="rev-ans">{esc(a)}</span></div>')

# chips: (word, color-class a=salmon s=mint g=gold)
TOPICS = [
{
 "t": "Personal pronouns", "d": "Who's doing the verb — yo, tú, él, nosotros…",
 "chips": [("yo","a"),("nosotros","s"),("ellas","g")],
 "body": (
   '<p>These are the words for <b>who does the action</b>. Good news: Spanish '
   'usually <b>drops them</b> — the verb ending already says who. Keep them '
   'for emphasis or contrast.</p>'
   + _gtable(["Spanish","English"],[
     [_es("yo"),"I"],[_es("tú"),"you (friends & family)"],
     [_es("él / ella"),"he / she"],
     [_es("usted"),"you, polite — Colombia's favorite, even with family"],
     [_es("nosotros / nosotras"),"we"],
     [_es("ellos / ellas"),"they"],
     [_es("ustedes"),"you all (never vosotros here)"]])),
 "ex": [("Yo soy de Massachusetts y él es de Cuba.","I'm from Massachusetts and he's from Cuba. (contrast — keep the pronouns)"),
        ("Hablo un poco de español.","I speak a little Spanish. (no 'yo' needed)"),
        ("¿Y tú?","And you?")],
 "pr": [("“we” (you and Joshua)","nosotros"),
        ("you — polite, the Colombian default","usted"),
        ("they (all women)","ellas")],
},
{
 "t": "Definite articles", "d": "How to use el, la, los, las — “the.”",
 "chips": [("el","s"),("la","s"),("los","g")],
 "body": (
   '<p>“The” has four forms, matching the noun\'s gender and number. '
   'The habit: words ending in <b>-o</b> usually take '+_es("el")+', words in '
   '<b>-a</b> usually take '+_es("la")+'.</p>'
   + _gtable(["Article","Used for","Example"],[
     [_es("el"),"masculine, one",_es("el jardín")],
     [_es("la"),"feminine, one",_es("la playa")],
     [_es("los"),"masculine, plural",_es("los perros")],
     [_es("las"),"feminine, plural",_es("las olas")]])
   + '<p class="small">A few rebels to memorize: '+_es("el día")+', '
     +_es("la mano")+', '+_es("el problema")+'.</p>'),
 "ex": [("La playa está tranquila hoy.","The beach is calm today."),
        ("Los perros corren en la arena.","The dogs run in the sand."),
        ("El café está caliente.","The coffee is hot.")],
 "pr": [("___ playa","la"),("___ problema (sneaky one)","el"),("___ flores","las")],
},
{
 "t": "Indefinite articles", "d": "un, una, unos, unas — “a / an / some.”",
 "chips": [("un","s"),("una","s"),("unos","g")],
 "body": (
   '<p>Same idea as el/la, but for “a” and “some.”</p>'
   + _gtable(["Article","Used for","Example"],[
     [_es("un"),"a (masculine)",_es("un cafecito")],
     [_es("una"),"a (feminine)",_es("una perra")],
     [_es("unos"),"some (masculine)",_es("unos mangos")],
     [_es("unas"),"some (feminine)",_es("unas flores")]])),
 "ex": [("Tengo una perra que se llama Maggie.","I have a dog named Maggie."),
        ("¿Me das un cafecito?","Will you give me a little coffee?"),
        ("Compramos unas flores para el jardín.","We bought some flowers for the garden.")],
 "pr": [("___ perro","un"),("___ casa","una"),("some mangos: ___ mangos","unos")],
},
{
 "t": "Nouns: gender & number", "d": "Singular, plural, masculine, feminine.",
 "chips": [("el","g"),("las","a"),("-os","s")],
 "body": (
   '<p>Every noun is masculine or feminine. Ends in <b>-o</b> → usually '
   'masculine; ends in <b>-a</b> → usually feminine. Plurals are easy: add '
   '<b>-s</b> after a vowel, <b>-es</b> after a consonant.</p>'
   + _gtable(["Singular","Plural"],[
     [_es("el perro"),_es("los perros")],
     [_es("la playa"),_es("las playas")],
     [_es("la flor"),_es("las flores")],
     [_es("el mes"),_es("los meses")]])),
 "ex": [("Las palmeras son altas.","The palm trees are tall."),
        ("El mar es azul.","The sea is blue."),
        ("Las flores del jardín son coloridas.","The garden flowers are colorful.")],
 "pr": [("plural of la flor","las flores"),
        ("plural of el mes","los meses"),
        ("el or la? ___ mano","la mano")],
},
{
 "t": "Adjectives", "d": "They follow the noun and match it.",
 "chips": [("cansada","a"),("grande","s"),("cubana","g")],
 "body": (
   '<p>Two differences from English: adjectives go <b>after</b> the noun '
   '(“the dog black”), and they <b>match</b> the noun\'s gender and '
   'number.</p>'
   '<p><b>This is why you say '+_es("cansada")+'.</b> You\'re describing '
   'yourself, so it ends in -a. Joshua would say '+_es("cansado")+'. Same '
   'for '+_es("lista")+', '+_es("ocupada")+', '+_es("nerviosa")+'. '
   'Words like '+_es("feliz")+' and '+_es("grande")+' don\'t change.</p>'),
 "ex": [("Estoy cansada pero contenta.","I'm tired but happy. (you, feminine)"),
        ("Maggie es una perra cariñosa.","Maggie is an affectionate dog."),
        ("Una familia cubana y colombiana.","A Cuban and Colombian family.")],
 "pr": [("(you, f) tired","cansada"),
        ("the black dog (Maggie): la perra ___","negra"),
        ("(you, f) ready","lista")],
},
{
 "t": "Possessive adjectives", "d": "mi, tu, su — whose is it?",
 "chips": [("mi","s"),("tu","s"),("su","g")],
 "body": (
   _gtable(["Spanish","English"],[
     [_es("mi / mis"),"my"],[_es("tu / tus"),"your"],
     [_es("su / sus"),"his · her · their · your (usted)"],
     [_es("nuestro / nuestra"),"our"]])
   + '<p><b>No apostrophe-s in Spanish.</b> “Joshua\'s mom” is '
   + _es("la mamá de Joshua") + ' — literally “the mom of Joshua.”</p>'),
 "ex": [("Mi perra se llama Maggie.","My dog is named Maggie."),
        ("Su familia es de Cuba y de Colombia.","His family is from Cuba and Colombia."),
        ("La casa de su abuela.","His grandmother's house.")],
 "pr": [("my dog: ___ perra","mi"),
        ("Joshua's mom","la mamá de Joshua"),
        ("our house: ___ casa","nuestra")],
},
{
 "id": "demostrativos",
 "t": "Demonstrative adjectives", "d": "este, ese, aquel — this, that, that over there.",
 "chips": [("este","s"),("ese","s"),("aquel","g")],
 "body": (
   '<p>These point at things — and Spanish sorts them by <b>how far away</b> '
   'the thing is from you. They match the noun\'s gender and number, just '
   'like adjectives.</p>'
   + _gtable(["Distance","Singular (m/f)","Plural (m/f)"],[
     ["<b>Short</b> — within reach",
      _es("este / esta")+"<br><span class='small'>this</span>",
      _es("estos / estas")+"<br><span class='small'>these</span>"],
     ["<b>Medium</b> — visible, same area",
      _es("ese / esa")+"<br><span class='small'>that</span>",
      _es("esos / esas")+"<br><span class='small'>those</span>"],
     ["<b>Long</b> — further or far away",
      _es("aquel / aquella")+"<br><span class='small'>that over there</span>",
      _es("aquellos / aquellas")+"<br><span class='small'>those over there</span>"]])
   + '<p><b>The memory trick:</b> this & these have the T\'s ('+_es("este, estos")
   +') — that & those don\'t ('+_es("ese, esos")+'). And '+_es("aquel")
   +' is for “waaay over there.” The distance can be physical or in time: '
   +_es("aquellos días")+' — those (long-ago) days.</p>'),
 "ex": [("Me encanta esta playa.","I love this beach. (you're standing on it)"),
        ("¿Ves ese barco?","Do you see that boat? (visible, a bit away)"),
        ("Aquella casa es de su abuela.","That house over there is his grandma's."),
        ("Estas flores son del jardín.","These flowers are from the garden."),
        ("Esos tostones están ricos.","Those tostones are delicious.")],
 "pr": [("this beach","esta playa"),
        ("that dog (visible, over there a bit)","ese perro"),
        ("these flowers","estas flores"),
        ("that house waaay over there","aquella casa")],
},
{
 "t": "The verb “ser”", "d": "To be — who or what something IS.",
 "chips": [("soy","a"),("eres","a"),("es","g")],
 "body": (
   '<p>'+_es("Ser")+' is “to be” for <b>identity</b>: who you are, where '
   'you\'re from, what you\'re like, what time it is.</p>'
   + _gtable(["Who","Form"],[
     ["yo",_es("soy")],["tú",_es("eres")],["él / ella / usted",_es("es")],
     ["nosotros",_es("somos")],["ellos / ustedes",_es("son")]])),
 "ex": [("Soy Jenna. Soy de Massachusetts.","I'm Jenna. I'm from Massachusetts."),
        ("Joshua es cubano.","Joshua is Cuban."),
        ("Son las ocho.","It's eight o'clock.")],
 "pr": [("yo ___ de Massachusetts","soy"),
        ("ellos ___ de Colombia","son"),
        ("hoy ___ lunes","es")],
},
{
 "t": "The verb “estar”", "d": "To be — how and where you are right now.",
 "chips": [("estoy","a"),("estás","a"),("están","g")],
 "body": (
   '<p>'+_es("Estar")+' is “to be” for <b>situations</b>: feelings, '
   'conditions, location — things that could be different tomorrow. It\'s '
   'also the “I am ___-ing” verb.</p>'
   + _gtable(["Who","Form"],[
     ["yo",_es("estoy")],["tú",_es("estás")],["él / ella / usted",_es("está")],
     ["nosotros",_es("estamos")],["ellos / ustedes",_es("están")]])),
 "ex": [("Estoy cansada pero contenta.","I'm tired but happy."),
        ("Maggie está en el sofá.","Maggie is on the couch."),
        ("¿Cómo estás?","How are you?")],
 "pr": [("yo ___ en casa","estoy"),
        ("¿cómo ___ tú?","estás"),
        ("nosotros ___ bien","estamos")],
},
{
 "id": "servsestar",
 "t": "“Ser” vs. “estar”", "d": "The two “to be”s — identity vs. situation.",
 "chips": [("soy","a"),("estoy","s"),("cansada","g")],
 "body": (
   '<p>The memory hook: <b>ser = identity, estar = situation.</b> If you '
   'could put “currently” in front of the English, use '+_es("estar")+'.</p>'
   + _gtable(["SER — what it is","ESTAR — how it's doing"],[
     ["who you are","feelings right now"],
     ["where you're from","where something is"],
     ["what it's like (always)","conditions (today)"],
     ["time & dates","the -ing form"]])
   + '<p>The pair that shows it best: '+_es("Ella es aburrida")+' = she\'s '
   'boring (personality). '+_es("Ella está aburrida")+' = she\'s bored '
   '(right now).</p>'),
 "ex": [("Soy de Massachusetts, pero estoy en Florida.","I'm from Massachusetts, but I'm in Florida."),
        ("El café cubano es dulce; este café está frío.","Cuban coffee is sweet (always); this coffee is cold (right now)."),
        ("Joshua es mi novio y está en el gimnasio.","Joshua is my boyfriend and he's at the gym.")],
 "pr": [("yo ___ americana (ser/estar)","soy"),
        ("el café ___ frío hoy","está"),
        ("Joshua ___ mi novio","es")],
},
{
 "id": "present",
 "t": "Regular verbs (present)", "d": "Chop the ending, add the new one.",
 "chips": [("hablo","a"),("comes","a"),("vivimos","g")],
 "body": (
   '<p>Cut the <b>-ar / -er / -ir</b>, add these. The <b>yo</b> form always '
   'ends in <b>-o</b>.</p>'
   + _gtable(["Who","-AR (hablar)","-ER (comer)","-IR (vivir)"],[
     ["yo",_es("hablo"),_es("como"),_es("vivo")],
     ["tú",_es("hablas"),_es("comes"),_es("vives")],
     ["él / ella",_es("habla"),_es("come"),_es("vive")],
     ["nosotros",_es("hablamos"),_es("comemos"),_es("vivimos")],
     ["ellos / uds.",_es("hablan"),_es("comen"),_es("viven")]])
   + '<p class="small">-ER and -IR differ in exactly one spot: nosotros '
   '(comemos vs vivimos). That\'s the only difference.</p>'),
 "ex": [("Camino con Maggie todos los días.","I walk with Maggie every day."),
        ("Vivo en Boynton Beach.","I live in Boynton Beach."),
        ("Comemos con su familia los domingos.","We eat with his family on Sundays.")],
 "pr": [("yo (hablar)","hablo"),("nosotros (comer)","comemos"),
        ("ellos (vivir)","viven")],
},
{
 "t": "Some irregular verbs", "d": "The five kings + the “-go gang.”",
 "chips": [("tengo","a"),("hago","a"),("voy","g")],
 "body": (
   '<p>Five verbs refuse the pattern and you\'ll use them a hundred times a '
   'day — learn them as whole words: '+_es("ser")+', '+_es("estar")+', '
   +_es("tener")+', '+_es("ir")+', '+_es("hacer")+'.</p>'
   '<p><b>The -go gang:</b> six verbs are only weird in the yo form, and '
   'they all end in -go. Say them out loud twice a day: '
   +_es("tengo")+' · '+_es("hago")+' · '+_es("vengo")+' · '
   +_es("pongo")+' · '+_es("salgo")+' · '+_es("digo")+'</p>'
   '<p class="small">Tap any of the 16 core verbs elsewhere in the app for '
   'its full breakdown with all tenses.</p>'),
 "ex": [("Tengo una perra y hago ejercicio casi todos los días.","I have a dog and I exercise almost every day."),
        ("Salgo del trabajo a las cinco y voy a la playa.","I leave work at five and go to the beach."),
        ("Digo “mucho gusto” cuando conozco a alguien.","I say “nice to meet you” when I meet someone.")],
 "pr": [("yo (hacer)","hago"),("yo (salir)","salgo"),("yo (ir)","voy")],
},
{
 "id": "boot",
 "t": "Stem-changing verbs", "d": "The “boot” — the middle vowel shifts.",
 "chips": [("puedo","a"),("quiero","a"),("riego","g")],
 "body": (
   '<p>Some verbs change their middle vowel — but <b>only in the present</b>, '
   'and <b>nosotros never changes</b> (it stands outside the boot).</p>'
   + _gtable(["Change","Verbs"],[
     ["o → ue",_es("poder → puedo")+" · "+_es("dormir → duermo")+" · "+_es("volver → vuelvo")],
     ["e → ie",_es("querer → quiero")+" · "+_es("pensar → pienso")+" · "+_es("empezar → empiezo")],
     ["e → i",_es("pedir → pido")+" · "+_es("servir → sirvo")+" · "+_es("repetir → repito")]])
   + '<p><b>The sneaky one:</b> '+_es("regar → riego")+' — “I water the '
   'plants” is '+_es("riego las plantas")+', not “rego.” And in the past, '
   'the boot disappears: '+_es("volví, quise, entendí")+'.</p>'),
 "ex": [("Quiero aprender a cocinar comida cubana.","I want to learn to cook Cuban food."),
        ("No puedo dormir cuando hace calor.","I can't sleep when it's hot."),
        ("Riego las plantas todos los días.","I water the plants every day.")],
 "pr": [("yo (poder)","puedo"),("nosotros (poder) — outside the boot","podemos"),
        ("yo (regar)","riego")],
},
{
 "id": "reflexivos",
 "t": "Reflexive verbs", "d": "Actions you do to yourself — me levanto.",
 "chips": [("me","a"),("ducho","a"),("se","g")],
 "body": (
   '<p>Verbs ending in <b>-se</b> point the action back at you. Conjugate '
   'normally, and put a little word in front. You already use one daily: '
   +_es("¿Cómo te llamas?")+' → '+_es("Me llamo Jenna.")+'</p>'
   + _gtable(["Who","Little word","levantarse (get up)"],[
     ["yo",_es("me"),_es("me levanto")],
     ["tú",_es("te"),_es("te levantas")],
     ["él / ella / usted",_es("se"),_es("se levanta")],
     ["nosotros",_es("nos"),_es("nos levantamos")],
     ["ellos / ustedes",_es("se"),_es("se levantan")]])),
 "ex": [("Me levanto a las seis y me ducho.","I get up at six and shower."),
        ("Mi novio se llama Joshua.","My boyfriend's name is Joshua."),
        ("Me acuesto temprano cuando trabajo mucho.","I go to bed early when I work a lot.")],
 "pr": [("yo (ducharse)","me ducho"),("él (llamarse)","se llama"),
        ("yo (levantarse)","me levanto")],
},
{
 "t": "Negation", "d": "How to say no — and the double negative.",
 "chips": [("no","g"),("nada","a"),("nunca","s")],
 "body": (
   '<p>Put '+_es("no")+' <b>directly before the verb</b>. Every time, no '
   'exceptions. With two verbs, before the first: '
   +_es("No quiero salir.")+'</p>'
   '<p><b>Double negatives are correct in Spanish</b> — required, even: '
   +_es("No comí nada")+' (“I didn\'t eat nothing”) · '
   +_es("No conozco a nadie")+' · '+_es("No voy nunca")+'.</p>'),
 "ex": [("No tengo tiempo hoy.","I don't have time today."),
        ("No hablo español muy bien todavía.","I don't speak Spanish very well yet."),
        ("No comí nada esta mañana.","I didn't eat anything this morning.")],
 "pr": [("make it negative: Hablo español","No hablo español"),
        ("“I ate nothing”","No comí nada"),
        ("make it negative: Trabajo hoy","No trabajo hoy")],
},
{
 "t": "Question words", "d": "qué, dónde, cuándo — and their accents.",
 "chips": [("qué","g"),("dónde","g"),("cómo","a")],
 "body": (
   _gtable(["Spanish","English"],[
     [_es("¿Qué?"),"What?"],[_es("¿Quién?"),"Who?"],
     [_es("¿Cuándo?"),"When?"],[_es("¿Dónde?"),"Where (is it)?"],
     [_es("¿Adónde?"),"Where to? (with ir)"],[_es("¿Por qué?"),"Why?"],
     [_es("¿Cómo?"),"How?"],[_es("¿Cuánto?"),"How much?"]])
   + '<p><b>Every question word wears an accent.</b> And the pair to know: '
   +_es("¿Por qué?")+' (two words) asks why — '+_es("porque")+' (one word) '
   'answers it.</p>'),
 "ex": [("¿Dónde trabajas?","Where do you work?"),
        ("¿Adónde vas?","Where are you going?"),
        ("—¿Por qué estudias español? —Porque mi novio es cubano.","—Why do you study Spanish? —Because my boyfriend is Cuban.")],
 "pr": [("where to? (with ir)","adónde"),("why?","por qué"),
        ("because","porque")],
},
{
 "id": "preterite",
 "t": "The past (preterite)", "d": "Done and finished — ayer, anoche…",
 "chips": [("ayer","g"),("comí","a"),("fui","s")],
 "body": (
   '<p>The preterite is for things that <b>happened and finished</b>: '
   +_es("Ayer comí")+' — yesterday I ate. If you hear '+_es("ayer")+
   ' (yesterday), '+_es("anoche")+' (last night), or '
   +_es("la semana pasada")+' (last week), you\'re in the past.</p>'
   + _gtable(["Who","-AR (hablar)","-ER/-IR (comer)"],[
     ["yo",_es("hablé"),_es("comí")],
     ["tú",_es("hablaste"),_es("comiste")],
     ["él / ella",_es("habló"),_es("comió")],
     ["nosotros",_es("hablamos"),_es("comimos")],
     ["ellos / uds.",_es("hablaron"),_es("comieron")]])
   + '<p><b>The accent IS the tense:</b> '+_es("hablo")+' = I talk (now) but '
   +_es("habló")+' = he talked (past). Punch that last syllable.</p>'
   '<p class="small">The common irregulars come as whole words — '
   +_es("fui")+' (I went / I was — ser and ir share it!), '+_es("tuve")+', '
   +_es("hice")+', '+_es("estuve")+'. Tap any verb card for its own past '
   'table.</p>'),
 "ex": [("Ayer fui a la playa con Maggie.","Yesterday I went to the beach with Maggie."),
        ("Anoche comí arroz con pollo en casa de su mamá.","Last night I ate chicken and rice at his mom's house."),
        ("Joshua cocinó el domingo.","Joshua cooked on Sunday.")],
 "pr": [("yo (hablar), yesterday","hablé"),
        ("yo (ir), yesterday","fui"),
        ("nosotros (comer)","comimos")],
},
{
 "id": "futuro",
 "t": "The one-word future", "d": "iré, seré, tendré — “will.”",
 "chips": [("iré","a"),("será","s"),("tendré","g")],
 "body": (
   '<p>This is the “will” future — and it\'s the <b>easiest tense in '
   'Spanish</b>. Don\'t chop anything: take the <b>whole verb</b> and add '
   'one set of endings. The same endings work for every single verb.</p>'
   + _gtable(["Who","hablar → will speak","ir → will go"],[
     ["yo",_es("hablaré"),_es("iré")],
     ["tú",_es("hablarás"),_es("irás")],
     ["él / ella",_es("hablará"),_es("irá")],
     ["nosotros",_es("hablaremos"),_es("iremos")],
     ["ellos / uds.",_es("hablarán"),_es("irán")]])
   + '<p class="small">A few verbs squish their stem first: '
   +_es("tendré")+' · '+_es("haré")+' · '+_es("diré")+' · '+_es("pondré")
   +' · '+_es("saldré")+' · '+_es("vendré")+' · '+_es("podré")+' · '
   +_es("sabré")+' · '+_es("querré")+'. Same endings, though.</p>'
   '<p><b>When do you use it?</b> Mostly you\'ll <em>hear</em> it — in '
   'conversation people say '+_es("voy a + verb")+'. Learn this one to '
   'recognize the future when Joshua\'s family talks about '
   +_es("algún día")+' — someday.</p>'),
 "ex": [("Mañana hablaré con su abuela.","Tomorrow I'll talk with his grandma."),
        ("Algún día iremos a Cuba.","Someday we'll go to Cuba."),
        ("Aprenderé español, poco a poco.","I'll learn Spanish, little by little.")],
 "pr": [("I will eat","comeré"),
        ("we will go","iremos"),
        ("I will have","tendré")],
},
{
 "id": "continuo",
 "t": "The “presente continuo”", "d": "I am ___-ing, right this second.",
 "chips": [("estoy","a"),("comiendo","a"),("hablando","g")],
 "body": (
   '<p>For what\'s happening <b>right now</b>: conjugate '+_es("estar")+', '
   'then swap the second verb\'s ending — <b>-ar → -ando</b>, '
   '<b>-er/-ir → -iendo</b>.</p>'
   '<p class="small">Irregular ones: '+_es("leyendo")+' · '
   +_es("durmiendo")+' · '+_es("diciendo")+' · '+_es("yendo")+'. '
   'And “it” goes before estar: '+_es("Lo estoy intentando.")+'</p>'
   '<p><b>Don\'t overuse it</b> — for plans, use '+_es("voy a")+': '
   'tomorrow is '+_es("voy a trabajar")+', not “estoy trabajando '
   'mañana.”</p>'),
 "ex": [("Estoy aprendiendo español.","I'm learning Spanish — your most useful sentence."),
        ("Maggie está durmiendo en el sofá.","Maggie is sleeping on the couch."),
        ("Lo estoy intentando.","I'm trying it.")],
 "pr": [("I'm cooking","estoy cocinando"),
        ("I'm learning it","lo estoy aprendiendo"),
        ("Maggie is sleeping","está durmiendo")],
},
{
 "id": "nearfut",
 "t": "The near future", "d": "voy a + verb — how people really talk.",
 "chips": [("voy","a"),("a","g"),("nadar","a")],
 "body": (
   '<p>The everyday future: a form of '+_es("ir")+' + '+_es("a")+' + the '
   'plain verb. Only the first word changes: '+_es("voy a comer")+', '
   +_es("vamos a salir")+', '+_es("va a llover")+'.</p>'
   '<p><b>Careful with “to the”:</b> '+_es("a + el = al")+' — so '
   +_es("voy al gimnasio")+', but '+_es("voy a la playa")+'.</p>'),
 "ex": [("Voy a la playa este fin de semana.","I'm going to the beach this weekend."),
        ("Mañana voy a regar las plantas.","Tomorrow I'm going to water the plants."),
        ("Vamos a cenar con su familia.","We're going to have dinner with his family.")],
 "pr": [("I'm going to swim","voy a nadar"),
        ("to the gym: voy ___ gimnasio","al"),
        ("we're going to eat","vamos a comer")],
},
{
 "t": "The verb “haber” (hay)", "d": "There is / there are — one little word.",
 "chips": [("hay","a"),("mucha","s"),("gente","s")],
 "body": (
   '<p>'+_es("Hay")+' means both “there is” and “there are” — same word, '
   'no matter how many. Negative: '+_es("no hay")+'. Question: just add '
   'the marks: '+_es("¿Hay café?")+'</p>'),
 "ex": [("Hay mucha gente en la playa hoy.","There are a lot of people at the beach today."),
        ("No hay leche.","There's no milk."),
        ("¿Hay arroz con pollo?","Is there chicken and rice?")],
 "pr": [("there are waves","hay olas"),
        ("there's no coffee","no hay café"),
        ("is there food?","¿hay comida?")],
},
{
 "t": "Frequency words", "d": "Always, usually, sometimes, never — how often.",
 "chips": [("siempre","g"),("a veces","g"),("nunca","a")],
 "body": (
   '<p>From “always” down to “never”:</p>'
   + _gtable(["Spanish","English"],[
     [_es("siempre"),"always"],
     [_es("casi siempre"),"almost always"],
     [_es("normalmente"),"usually / normally"],
     [_es("a menudo"),"often"],
     [_es("a veces"),"sometimes"],
     [_es("raramente"),"rarely"],
     [_es("casi nunca"),"almost never"],
     [_es("nunca"),"never"]])
   + '<p><b>To be specific</b>, use '+_es("todos los")+' / '
   +_es("todas las")+' + a plural time period, or '+_es("una vez")+' (once) '
   'and a number + '+_es("veces")+' (times):</p>'
   + _gtable(["Spanish","English"],[
     [_es("todos los días"),"every day"],
     [_es("todos los domingos"),"every Sunday"],
     [_es("todas las mañanas"),"every morning"],
     [_es("los fines de semana"),"on weekends"],
     [_es("una vez al mes"),"once a month"],
     [_es("dos veces a la semana"),"twice a week"]])
   + '<p>They sit right before the verb or at the end of the sentence — '
   'both are fine: '+_es("Normalmente voy al gimnasio")+' / '
   +_es("Voy al gimnasio normalmente")+'.</p>'
   '<p><b>With “no”:</b> '+_es("no")+' still goes directly before the verb: '
   +_es("Normalmente no cocino los lunes.")+' And for “never,” don\'t say '
   '“no siempre” — use '+_es("nunca")+', with the double negative when it '
   'follows the verb: '+_es("No voy nunca.")+'</p>'),
 "ex": [("Siempre tomamos un cafecito después de cenar.","We always have a little coffee after dinner."),
        ("Normalmente voy al gimnasio después del trabajo.","I usually go to the gym after work."),
        ("Hago paddleboard dos veces a la semana.","I paddleboard twice a week."),
        ("Todos los domingos comemos con su familia.","Every Sunday we eat with his family."),
        ("Riego las plantas todas las mañanas.","I water the plants every morning."),
        ("A veces veo delfines desde la tabla.","Sometimes I see dolphins from the board.")],
 "pr": [("usually","normalmente"),("often","a menudo"),
        ("rarely","raramente"),("twice a week","dos veces a la semana"),
        ("every Sunday","todos los domingos"),("once a month","una vez al mes")],
},
{
 "t": "“Gustar” — the backwards verb", "d": "Me gusta = it pleases me.",
 "chips": [("me","a"),("gusta","a"),("gustan","g")],
 "body": (
   '<p>'+_es("Me gusta el café")+' doesn\'t literally mean “I like coffee” '
   '— it means “coffee <b>pleases me</b>.” So the ending follows the '
   '<b>thing</b>, not you:</p>'
   + _gtable(["One thing","More than one"],[
     [_es("Me gusta la playa."),_es("Me gustan las olas.")],
     [_es("Me gusta bailar."),_es("Me gustan los tostones.")]])
   + '<p class="small">Swap '+_es("me")+' for '+_es("te")+' (you) or '
   +_es("le")+' (he/she): '+_es("¿Te gusta la música latina?")+' '
   'Stronger: '+_es("me encanta")+' — I love it.</p>'),
 "ex": [("Me gusta la playa, la jardinería y hacer paddleboard.","I like the beach, gardening, and paddleboarding."),
        ("Me gustan los frijoles negros.","I like black beans."),
        ("Me encanta bailar salsa con Joshua.","I love dancing salsa with Joshua.")],
 "pr": [("I like coffee","me gusta el café"),
        ("I like the beans (plural!)","me gustan los frijoles"),
        ("I love the beach","me encanta la playa")],
},
{
 "id": "porpara",
 "t": "Por vs. para", "d": "Two words for “for” — and they're not interchangeable.",
 "chips": [("por","a"),("para","s"),("gracias","g")],
 "body": (
   '<p>The trick: <b>para looks forward</b> (goal, destination, recipient) — '
   '<b>por looks back or through</b> (reason, exchange, along, during).</p>'
   + _gtable(["PARA — forward →","POR — because / through"],[
     ["a goal: "+_es("Estudio para hablar con su familia"),
      "a reason: "+_es("Gracias por todo")],
     ["a recipient: "+_es("Este cafecito es para ti"),
      "movement through: "+_es("Caminamos por la playa")],
     ["a destination: "+_es("Salgo para el trabajo"),
      "time of day: "+_es("por la mañana")],
     ["a deadline: "+_es("para el viernes"),
      "an exchange: "+_es("Lo compré por veinte dólares")]])
   + '<p class="small">Don\'t stress about mastering this — even advanced '
   'learners mix these up. Learn the phrases above as chunks and you\'ll be '
   'right most of the time.</p>'),
 "ex": [("Gracias por todo.","Thanks for everything. (say this to his mom!)"),
        ("Este cafecito es para ti.","This little coffee is for you."),
        ("Caminamos por la playa con Maggie.","We walk along the beach with Maggie."),
        ("Estudio español para hablar con su familia.","I study Spanish (in order) to talk with his family.")],
 "pr": [("thanks for everything","gracias por todo"),
        ("this is for you: es ___ ti","para"),
        ("in the morning: ___ la mañana","por"),
        ("(goal) I study ___ to speak: estudio ___ hablar","para")],
},
{
 "id": "objetos",
 "t": "Object pronouns", "d": "me, te, lo, la — “me, you, it.”",
 "chips": [("lo","a"),("la","s"),("te","g")],
 "body": (
   '<p>Little words that stand in for people and things, so you don\'t '
   'repeat the noun. You already use two constantly: '
   +_es("te quiero")+' and '+_es("lo estoy intentando")+'.</p>'
   + _gtable(["Spanish","English"],[
     [_es("me"),"me"],[_es("te"),"you"],
     [_es("lo"),"him / it (masculine)"],[_es("la"),"her / it (feminine)"],
     [_es("nos"),"us"],[_es("los / las"),"them"]])
   + '<p><b>Where does it go?</b> Right <b>before</b> the conjugated verb: '
   +_es("Lo veo")+' — I see it. With two verbs you can also hang it on the '
   'end of the second: '+_es("Lo quiero comer")+' or '
   +_es("Quiero comerlo")+' — both correct.</p>'),
 "ex": [("Te quiero mucho.","I love you a lot."),
        ("¿Me ayudas con el español?","Will you help me with Spanish?"),
        ("Lo estoy intentando.","I'm trying it."),
        ("¿Los tostones? Los comí todos.","The tostones? I ate them all."),
        ("Maggie nos espera en casa.","Maggie is waiting for us at home.")],
 "pr": [("I love you","te quiero"),
        ("I'm trying it","lo estoy intentando"),
        ("I ate them (los tostones): ___ comí","los"),
        ("will you help me? ¿___ ayudas?","me")],
},
{
 "id": "muymucho",
 "t": "Muy vs. mucho", "d": "“Very” vs. “a lot” — the classic mix-up.",
 "chips": [("muy","a"),("mucho","s"),("muchas","g")],
 "body": (
   '<p>Both feel like “very,” but they live in different places:</p>'
   + _gtable(["MUY + describing word","MUCHO + noun / after verb"],[
     [_es("muy cansada")+" — very tired", _es("mucho calor")+" — a lot of heat"],
     [_es("muy bien")+" — very well", _es("muchas olas")+" — many waves"],
     [_es("muy dulce")+" — very sweet", _es("Te quiero mucho")+" — I love you a lot"]])
   + '<p><b>Muy never changes.</b> <b>Mucho matches the noun</b>: '
   +_es("mucho calor")+', '+_es("mucha agua")+', '+_es("muchos perros")+', '
   +_es("muchas flores")+'. And there\'s no “muy mucho” — for “very '
   'much,” say '+_es("muchísimo")+'.</p>'),
 "ex": [("Hoy hace mucho calor y estoy muy cansada.","Today it's very hot and I'm very tired."),
        ("Hay muchas olas esta mañana.","There are a lot of waves this morning."),
        ("El cafecito está muy dulce.","The cafecito is very sweet."),
        ("Te quiero muchísimo.","I love you very much.")],
 "pr": [("very tired (you, f)","muy cansada"),
        ("a lot of heat","mucho calor"),
        ("many waves","muchas olas"),
        ("I love you a lot: te quiero ___","mucho")],
},
{
 "id": "teneridioms",
 "t": "Tener expressions", "d": "In Spanish you HAVE hunger, heat, and sleepiness.",
 "chips": [("hambre","a"),("sueño","s"),("ganas","g")],
 "body": (
   '<p>English says “I <em>am</em> hungry” — Spanish says “I '
   '<em>have</em> hunger.” A whole family of feelings works this way:</p>'
   + _gtable(["Spanish","English"],[
     [_es("tengo hambre"),"I'm hungry"],[_es("tengo sed"),"I'm thirsty"],
     [_es("tengo calor"),"I'm hot"],[_es("tengo frío"),"I'm cold"],
     [_es("tengo sueño"),"I'm sleepy"],[_es("tengo miedo"),"I'm scared"],
     [_es("tengo prisa"),"I'm in a hurry"],[_es("tengo razón"),"I'm right"],
     [_es("tengo suerte"),"I'm lucky"],
     [_es("tengo ganas de…"),"I feel like… (+ verb)"]])
   + '<p><b>The one that saves you embarrassment:</b> for “I\'m hot” '
   '(temperature), always '+_es("tengo calor")+' — never “estoy '
   'caliente,” which means something very different.</p>'),
 "ex": [("Tengo hambre. ¿Comemos?","I'm hungry. Shall we eat?"),
        ("Tengo ganas de ir a la playa.","I feel like going to the beach."),
        ("Tengo sueño — me acuesto temprano.","I'm sleepy — I'm going to bed early."),
        ("¡Tengo suerte de tener a Joshua!","I'm lucky to have Joshua!")],
 "pr": [("I'm hungry","tengo hambre"),
        ("I'm sleepy","tengo sueño"),
        ("I feel like dancing","tengo ganas de bailar"),
        ("I'm hot (temperature!)","tengo calor")],
},
{
 "id": "comandos",
 "t": "Tú commands", "d": "Ven, dale, siéntate — you already use these with Maggie.",
 "chips": [("ven","a"),("dale","s"),("haz","g")],
 "body": (
   '<p>To tell someone (or Maggie) to do something, the regular rule is '
   'sweet: <b>use the él/ella form</b>: '+_es("habla")+' (speak!), '
   +_es("come")+' (eat!), '+_es("camina")+' (walk!).</p>'
   '<p><b>Eight famous rebels</b> — memorize the chant '
   '“<b>Vin Diesel Has Ten Weapons</b>”:</p>'
   + _gtable(["Command","From","Means"],[
     [_es("ven"),"venir","come!"],[_es("di"),"decir","say!"],
     [_es("sal"),"salir","leave!"],[_es("haz"),"hacer","do!"],
     [_es("ten"),"tener","have!"],[_es("ve"),"ir","go!"],
     [_es("pon"),"poner","put!"],[_es("sé"),"ser","be!"]])
   + '<p><b>Little words hang on the end:</b> '+_es("dime")+' (tell me), '
   +_es("hazlo")+' (do it), '+_es("siéntate")+' (sit down!). And now you '
   'know what '+_es("dale")+' literally is: da + le — “give it!” → '
   'Cuban for “go for it.”</p>'),
 "ex": [("¡Ven aquí, Maggie! ¡Siéntate!","Come here, Maggie! Sit!"),
        ("Dime la verdad.","Tell me the truth."),
        ("Pon música cubana.","Put on Cuban music."),
        ("Dale, vamos a la playa.","Go on, let's go to the beach.")],
 "pr": [("come! (Maggie)","ven"),
        ("tell me","dime"),
        ("do it","hazlo"),
        ("put on music: ___ música","pon")],
},
{
 "id": "comparar",
 "t": "Comparisons", "d": "más que, menos que, tan… como.",
 "chips": [("más","a"),("que","g"),("mejor","s")],
 "body": (
   _gtable(["Pattern","Example"],[
     [_es("más … que")+" — more … than",
      _es("El café cubano es más fuerte que el americano.")],
     [_es("menos … que")+" — less … than",
      _es("La tarde está menos tranquila que la mañana.")],
     [_es("tan … como")+" — as … as",
      _es("Esta playa es tan bonita como aquella.")],
     [_es("mejor / peor")+" — better / worse",
      _es("Joshua baila mejor que yo.")],
     [_es("el / la más …")+" — the most …",
      _es("Maggie es la perra más cariñosa del mundo.")]])),
 "ex": [("El café cubano es más fuerte que el americano.","Cuban coffee is stronger than American coffee."),
        ("Joshua baila mejor que yo… por ahora.","Joshua dances better than me… for now."),
        ("Maggie es la perra más cariñosa del mundo.","Maggie is the most affectionate dog in the world.")],
 "pr": [("stronger than: más fuerte ___","que"),
        ("as pretty as: tan bonita ___","como"),
        ("better","mejor"),
        ("the most affectionate: la ___ cariñosa","más")],
},
{
 "id": "lugares",
 "t": "Where things are", "d": "en, sobre, debajo de, cerca de…",
 "chips": [("cerca de","s"),("debajo","a"),("entre","g")],
 "body": (
   _gtable(["Spanish","English"],[
     [_es("en"),"in / on / at"],[_es("sobre"),"on top of"],
     [_es("debajo de"),"under"],[_es("cerca de"),"near"],
     [_es("lejos de"),"far from"],[_es("al lado de"),"next to"],
     [_es("entre"),"between"],[_es("dentro de"),"inside"],
     [_es("detrás de"),"behind"],[_es("delante de"),"in front of"]])
   + '<p class="small">Remember '+_es("de + el = del")+': '
   +_es("al lado del café")+' — next to the café. Use these with '
   +_es("estar")+': '+_es("Maggie está debajo de la mesa.")+'</p>'),
 "ex": [("Maggie está debajo de la mesa.","Maggie is under the table."),
        ("La casa está cerca de la playa.","The house is near the beach."),
        ("Las llaves están sobre la mesa.","The keys are on the table."),
        ("El gimnasio está al lado del café.","The gym is next to the café.")],
 "pr": [("near the beach","cerca de la playa"),
        ("under the table","debajo de la mesa"),
        ("next to the café","al lado del café"),
        ("between","entre")],
},
]


def get():
    """Returns (tab_body_html, {detail_key: sheet_html})."""
    cards, sheets = [], {}
    cards.append('<div class="eyebrow">Grammar Guide</div>')
    cards.append('<h1>Grammar, in plain English</h1>')
    cards.append('<p class="muted">Simple explanations with clear examples. '
                 'Tap a card for the breakdown — rule, table, real sentences, '
                 'and quick practice.</p>')
    cards.append('<div class="ggrid">')
    for i, tp in enumerate(TOPICS):
        key = f"g_{tp['id']}" if "id" in tp else f"g{i}"
        chip_h = "".join(
            f'<span class="gchip {c} r{(j % 3) + 1}">{esc(w)}</span>'
            for j, (w, c) in enumerate(tp["chips"]))
        cards.append(
            f'<div class="gcard" data-key="{key}" role="button" tabindex="0">'
            f'<div class="gc-t">{esc(tp["t"])}</div>'
            f'<div class="gc-d">{esc(tp["d"])}</div>'
            f'<div class="gchips">{chip_h}</div></div>')
        sheet = ['<div class="sh-k">Grammar Guide</div>',
                 f'<h3 class="gg-t">{esc(tp["t"])}</h3>',
                 f'<p class="muted">{esc(tp["d"])}</p>',
                 tp["body"],
                 '<h4>Examples — tap to hear</h4>', examples(tp["ex"]),
                 '<h4>Practice — tap to check</h4>']
        sheet += [_rev(q, a) for q, a in tp["pr"]]
        sheets[key] = "".join(sheet)
    cards.append('</div>')
    return "".join(cards), sheets
