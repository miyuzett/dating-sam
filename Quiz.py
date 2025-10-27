import streamlit as st
import random
import time

st.title("Dating Sam 💞")
st.audio("videoplayback (1).m4a")
col1, col2, col3 = st.columns(3)

col2.image("1000046783.jpg")
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

# Estado inicial
if "count" not in st.session_state:
    st.session_state.count = 0

# Verificar si aún hay preguntas
if st.session_state.count < len(questions):
    question = questions[st.session_state.count]
    st.subheader(question["question"])
    selected_option = st.radio("Elige tu respuesta:", question["options"], key=f"opcion_{st.session_state.count}")

    if st.button("Sube tu respuesta"):
        if selected_option == question["answer"]:
            st.success("¡Ganaste! 🎉")
        else:
            st.error(f"Morirás 😈 La respuesta correcta era: {question['answer']}")

        # Avanzar a la siguiente pregunta
        st.session_state.count += 1
        time.sleep(2)
        st.rerun()

else:
    st.success("Has terminado el quiz, para tener el ***_tesoro_*** de sam debes pasar a la siguiente pestaña.")
    if st.button("Reiniciar"):
        st.session_state.count = 0
        st.rerun()