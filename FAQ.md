❓ Questions / Réponses
1. Quelle est la finalité de cette application ?
Cette application permet d’explorer des informations sur les films et acteurs via une API FastAPI enrichie par l’IA (Langchain + Groq). L’utilisateur peut rechercher, obtenir des résumés intelligents, et consulter les résultats via une interface Streamlit.

2. Qu’est-ce qu’un LLM ? Pourquoi est-il utilisé ici ?
Un LLM (Large Language Model) est un modèle d’IA entraîné sur de grandes quantités de texte. Dans cette application, il permet de générer automatiquement des descriptions ou résumés détaillés de films et acteurs en langage naturel.

3. Quelle est la différence entre FastAPI et Streamlit dans ce projet ?
FastAPI sert de backend, offrant des endpoints REST pour la gestion des données.

Streamlit est utilisé comme frontend, offrant une interface utilisateur simple pour consommer ces endpoints.

4. Pourquoi utiliser Langchain avec Groq ?
Langchain permet d'orchestrer des appels LLM complexes, et Groq propose des modèles très rapides et performants. Ensemble, ils permettent d’enrichir les données textuelles avec de l’intelligence artificielle.

5. Quels types de données sont stockés dans PostgreSQL ?
Les données des films, des acteurs, les relations entre eux, ainsi que les historiques de requêtes (éventuellement) sont stockés dans la base PostgreSQL.

6. Puis-je utiliser un autre LLM que Groq ?
Oui, grâce à Langchain, tu peux facilement basculer vers d’autres fournisseurs LLM (comme OpenAI, Anthropic, Mistral, etc.) en changeant la configuration de la chaîne.

7. Est-ce que l’application est sécurisée ?
La sécurité de base est assurée, mais elle peut être renforcée (authentification, validation, rate limiting, etc.). À l’heure actuelle, l’accès est libre.

8. Comment ajouter un nouveau film ou acteur ?
Via les endpoints API de FastAPI (/movies, /actors) ou en ajoutant un formulaire via l’interface Streamlit.

9. Puis-je déployer cette application ?
Oui. Tu peux la dockeriser avec Docker ou l’héberger séparément :

FastAPI sur un serveur ou avec Uvicorn + Gunicorn

PostgreSQL via un conteneur Docker

Streamlit sur un service comme Streamlit Cloud ou Render

10. Quelles améliorations sont prévues ?
Authentification utilisateur

Fonction de favoris avec un microservice (ex: Spring Boot + MongoDB)

Scraping automatique des films récents

Résumés multimodaux (texte + image)

Tableau de bord analytique