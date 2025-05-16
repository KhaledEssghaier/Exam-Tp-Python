# main_streamlit.py

import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("🎥 Movie Explorer")

# Initialisation de session_state
if "movie" not in st.session_state:
    st.session_state.movie = None
if "summary" not in st.session_state:
    st.session_state.summary = None

# 🎲 Bouton pour charger un film aléatoire
if st.button("🎲 Show Random Movie"):
    try:
        response = requests.get(f"{API_URL}/movies/random/")
        response.raise_for_status()
        st.session_state.movie = response.json()
        st.session_state.summary = None  # Réinitialiser le résumé
    except requests.RequestException as e:
        st.error(f"Erreur lors de la récupération du film : {e}")

# 📺 Affichage du film
if st.session_state.movie:
    movie = st.session_state.movie
    st.header(f"{movie['title']} ({movie['year']})")
    st.write(f"🎬 Directed by: **{movie['director']}**")

    st.subheader("👥 Actors:")
    for actor in movie["actors"]:
        st.write(f"• {actor['actor_name']}")

    # ✅ Activer le bouton Get Summary
    if st.button("🧠 Get Summary"):
        try:
            payload = {"movie_id": movie["id"]}
            response = requests.post(f"{API_URL}/generate_summary/", json=payload)
            response.raise_for_status()
            st.session_state.summary = response.json()["summary_text"]
        except requests.RequestException as e:
            st.error(f"Erreur lors de la génération du résumé : {e}")

    # 💬 Affichage du résumé
    if st.session_state.summary:
        st.subheader("📝 Summary:")
        st.info(st.session_state.summary)
