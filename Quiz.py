import streamlit as st
import random
import time

#  Título y audio DE JUSTIN BIEBER
st.markdown("<h1 style='text-align: center; color: pink;'>💞 Dating Sam 💞</h1>", unsafe_allow_html=True)
st.audio("videoplayback (1).m4a")
col1, col2, col3 = st.columns(3)
col2.image("1000046783.jpg")

name = st.text_input("Ingresa tu nombre")

# Preguntas
questions = [
    {
        "question": "¿Cómo se llaman los padres de Sam? 😱🐱",
        "options": [
            "Selena Gómez y Justin Bieber",
            "Daniel el más variado y Matías Venegas",
            "Rosenharte y Anina",
            "Baby Steve y Aiken",
        ],
        "answer": "Rosenharte y Anina",
    },
    {
        "question": "¿Qué quería ser Sam de pequeño?",
        "options": ["Astronauta", "Panadero", "Muhammad Ali Jinnah", "Presidente"],
        "answer": "Astronauta",
    },
    {
        "question": "¿Cuál es su número favorito?",
        "options": ["7", "100", "8", "10"],
        "answer": "10",
    },
    {
        "question": "¿Cuál es su comida favorita?",
        "options": ["Spaghetti", "Tu tesoro", "Helado", "Pozole de lavadero"],
        "answer": "Pozole de lavadero",
    },
    {
        "question": "¿Cuál es su superpoder?",
        "options": ["Volar", "Super fuerza", "Invisibilidad", "Manipulación mental"],
        "answer": "Volar",
    },
    {
        "question": "¿Cuál es su fobia?",
        "options": [
            "filofobia",
            "homofobia",
            "hidrofobia",
            "hipaputomonstrosesquipedalofobia",
        ],
        "answer": "hipaputomonstrosesquipedalofobia",
    },
    {
        "question": "¿Cuál es su animal favorito?",
        "options": ["cocodrilo", "paput", "Perro", "megalodón"],
        "answer": "Perro",
    },
    {
        "question": "¿Cuándo nació?",
        "options": ["1445", "600 A.C", "666 D.C", "1985"],
        "answer": "666 D.C",
    },
    {
        "question": "¿Cuál es su brainrot favorito?",
        "options": [
            "bombardiro crocodrilo",
            "tralarero",
            "boneca ambalabu",
            "chicleteira bicicleteira",
        ],
        "answer": "chicleteira bicicleteira",
    },
]

#Estado inicial
if "count" not in st.session_state:
    st.session_state.count = 0
if "correct" not in st.session_state:
    st.session_state.correct = 0
if "wrong" not in st.session_state:
    st.session_state.wrong = 0

# Mostrar progreso guardado anteriormente de las respuestas acertadas y erradas 
st.progress(st.session_state.count / len(questions))
st.caption(f"Pregunta {st.session_state.count + 1} de {len(questions)}")

# Lógica principal
if st.session_state.count < len(questions):
    question = questions[st.session_state.count]
    st.subheader(question["question"])
    selected_option = st.radio("Elige tu respuesta:", question["options"], key=f"opcion_{st.session_state.count}")

    if st.button("Sube tu respuesta"):
        if selected_option == question["answer"]:
            st.success("¡Ganaste! :partying:")
            st.session_state.correct += 1
        else:
            st.error(f"Morirás :imp: La respuesta correcta era: {question['answer']}")
            st.session_state.wrong += 1

        # Avanzar a la siguiente pregunta
        st.session_state.count += 1
        time.sleep(2)
        st.rerun()

# Resultado final
else:
    total = st.session_state.correct + st.session_state.wrong
    porcentaje = (st.session_state.correct / total) * 100 if total > 0 else 0

    st.success("felicidades has terminado el quiz:revolving_hearts: ")
    st.write(f":white_check_mark: Correctas: **{st.session_state.correct}**")
    st.write(f"❌ Incorrectas: **{st.session_state.wrong}**")
    st.write(f":bar_chart: Porcentaje de aciertos: **{porcentaje:.2f}%**")

    # Mensaje personalizado según el puntaje
    if porcentaje == 100:
        st.balloons()
        st.markdown("🌹 **¡Eres el alma gemela de Sam!** 💍")
    elif porcentaje >= 70:
        st.markdown("¡Te llevas bien con Sam, pero puedes conocerlo mejor!:heart_eyes_cat:")
    else:
        st.markdown(":crying_cat_face: Sam dice que t/N estudie más sobre él...")

    # Botón de reinicio
    if st.button("Reiniciar"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

