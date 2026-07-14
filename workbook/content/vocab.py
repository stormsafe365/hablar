# -*- coding: utf-8 -*-
"""Part III data: real-life vocabulary, organized around Celeste's actual life
in Florida rather than a generic textbook (no 'the museum is to the left').

Each theme dict has:
  icon, title, intro, vocab [(es,en,note)], dialogue [(who,es,en)],
  story {title, es, en}, fill [(sentence,answer)], translate [(en,es)].
"""

THEMES = [
{
  "icon": "🏖", "title": "The Beach",
  "intro": "The center of Florida life. If you learn one theme cold, make it this one.",
  "vocab": [
    ("la playa", "the beach", ""),
    ("el mar", "the sea", ""),
    ("la arena", "the sand", ""),
    ("la ola", "the wave", "las olas = the waves"),
    ("la marea", "the tide", "marea alta/baja = high/low tide"),
    ("el traje de baño", "the swimsuit", ""),
    ("la toalla", "the towel", ""),
    ("las gafas de sol", "the sunglasses", ""),
    ("la crema solar", "the sunscreen", "also el protector solar"),
    ("la sombrilla", "the beach umbrella", ""),
    ("la concha", "the seashell", ""),
    ("el atardecer", "the sunset", ""),
    ("nadar", "to swim", ""),
    ("broncearse", "to tan / sunbathe", ""),
    ("la brisa", "the breeze", ""),
    ("mojado / mojada", "wet", ""),
  ],
  "dialogue": [
    ("Celeste", "¿Vamos a la playa? Hace sol.", "Shall we go to the beach? It's sunny."),
    ("Novio", "¡Dale! Llevo las toallas y la sombrilla.", "Sure! I'll bring the towels and the umbrella."),
    ("Celeste", "Yo llevo la crema solar y el agua.", "I'll bring the sunscreen and the water."),
    ("Novio", "El mar está tranquilo hoy, perfecto para nadar.", "The sea is calm today, perfect for swimming."),
    ("Celeste", "Quiero ver el atardecer también.", "I want to watch the sunset too."),
  ],
  "story": {
    "title": "Un día en la playa",
    "es": "Es sábado por la mañana y hace sol. Celeste y su novio van a la playa "
          "temprano. El mar está tranquilo y la arena está caliente. Celeste nada "
          "un poco y después busca conchas. Su novio pone música cubana y toman "
          "café. Por la tarde, ven el atardecer juntos. El cielo es rosa y "
          "naranja. “Qué bonito”, dice Celeste.",
    "en": "It's Saturday morning and it's sunny. Celeste and her boyfriend go to "
          "the beach early. The sea is calm and the sand is hot. Celeste swims a "
          "little and then looks for shells. Her boyfriend plays Cuban music and "
          "they drink coffee. In the afternoon, they watch the sunset together. "
          "The sky is pink and orange. “How beautiful,” says Celeste.",
  },
  "fill": [
    ("Voy a la ___ los sábados.", "playa"),
    ("El ___ está tranquilo hoy.", "mar"),
    ("Necesito ___ solar para no quemarme.", "crema"),
    ("Me gusta ver el ___ por la tarde.", "atardecer"),
    ("Llevo mi ___ de baño y una toalla.", "traje"),
  ],
  "translate": [
    ("Let's go to the beach.", "Vamos a la playa."),
    ("The sea is calm.", "El mar está tranquilo."),
    ("I want to watch the sunset.", "Quiero ver el atardecer."),
    ("Bring the sunscreen.", "Lleva la crema solar."),
  ],
},
{
  "icon": "🌊", "title": "Paddleboarding & Water",
  "intro": "Your favorite way to be on the water — vocabulary for getting out on the board.",
  "vocab": [
    ("la tabla de paddle", "the paddleboard", "or tabla de remo"),
    ("el remo", "the paddle", ""),
    ("remar", "to paddle", ""),
    ("el chaleco salvavidas", "the life vest", ""),
    ("el equilibrio", "the balance", "mantener el equilibrio"),
    ("de pie", "standing", ""),
    ("arrodillarse", "to kneel", ""),
    ("la corriente", "the current", ""),
    ("el delfín", "the dolphin", "los delfines"),
    ("el manglar", "the mangrove", ""),
    ("tranquilo / tranquila", "calm", ""),
    ("caerse", "to fall (off)", "me caigo = I fall"),
    ("flotar", "to float", ""),
    ("la orilla", "the shore", ""),
    ("el amanecer", "the sunrise", ""),
    ("mojarse", "to get wet", ""),
  ],
  "dialogue": [
    ("Celeste", "El agua está tranquila. Voy a hacer paddleboard.", "The water is calm. I'm going to paddleboard."),
    ("Novio", "¿Llevas el chaleco salvavidas?", "Are you taking the life vest?"),
    ("Celeste", "Sí, siempre. A veces veo delfines por la mañana.", "Yes, always. Sometimes I see dolphins in the morning."),
    ("Novio", "Ten cuidado con la corriente cerca del manglar.", "Be careful with the current near the mangrove."),
    ("Celeste", "Tranquilo, mantengo el equilibrio muy bien.", "Don't worry, I keep my balance very well."),
  ],
  "story": {
    "title": "El amanecer en la tabla",
    "es": "Celeste se levanta muy temprano, cuando el mar está tranquilo. Lleva su "
          "tabla de paddle a la orilla y se pone el chaleco salvavidas. Rema despacio "
          "hacia los manglares. El agua está como un espejo. De repente, ve dos "
          "delfines cerca de la tabla. Celeste se queda de pie, sin moverse, y "
          "sonríe. El amanecer es su momento favorito del día.",
    "en": "Celeste gets up very early, when the sea is calm. She carries her "
          "paddleboard to the shore and puts on the life vest. She paddles slowly "
          "toward the mangroves. The water is like a mirror. Suddenly, she sees two "
          "dolphins near the board. Celeste stays standing, without moving, and "
          "smiles. Sunrise is her favorite moment of the day.",
  },
  "fill": [
    ("Uso el ___ para remar.", "remo"),
    ("Siempre llevo el ___ salvavidas.", "chaleco"),
    ("A veces veo ___ en el agua.", "delfines"),
    ("El agua está ___ por la mañana.", "tranquila"),
    ("Remo hacia la ___.", "orilla"),
  ],
  "translate": [
    ("I'm going to paddleboard.", "Voy a hacer paddleboard."),
    ("The water is calm.", "El agua está tranquila."),
    ("Sometimes I see dolphins.", "A veces veo delfines."),
    ("I keep my balance.", "Mantengo el equilibrio."),
  ],
},
{
  "icon": "🌴", "title": "Florida & Weather",
  "intro": "Your home state — sun, heat, storms, and the words to talk about the sky.",
  "vocab": [
    ("Florida", "Florida", ""),
    ("el calor", "the heat", "hace calor = it's hot"),
    ("la humedad", "the humidity", ""),
    ("el sol", "the sun", "hace sol"),
    ("la lluvia", "the rain", "llueve = it rains"),
    ("la tormenta", "the storm", ""),
    ("el huracán", "the hurricane", ""),
    ("el trueno", "the thunder", ""),
    ("el relámpago", "the lightning", ""),
    ("la palmera", "the palm tree", ""),
    ("el cocodrilo", "the alligator/croc", ""),
    ("el mosquito", "the mosquito", ""),
    ("húmedo / húmeda", "humid / damp", ""),
    ("soleado / soleada", "sunny", ""),
    ("nublado / nublada", "cloudy", ""),
    ("el verano", "the summer", ""),
  ],
  "dialogue": [
    ("Novio", "¿Cómo está el tiempo hoy?", "How's the weather today?"),
    ("Celeste", "Hace mucho calor y hay mucha humedad.", "It's very hot and very humid."),
    ("Novio", "Por la tarde viene una tormenta, dicen.", "In the afternoon a storm is coming, they say."),
    ("Celeste", "Típico de Florida en verano.", "Typical of Florida in summer."),
    ("Novio", "Vamos a la playa temprano, antes de la lluvia.", "Let's go to the beach early, before the rain."),
  ],
  "story": {
    "title": "Verano en Florida",
    "es": "En verano, Florida es muy caliente y húmeda. Por la mañana hace sol y el "
          "cielo es azul. Pero por la tarde, casi todos los días, viene una tormenta. "
          "Hay truenos y relámpagos, y llueve mucho por veinte minutos. Después, "
          "el sol sale otra vez. Celeste dice que el clima de Florida es dramático "
          "pero nunca aburrido.",
    "en": "In summer, Florida is very hot and humid. In the morning it's sunny and "
          "the sky is blue. But in the afternoon, almost every day, a storm comes. "
          "There's thunder and lightning, and it rains a lot for twenty minutes. "
          "Afterward, the sun comes out again. Celeste says Florida's weather is "
          "dramatic but never boring.",
  },
  "fill": [
    ("En verano hace mucho ___.", "calor"),
    ("Por la tarde viene una ___.", "tormenta"),
    ("Hay mucha ___ en Florida.", "humedad"),
    ("Las ___ son muy altas aquí.", "palmeras"),
    ("Después de la lluvia, sale el ___.", "sol"),
  ],
  "translate": [
    ("It's very hot today.", "Hoy hace mucho calor."),
    ("A storm is coming.", "Viene una tormenta."),
    ("It's very humid.", "Hay mucha humedad."),
    ("The sky is blue.", "El cielo es azul."),
  ],
},
{
  "icon": "🌺", "title": "Tropical Plants",
  "intro": "The plants that fill a Florida yard — great for describing color and beauty.",
  "vocab": [
    ("la flor", "the flower", "las flores"),
    ("la palmera", "the palm tree", ""),
    ("el hibisco", "the hibiscus", ""),
    ("la buganvilla", "the bougainvillea", ""),
    ("la orquídea", "the orchid", ""),
    ("la hoja", "the leaf", "las hojas"),
    ("el tronco", "the trunk", ""),
    ("la raíz", "the root", "las raíces"),
    ("el helecho", "the fern", ""),
    ("la maceta", "the flowerpot", ""),
    ("florecer", "to bloom", ""),
    ("crecer", "to grow", ""),
    ("verde", "green", ""),
    ("colorido / colorida", "colorful", ""),
    ("la sombra", "the shade", ""),
    ("el aroma", "the scent", ""),
  ],
  "dialogue": [
    ("Celeste", "Mira, el hibisco tiene flores nuevas.", "Look, the hibiscus has new flowers."),
    ("Novio", "Son muy coloridas. ¿De qué color?", "They're very colorful. What color?"),
    ("Celeste", "Rojas y rosadas. La buganvilla también florece.", "Red and pink. The bougainvillea is blooming too."),
    ("Novio", "Las palmeras dan buena sombra.", "The palm trees give good shade."),
    ("Celeste", "Me encanta el aroma del jardín por la mañana.", "I love the scent of the garden in the morning."),
  ],
  "story": {
    "title": "El jardín tropical",
    "es": "El jardín de Celeste está lleno de plantas tropicales. Hay palmeras "
          "altas que dan sombra y flores de muchos colores. El hibisco es rojo, "
          "la buganvilla es rosada y las orquídeas son blancas. Por la mañana, "
          "el aroma de las flores es dulce. Los pájaros vienen a beber agua. "
          "Celeste dice que su jardín es un pequeño paraíso.",
    "en": "Celeste's garden is full of tropical plants. There are tall palm trees "
          "that give shade and flowers of many colors. The hibiscus is red, the "
          "bougainvillea is pink, and the orchids are white. In the morning, the "
          "scent of the flowers is sweet. The birds come to drink water. Celeste "
          "says her garden is a little paradise.",
  },
  "fill": [
    ("El ___ tiene flores rojas.", "hibisco"),
    ("Las ___ dan buena sombra.", "palmeras"),
    ("Las flores son muy ___.", "coloridas"),
    ("Me gusta el ___ de las flores.", "aroma"),
    ("La buganvilla ___ en primavera.", "florece"),
  ],
  "translate": [
    ("The flowers are colorful.", "Las flores son coloridas."),
    ("The hibiscus is red.", "El hibisco es rojo."),
    ("The palm trees give shade.", "Las palmeras dan sombra."),
    ("I love the garden.", "Me encanta el jardín."),
  ],
},
{
  "icon": "🌱", "title": "Gardening",
  "intro": "The actions of tending a garden — verbs you'll use every week.",
  "vocab": [
    ("el jardín", "the garden", ""),
    ("la tierra", "the soil / earth", ""),
    ("la semilla", "the seed", "las semillas"),
    ("regar", "to water", "riego = I water"),
    ("plantar", "to plant", ""),
    ("sembrar", "to sow", ""),
    ("podar", "to prune / trim", ""),
    ("la pala", "the shovel", ""),
    ("la manguera", "the hose", ""),
    ("el abono", "the fertilizer", ""),
    ("la mala hierba", "the weed", ""),
    ("cosechar", "to harvest", ""),
    ("los guantes", "the gloves", ""),
    ("húmedo / húmeda", "moist", ""),
    ("crecer", "to grow", ""),
    ("cuidar", "to take care of", ""),
  ],
  "dialogue": [
    ("Celeste", "Voy a regar las plantas antes del calor.", "I'm going to water the plants before the heat."),
    ("Novio", "¿Necesitas los guantes y la pala?", "Do you need the gloves and the shovel?"),
    ("Celeste", "Sí, y voy a plantar unas semillas nuevas.", "Yes, and I'm going to plant some new seeds."),
    ("Novio", "La tierra está seca. Necesita agua.", "The soil is dry. It needs water."),
    ("Celeste", "También tengo que quitar la mala hierba.", "I also have to pull the weeds."),
  ],
  "story": {
    "title": "La rutina del jardín",
    "es": "Todas las mañanas, Celeste cuida su jardín. Primero riega las plantas con "
          "la manguera, porque la tierra de Florida se seca rápido. Después planta "
          "semillas nuevas y quita la mala hierba con los guantes puestos. A veces "
          "poda las plantas grandes. Le gusta el trabajo tranquilo de la mañana, "
          "cuando todavía no hace mucho calor. Sus tomates ya empiezan a crecer.",
    "en": "Every morning, Celeste takes care of her garden. First she waters the "
          "plants with the hose, because Florida's soil dries out fast. Then she "
          "plants new seeds and pulls the weeds with her gloves on. Sometimes she "
          "prunes the big plants. She likes the quiet work of the morning, when it's "
          "not very hot yet. Her tomatoes are already starting to grow.",
  },
  "fill": [
    ("Todas las mañanas ___ las plantas.", "riego"),
    ("La ___ está seca; necesita agua.", "tierra"),
    ("Voy a ___ unas semillas nuevas.", "plantar"),
    ("Uso los ___ para trabajar en el jardín.", "guantes"),
    ("Tengo que quitar la mala ___.", "hierba"),
  ],
  "translate": [
    ("I water the plants.", "Riego las plantas."),
    ("The soil is dry.", "La tierra está seca."),
    ("I'm going to plant seeds.", "Voy a plantar semillas."),
    ("I take care of my garden.", "Cuido mi jardín."),
  ],
},
{
  "icon": "🐶", "title": "Dogs",
  "intro": "Your dogs are family — here's how to talk to them and about them.",
  "vocab": [
    ("el perro", "the dog", "la perra = female dog"),
    ("el cachorro", "the puppy", ""),
    ("la correa", "the leash", ""),
    ("el collar", "the collar", ""),
    ("pasear", "to walk (a dog)", ""),
    ("ladrar", "to bark", ""),
    ("la cola", "the tail", ""),
    ("la pata", "the paw", ""),
    ("morder", "to bite", ""),
    ("el hueso", "the bone", ""),
    ("la comida para perros", "dog food", ""),
    ("obediente", "obedient", ""),
    ("cariñoso / cariñosa", "affectionate", ""),
    ("¡Ven!", "Come!", "command"),
    ("¡Siéntate!", "Sit!", "command"),
    ("¡Quieto!", "Stay!", "command"),
  ],
  "dialogue": [
    ("Celeste", "Voy a pasear a los perros por la playa.", "I'm going to walk the dogs on the beach."),
    ("Novio", "¿Llevas las correas?", "Are you taking the leashes?"),
    ("Celeste", "Sí. ¡Ven, Max! ¡Siéntate!", "Yes. Come, Max! Sit!"),
    ("Novio", "Ese perro es muy obediente.", "That dog is very obedient."),
    ("Celeste", "Y muy cariñoso. Mueve la cola cuando me ve.", "And very affectionate. He wags his tail when he sees me."),
  ],
  "story": {
    "title": "Los perros de Celeste",
    "es": "Celeste tiene dos perros: Max y Luna. Cada tarde los pasea por la playa "
          "con sus correas. A Max le gusta correr en la arena y ladrar a las olas. "
          "Luna es más tranquila y camina cerca de Celeste. Cuando llegan a casa, "
          "los perros beben mucha agua y duermen. Por la noche, Luna pone la cabeza "
          "en las piernas de Celeste. Son parte de la familia.",
    "en": "Celeste has two dogs: Max and Luna. Every afternoon she walks them on "
          "the beach with their leashes. Max likes to run in the sand and bark at "
          "the waves. Luna is calmer and walks close to Celeste. When they get "
          "home, the dogs drink a lot of water and sleep. At night, Luna puts her "
          "head on Celeste's legs. They're part of the family.",
  },
  "fill": [
    ("Voy a ___ a los perros.", "pasear"),
    ("Llevo las ___ para caminar.", "correas"),
    ("Mi perro es muy ___.", "cariñoso"),
    ("El perro ___ a las olas.", "ladra"),
    ("¡___, Max! ¡Siéntate!", "Ven"),
  ],
  "translate": [
    ("I walk the dogs.", "Paseo a los perros."),
    ("The dog is affectionate.", "El perro es cariñoso."),
    ("Come here!", "¡Ven aquí!"),
    ("The dog barks.", "El perro ladra."),
  ],
},
{
  "icon": "🏋", "title": "The Gym",
  "intro": "Workout vocabulary for you and your boyfriend.",
  "vocab": [
    ("el gimnasio", "the gym", ""),
    ("entrenar", "to train / work out", ""),
    ("el ejercicio", "the exercise", "hacer ejercicio"),
    ("las pesas", "the weights", "levantar pesas"),
    ("la cinta de correr", "the treadmill", ""),
    ("el músculo", "the muscle", ""),
    ("sudar", "to sweat", ""),
    ("estirar", "to stretch", ""),
    ("el calentamiento", "the warm-up", ""),
    ("la repetición", "the rep", ""),
    ("cansado / cansada", "tired", ""),
    ("fuerte", "strong", ""),
    ("el descanso", "the rest / break", ""),
    ("respirar", "to breathe", ""),
    ("la rutina", "the routine", ""),
    ("el yoga", "yoga", ""),
  ],
  "dialogue": [
    ("Novio", "¿Vamos al gimnasio a las siete?", "Shall we go to the gym at seven?"),
    ("Celeste", "Sí, hoy quiero hacer pesas y yoga.", "Yes, today I want to do weights and yoga."),
    ("Novio", "Yo voy a correr en la cinta primero.", "I'm going to run on the treadmill first."),
    ("Celeste", "No olvides el calentamiento.", "Don't forget the warm-up."),
    ("Novio", "Después de entrenar, estoy muy cansado pero contento.", "After working out, I'm very tired but happy."),
  ],
  "story": {
    "title": "La rutina del gimnasio",
    "es": "Celeste y su novio van al gimnasio tres veces por semana. Ella hace yoga "
          "y levanta pesas ligeras. Él corre en la cinta y levanta pesas pesadas. "
          "Siempre empiezan con un calentamiento y terminan con estiramientos. "
          "Después de una hora, los dos sudan mucho y están cansados. “Estoy "
          "fuerte hoy”, dice él. Celeste se ríe y toma agua.",
    "en": "Celeste and her boyfriend go to the gym three times a week. She does "
          "yoga and lifts light weights. He runs on the treadmill and lifts heavy "
          "weights. They always start with a warm-up and finish with stretches. "
          "After an hour, they both sweat a lot and are tired. “I'm strong "
          "today,” he says. Celeste laughs and drinks water.",
  },
  "fill": [
    ("Voy al ___ tres veces por semana.", "gimnasio"),
    ("Me gusta levantar ___.", "pesas"),
    ("Siempre empiezo con un ___.", "calentamiento"),
    ("Después de entrenar estoy muy ___.", "cansada"),
    ("Él corre en la ___ de correr.", "cinta"),
  ],
  "translate": [
    ("I go to the gym.", "Voy al gimnasio."),
    ("I want to work out.", "Quiero entrenar."),
    ("I'm very tired.", "Estoy muy cansada."),
    ("He lifts weights.", "Él levanta pesas."),
  ],
},
{
  "icon": "🎵", "title": "Music",
  "intro": "Cuban salsa, reggaetón, and the words to talk about the songs you love.",
  "vocab": [
    ("la música", "the music", ""),
    ("la canción", "the song", "las canciones"),
    ("la salsa", "salsa (music/dance)", ""),
    ("el reguetón", "reggaeton", ""),
    ("bailar", "to dance", ""),
    ("cantar", "to sing", ""),
    ("la letra", "the lyrics", ""),
    ("el ritmo", "the rhythm", ""),
    ("el cantante", "the singer", "la cantante"),
    ("la banda", "the band", ""),
    ("el altavoz", "the speaker", ""),
    ("la guitarra", "the guitar", ""),
    ("el tambor", "the drum", ""),
    ("pegadizo / pegadiza", "catchy", ""),
    ("subir el volumen", "to turn up the volume", ""),
    ("la pista de baile", "the dance floor", ""),
  ],
  "dialogue": [
    ("Novio", "Pon una canción de salsa.", "Put on a salsa song."),
    ("Celeste", "¿Esta? Tiene un ritmo muy pegadizo.", "This one? It has a very catchy rhythm."),
    ("Novio", "¡Perfecta! Vamos a bailar.", "Perfect! Let's dance."),
    ("Celeste", "No sé bailar salsa muy bien todavía.", "I don't know how to dance salsa very well yet."),
    ("Novio", "Yo te enseño. Sigue el ritmo.", "I'll teach you. Follow the rhythm."),
  ],
  "story": {
    "title": "Noche de salsa",
    "es": "Los sábados por la noche, el novio de Celeste pone música cubana en la "
          "casa. Sube el volumen y baila en la cocina. Las canciones tienen un ritmo "
          "rápido y una letra alegre. Celeste no sabe bailar salsa muy bien, pero "
          "él la enseña, paso a paso. Poco a poco, ella sigue el ritmo mejor. "
          "Al final de la noche, los dos ríen y bailan sin parar.",
    "en": "On Saturday nights, Celeste's boyfriend plays Cuban music in the house. "
          "He turns up the volume and dances in the kitchen. The songs have a fast "
          "rhythm and happy lyrics. Celeste doesn't know how to dance salsa very "
          "well, but he teaches her, step by step. Little by little, she follows "
          "the rhythm better. At the end of the night, they both laugh and dance "
          "without stopping.",
  },
  "fill": [
    ("Pon una ___ de salsa.", "canción"),
    ("Esta canción tiene un ritmo ___.", "pegadizo"),
    ("Quiero aprender a ___ salsa.", "bailar"),
    ("Él ___ el volumen de la música.", "sube"),
    ("La ___ de la canción es alegre.", "letra"),
  ],
  "translate": [
    ("Put on a song.", "Pon una canción."),
    ("Let's dance.", "Vamos a bailar."),
    ("I don't know how to dance salsa.", "No sé bailar salsa."),
    ("The rhythm is catchy.", "El ritmo es pegadizo."),
  ],
},
{
  "icon": "❤️", "title": "Relationships",
  "intro": "The everyday language of love and life with your partner.",
  "vocab": [
    ("el novio", "the boyfriend", ""),
    ("la novia", "the girlfriend", ""),
    ("la pareja", "the couple / partner", ""),
    ("el amor", "love", "mi amor = my love"),
    ("querer", "to love / want", "te quiero"),
    ("amar", "to love (deeply)", "te amo"),
    ("el beso", "the kiss", ""),
    ("el abrazo", "the hug", ""),
    ("extrañar", "to miss (someone)", "te extraño"),
    ("cariño", "sweetheart / affection", ""),
    ("juntos / juntas", "together", ""),
    ("la cita", "the date", ""),
    ("enamorado / enamorada", "in love", ""),
    ("confiar", "to trust", ""),
    ("cuidar", "to care for", ""),
    ("feliz", "happy", ""),
  ],
  "dialogue": [
    ("Novio", "Te extraño cuando estás en el trabajo.", "I miss you when you're at work."),
    ("Celeste", "Yo también, mi amor. Nos vemos esta noche.", "Me too, my love. See you tonight."),
    ("Novio", "¿Quieres salir a cenar? Una cita.", "Do you want to go out to dinner? A date."),
    ("Celeste", "¡Me encanta la idea! Te quiero.", "I love the idea! I love you."),
    ("Novio", "Yo te quiero más. Un beso.", "I love you more. A kiss."),
  ],
  "story": {
    "title": "Nuestra historia",
    "es": "Celeste y su novio están juntos desde hace dos años. Se conocieron en "
          "una fiesta y hablaron toda la noche. Al principio, Celeste no hablaba "
          "español y él no hablaba mucho inglés, pero el amor no necesita muchas "
          "palabras. Ahora Celeste aprende español para hablar con él y con su "
          "familia cubana. Cada día están más enamorados. “Eres mi cariño”, "
          "le dice él.",
    "en": "Celeste and her boyfriend have been together for two years. They met at "
          "a party and talked all night. At first, Celeste didn't speak Spanish and "
          "he didn't speak much English, but love doesn't need many words. Now "
          "Celeste is learning Spanish to talk with him and with his Cuban family. "
          "Every day they're more in love. “You're my sweetheart,” he "
          "tells her.",
  },
  "fill": [
    ("Estamos ___ desde hace dos años.", "juntos"),
    ("Te ___ cuando estás en el trabajo.", "extraño"),
    ("¿Quieres salir en una ___?", "cita"),
    ("Te ___ mucho, mi amor.", "quiero"),
    ("Cada día estamos más ___.", "enamorados"),
  ],
  "translate": [
    ("I love you.", "Te quiero."),
    ("I miss you.", "Te extraño."),
    ("We're together.", "Estamos juntos."),
    ("Do you want to go on a date?", "¿Quieres salir en una cita?"),
  ],
},
{
  "icon": "🍳", "title": "Cooking",
  "intro": "Cuban home cooking and everyday kitchen verbs.",
  "vocab": [
    ("cocinar", "to cook", ""),
    ("la cocina", "the kitchen", ""),
    ("el arroz", "the rice", ""),
    ("los frijoles", "the beans", "arroz con frijoles"),
    ("el pollo", "the chicken", ""),
    ("los plátanos", "the plantains", "tostones, maduros"),
    ("cortar", "to cut", ""),
    ("freír", "to fry", ""),
    ("hervir", "to boil", ""),
    ("probar", "to taste / try", ""),
    ("la sartén", "the frying pan", ""),
    ("la olla", "the pot", ""),
    ("la receta", "the recipe", ""),
    ("el ajo", "the garlic", ""),
    ("la cebolla", "the onion", ""),
    ("sabroso / sabrosa", "tasty", ""),
  ],
  "dialogue": [
    ("Novio", "Voy a cocinar arroz con pollo esta noche.", "I'm going to cook chicken and rice tonight."),
    ("Celeste", "¡Qué rico! ¿Necesitas ayuda?", "How delicious! Do you need help?"),
    ("Novio", "Sí, corta la cebolla y el ajo, por favor.", "Yes, cut the onion and garlic, please."),
    ("Celeste", "¿Y los plátanos? ¿Tostones o maduros?", "And the plantains? Tostones or sweet?"),
    ("Novio", "Tostones. Los frío en la sartén.", "Tostones. I'll fry them in the pan."),
  ],
  "story": {
    "title": "La cena cubana",
    "es": "El novio de Celeste cocina comida cubana los domingos. Hoy hace arroz "
          "con pollo, frijoles negros y tostones. Primero corta la cebolla, el ajo "
          "y el pimiento. Después fríe el pollo en una sartén grande y hierve el "
          "arroz. La cocina huele delicioso. Celeste prueba los frijoles. "
          "“Están sabrosos”, dice. Comen juntos y escuchan música. Es su "
          "domingo perfecto.",
    "en": "Celeste's boyfriend cooks Cuban food on Sundays. Today he makes chicken "
          "and rice, black beans, and tostones. First he cuts the onion, garlic, "
          "and pepper. Then he fries the chicken in a big pan and boils the rice. "
          "The kitchen smells delicious. Celeste tastes the beans. “They're "
          "tasty,” she says. They eat together and listen to music. It's their "
          "perfect Sunday.",
  },
  "fill": [
    ("Voy a ___ arroz con pollo.", "cocinar"),
    ("Corta la ___ y el ajo.", "cebolla"),
    ("Frío los plátanos en la ___.", "sartén"),
    ("La comida está muy ___.", "sabrosa"),
    ("Como arroz con ___ negros.", "frijoles"),
  ],
  "translate": [
    ("I'm going to cook.", "Voy a cocinar."),
    ("Cut the onion.", "Corta la cebolla."),
    ("The food is tasty.", "La comida está sabrosa."),
    ("Do you need help?", "¿Necesitas ayuda?"),
  ],
},
{
  "icon": "🛒", "title": "Grocery Shopping",
  "intro": "The supermarket, the market, and asking for what you need.",
  "vocab": [
    ("el supermercado", "the supermarket", ""),
    ("el mercado", "the market", ""),
    ("la lista", "the list", ""),
    ("comprar", "to buy", ""),
    ("el carrito", "the shopping cart", ""),
    ("la fruta", "the fruit", ""),
    ("la verdura", "the vegetable", ""),
    ("la leche", "the milk", ""),
    ("el pan", "the bread", ""),
    ("el huevo", "the egg", "los huevos"),
    ("la caja", "the checkout / box", ""),
    ("el precio", "the price", ""),
    ("caro / cara", "expensive", ""),
    ("barato / barata", "cheap", ""),
    ("pagar", "to pay", ""),
    ("la bolsa", "the bag", ""),
  ],
  "dialogue": [
    ("Celeste", "¿Tenemos la lista para el supermercado?", "Do we have the list for the supermarket?"),
    ("Novio", "Sí. Necesitamos leche, pan y frutas.", "Yes. We need milk, bread, and fruit."),
    ("Celeste", "¿Cuánto cuesta el mango?", "How much does the mango cost?"),
    ("Novio", "Está barato hoy. Compramos varios.", "It's cheap today. Let's buy several."),
    ("Celeste", "Perfecto. Pago yo en la caja.", "Perfect. I'll pay at the checkout."),
  ],
  "story": {
    "title": "En el mercado",
    "es": "Los sábados, Celeste y su novio van al mercado. Primero hacen una lista "
          "en casa. En el mercado hay mucha fruta fresca: mangos, piñas y plátanos. "
          "Las verduras están baratas y de buena calidad. Celeste pregunta el precio "
          "de todo. Compran comida para toda la semana y llenan dos bolsas. Al "
          "final, pagan en la caja y vuelven a casa contentos.",
    "en": "On Saturdays, Celeste and her boyfriend go to the market. First they "
          "make a list at home. At the market there's a lot of fresh fruit: mangos, "
          "pineapples, and plantains. The vegetables are cheap and good quality. "
          "Celeste asks the price of everything. They buy food for the whole week "
          "and fill two bags. In the end, they pay at the checkout and go home "
          "happy.",
  },
  "fill": [
    ("Hacemos una ___ antes de ir al mercado.", "lista"),
    ("¿Cuánto ___ el mango?", "cuesta"),
    ("La fruta está muy ___ hoy.", "barata"),
    ("Pago en la ___.", "caja"),
    ("Necesitamos leche y ___.", "pan"),
  ],
  "translate": [
    ("We need milk and bread.", "Necesitamos leche y pan."),
    ("How much does it cost?", "¿Cuánto cuesta?"),
    ("It's cheap today.", "Está barato hoy."),
    ("I'll pay at the checkout.", "Pago en la caja."),
  ],
},
{
  "icon": "🏡", "title": "Home",
  "intro": "Rooms, furniture, and the daily rhythm of the house.",
  "vocab": [
    ("la casa", "the house", ""),
    ("el cuarto", "the room / bedroom", "la habitación"),
    ("la cocina", "the kitchen", ""),
    ("el baño", "the bathroom", ""),
    ("la sala", "the living room", ""),
    ("el jardín", "the yard / garden", ""),
    ("la cama", "the bed", ""),
    ("el sofá", "the couch", ""),
    ("la mesa", "the table", ""),
    ("la silla", "the chair", ""),
    ("la puerta", "the door", ""),
    ("la ventana", "the window", ""),
    ("limpiar", "to clean", ""),
    ("ordenar", "to tidy up", ""),
    ("descansar", "to rest", ""),
    ("cómodo / cómoda", "comfortable", ""),
  ],
  "dialogue": [
    ("Celeste", "Voy a limpiar la cocina esta mañana.", "I'm going to clean the kitchen this morning."),
    ("Novio", "Yo ordeno la sala y saco la basura.", "I'll tidy the living room and take out the trash."),
    ("Celeste", "Después descansamos en el sofá.", "Then we'll rest on the couch."),
    ("Novio", "Abre la ventana, hace calor.", "Open the window, it's hot."),
    ("Celeste", "La casa está muy cómoda hoy.", "The house is very comfortable today."),
  ],
  "story": {
    "title": "Nuestra casa",
    "es": "La casa de Celeste es pequeña pero cómoda. Tiene dos cuartos, una cocina, "
          "un baño y una sala con un sofá grande. Afuera hay un jardín con palmeras. "
          "Por la mañana, Celeste abre las ventanas para sentir la brisa. Los "
          "sábados limpian y ordenan la casa juntos. Después descansan en el sofá "
          "con los perros y ven una película. Para ellos, la casa es su lugar "
          "favorito del mundo.",
    "en": "Celeste's house is small but comfortable. It has two bedrooms, a "
          "kitchen, a bathroom, and a living room with a big couch. Outside there's "
          "a garden with palm trees. In the morning, Celeste opens the windows to "
          "feel the breeze. On Saturdays they clean and tidy the house together. "
          "Then they rest on the couch with the dogs and watch a movie. For them, "
          "the house is their favorite place in the world.",
  },
  "fill": [
    ("Voy a ___ la cocina.", "limpiar"),
    ("Descansamos en el ___.", "sofá"),
    ("Abre la ___, hace calor.", "ventana"),
    ("La casa tiene dos ___.", "cuartos"),
    ("La casa está muy ___.", "cómoda"),
  ],
  "translate": [
    ("I'm going to clean the kitchen.", "Voy a limpiar la cocina."),
    ("We rest on the couch.", "Descansamos en el sofá."),
    ("Open the window.", "Abre la ventana."),
    ("The house is comfortable.", "La casa está cómoda."),
  ],
},
{
  "icon": "☕", "title": "Coffee",
  "intro": "Cuban coffee is a whole ritual — and a great daily conversation.",
  "vocab": [
    ("el café", "the coffee", ""),
    ("el cafecito", "little (Cuban) coffee", "small & strong"),
    ("el colador", "the coffee strainer", ""),
    ("la cafetera", "the coffee maker", "moka pot"),
    ("el azúcar", "the sugar", ""),
    ("la leche", "the milk", ""),
    ("el café con leche", "coffee with milk", ""),
    ("la cortadito", "espresso w/ a little milk", "un cortadito"),
    ("caliente", "hot", ""),
    ("fuerte", "strong", ""),
    ("dulce", "sweet", ""),
    ("amargo / amarga", "bitter", ""),
    ("la taza", "the cup / mug", ""),
    ("colar", "to brew (strain)", ""),
    ("despertarse", "to wake up", ""),
    ("por la mañana", "in the morning", ""),
  ],
  "dialogue": [
    ("Novio", "¿Quieres un cafecito?", "Do you want a little coffee?"),
    ("Celeste", "Sí, por favor. Con un poco de azúcar.", "Yes, please. With a little sugar."),
    ("Novio", "El café cubano es fuerte y dulce.", "Cuban coffee is strong and sweet."),
    ("Celeste", "Me gusta el café con leche por la mañana.", "I like coffee with milk in the morning."),
    ("Novio", "Ya está listo. Está bien caliente.", "It's ready. It's nice and hot."),
  ],
  "story": {
    "title": "El cafecito de la mañana",
    "es": "En la casa de Celeste, la mañana empieza con café. Su novio prepara un "
          "cafecito cubano en la cafetera. El café es pequeño, fuerte y muy dulce, "
          "con mucha azúcar. Celeste prefiere un café con leche, más suave. Beben el "
          "café juntos en el jardín, con los perros a los pies. El aroma del café "
          "cubano llena la casa. “Así empieza un buen día”, dice ella.",
    "en": "In Celeste's house, the morning begins with coffee. Her boyfriend makes "
          "a Cuban cafecito in the moka pot. The coffee is small, strong, and very "
          "sweet, with a lot of sugar. Celeste prefers a coffee with milk, milder. "
          "They drink the coffee together in the garden, with the dogs at their "
          "feet. The aroma of Cuban coffee fills the house. “That's how a good "
          "day starts,” she says.",
  },
  "fill": [
    ("¿Quieres un ___?", "cafecito"),
    ("El café cubano es fuerte y ___.", "dulce"),
    ("Me gusta el café con ___.", "leche"),
    ("El café está muy ___.", "caliente"),
    ("Preparo el café en la ___.", "cafetera"),
  ],
  "translate": [
    ("Do you want a coffee?", "¿Quieres un café?"),
    ("Cuban coffee is strong.", "El café cubano es fuerte."),
    ("With a little sugar.", "Con un poco de azúcar."),
    ("The coffee is hot.", "El café está caliente."),
  ],
},
{
  "icon": "💼", "title": "Work",
  "intro": "Talking about your job, your schedule, and your day.",
  "vocab": [
    ("el trabajo", "the work / job", ""),
    ("trabajar", "to work", ""),
    ("la oficina", "the office", ""),
    ("el jefe", "the boss", "la jefa"),
    ("el compañero", "the coworker", "la compañera"),
    ("la reunión", "the meeting", ""),
    ("el correo", "the email", ""),
    ("la computadora", "the computer", ""),
    ("el horario", "the schedule", ""),
    ("ocupado / ocupada", "busy", ""),
    ("el sueldo", "the salary", ""),
    ("el descanso", "the break", ""),
    ("empezar", "to start", ""),
    ("terminar", "to finish", ""),
    ("cansado / cansada", "tired", ""),
    ("el proyecto", "the project", ""),
  ],
  "dialogue": [
    ("Novio", "¿A qué hora empiezas a trabajar?", "What time do you start work?"),
    ("Celeste", "A las nueve. Tengo una reunión temprano.", "At nine. I have an early meeting."),
    ("Novio", "¿Estás muy ocupada hoy?", "Are you very busy today?"),
    ("Celeste", "Sí, tengo mucho trabajo y muchos correos.", "Yes, I have a lot of work and a lot of emails."),
    ("Novio", "Descansa un poco. Nos vemos esta tarde.", "Rest a little. See you this afternoon."),
  ],
  "story": {
    "title": "Un día de trabajo",
    "es": "Celeste trabaja en una oficina cerca de la playa. Empieza a las nueve y "
          "termina a las cinco. Por la mañana tiene una reunión con su jefa y sus "
          "compañeros. Después responde muchos correos en la computadora. A "
          "mediodía toma un descanso y come afuera, al sol. Los días están "
          "ocupados, pero le gusta su trabajo. Cuando termina, va directo a la "
          "playa a descansar.",
    "en": "Celeste works in an office near the beach. She starts at nine and "
          "finishes at five. In the morning she has a meeting with her boss and "
          "coworkers. Then she answers a lot of emails on the computer. At noon she "
          "takes a break and eats outside, in the sun. The days are busy, but she "
          "likes her job. When she finishes, she goes straight to the beach to "
          "rest.",
  },
  "fill": [
    ("___ a las nueve de la mañana.", "Empiezo"),
    ("Tengo una ___ con mi jefa.", "reunión"),
    ("Estoy muy ___ hoy.", "ocupada"),
    ("Respondo muchos ___.", "correos"),
    ("___ de trabajar a las cinco.", "Termino"),
  ],
  "translate": [
    ("I work in an office.", "Trabajo en una oficina."),
    ("I have a meeting.", "Tengo una reunión."),
    ("I'm very busy.", "Estoy muy ocupada."),
    ("What time do you start?", "¿A qué hora empiezas?"),
  ],
},
{
  "icon": "📱", "title": "Texting",
  "intro": "How Spanish actually looks in messages — abbreviations and quick replies.",
  "vocab": [
    ("el mensaje", "the message", ""),
    ("escribir", "to write / text", ""),
    ("el teléfono", "the phone", "el celular"),
    ("llamar", "to call", ""),
    ("contestar", "to answer / reply", ""),
    ("q / que", "that / what", "'q' in texts"),
    ("xq / porq", "because / why", "porque"),
    ("tqm", "love you lots", "te quiero mucho"),
    ("bn", "good / fine", "bien"),
    ("tb", "also", "también"),
    ("finde", "weekend", "fin de semana"),
    ("¿qué tal?", "how's it going?", ""),
    ("jaja", "haha", ""),
    ("ahora", "now", ""),
    ("luego", "later", "'lue-go'"),
    ("nos vemos", "see you", ""),
  ],
  "dialogue": [
    ("Novio", "Hola mi amor, ¿q haces?", "Hi my love, whatcha doing?"),
    ("Celeste", "Nada, en la playa. ¿Y tú?", "Nothing, at the beach. And you?"),
    ("Novio", "En el gym. Nos vemos luego?", "At the gym. See you later?"),
    ("Celeste", "Claro! A las 6 en casa. Tqm", "Of course! At 6 at home. Love you lots."),
    ("Novio", "Dale, bn. Un beso 😘", "Okay, cool. A kiss."),
  ],
  "story": {
    "title": "Mensajes de un día",
    "es": "Celeste y su novio se escriben todo el día. Por la mañana, él le manda "
          "un mensaje: “Buenos días, mi amor”. Al mediodía, ella pregunta: "
          "“¿Qué hacemos esta noche?”. Él contesta rápido: “Cena y "
          "peli en casa”. En los mensajes usan palabras cortas como “q”, "
          "“tb” y “finde”. Al final del día, siempre escriben lo "
          "mismo: “Nos vemos, tqm”.",
    "en": "Celeste and her boyfriend text all day. In the morning, he sends her a "
          "message: “Good morning, my love.” At noon, she asks: “What "
          "are we doing tonight?” He replies quickly: “Dinner and a movie "
          "at home.” In their messages they use short words like “q,” "
          "“tb,” and “finde.” At the end of the day, they always "
          "write the same thing: “See you, love you lots.”",
  },
  "fill": [
    ("¿Qué ___ esta noche?  (planes)", "hacemos"),
    ("En los textos, “q” significa ___.", "que"),
    ("“Tqm” significa te ___ mucho.", "quiero"),
    ("“Finde” significa fin de ___.", "semana"),
    ("Al final escriben: nos ___.", "vemos"),
  ],
  "translate": [
    ("What are you doing?", "¿Qué haces?"),
    ("See you later.", "Nos vemos luego."),
    ("Love you lots.", "Te quiero mucho."),
    ("At the beach, and you?", "En la playa, ¿y tú?"),
  ],
},
]

BY_TITLE = {t["title"]: t for t in THEMES}
