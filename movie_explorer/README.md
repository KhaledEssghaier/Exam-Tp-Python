# 🎬 LLM-Powered Movie & Actor Explorer

Une application complète pour explorer des films et des acteurs grâce à la puissance des LLMs (Large Language Models), combinant backend FastAPI, base de données PostgreSQL, Langchain (Groq), et une interface utilisateur avec Streamlit.

---

## 🚀 Fonctionnalités

- 🔍 Rechercher des informations sur des films et acteurs via une API intelligente.
- 🧠 Génération de résumés automatiques avec Langchain + Groq.
- 🌐 API RESTful avec FastAPI.
- 💾 Base de données PostgreSQL avec SQLAlchemy.
- 🎨 Interface utilisateur simple et rapide avec Streamlit.
- 📦 Architecture modulaire et scalable.

---

## 🛠️ Stack Technique

| Technologie    | Rôle                           |
|----------------|--------------------------------|
| FastAPI        | Backend API                    |
| PostgreSQL     | Base de données relationnelle  |
| SQLAlchemy     | ORM pour les modèles Python    |
| Langchain      | Cadre d'orchestration LLM      |
| GroqCloud      | Fournisseur de LLM (via Langchain) |
| Pydantic       | Validation des données         |
| Streamlit      | Interface utilisateur          |
| Docker         | Déploiement et conteneurisation (optionnel) |

---

## 📁 Structure du projet

llm_movie_actor_explorer/
│
├── app/
│ ├── main.py # Entrée FastAPI
│ ├── models.py # Modèles SQLAlchemy
│ ├── schemas.py # Schémas Pydantic
│ ├── database.py # Connexion DB
│ ├── langchain_utils.py # Intégration Groq & Langchain
│ └── routers/
│ ├── movies.py # Endpoints liés aux films
│ └── actors.py # Endpoints liés aux acteurs
│
├── streamlit_app/
│ └── dashboard.py # Interface utilisateur Streamlit
│
├── requirements.txt
├── .env # Variables d’environnement (non versionnées)
└── README.md


## ⚙️ Installation

1. **Cloner le projet :**

```bash
git clone https://github.com/votre-utilisateur/llm-movie-actor-explorer.git
cd llm-movie-actor-explorer


python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows


Installer les dépendances :
pip install -r requirements.txt


Créer une base de données PostgreSQL et configurer les variables dans .env :
DATABASE_URL=postgresql://user:password@localhost:5432/llm_movies
GROQ_API_KEY=your_groq_api_key



Lancer l’API FastAPI :
uvicorn app.main:app --reload


Lancer l’interface utilisateur (Streamlit) :
streamlit run streamlit_app/dashboard.py


🙋‍♂️ Auteur
Développé avec ❤️ par [ Khaled Essghaier ]
