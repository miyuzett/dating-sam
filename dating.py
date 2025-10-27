import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="Dating Sam",
    page_icon=":heartpulse:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)


#barra de navegación


pg = st.navigation(["home page.py","Dating Sam.py","Quiz.py"])
pg.run()