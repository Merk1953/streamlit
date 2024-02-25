import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Créer les onglets
with st.sidebar:
    st.title('Navigation')
    onglet = st.radio("Choisir un onglet", ["Préparation et rappels", "Onglet 2", "Onglet 3", "Démo"])

# Afficher le contenu de l'onglet sélectionné
if onglet == "Préparation et rappels":
    st.title("Hypothèses de modélisation")
    st.write("""L'objectif de cette deuxième partie de rapport est d'offrir une analyse approfondie des résultats obtenus lors de la 
             modélisation des temps d'intervention de la brigade des pompiers. Notre approche a englobé un processus rigoureux, 
             débutant par un préprocessing des données et s'étendant jusqu'à l'utilisation de modèles sophistiqués de machine 
             learning. Chaque étape a été étudiée pour garantir la robustesse et la fiabilité des résultats.""")
    
    st.write("""Ces modèles bien que délibérément simplistes, ont joué un rôle crucial en offrant une première perspective 
             sur la dynamique des systèmes sous-jacents""")
    
   
    elements = [
    "Entrainement de modèles naïfs pour ne conserver que les variables qui contribuent le plus au modèle",
    "Réduction de la base aux variables utiles",
    "Gridsearch CV sur plusieurs modèles linéaires et non linéaires sur le dataset nouvellement créé", 
    "Sélection des meilleurs modèles", 
    "Optimisation bayésienne sur les modèles sélectionnés à l’étape précédente"
]
    st.write("Les étapes qui nous ont conduit à la sélection du meilleur modèle sont les suivantes :")
    for element in elements:
        st.write("- " + element)


    st.write("## Préparation et rappels")
elif onglet == "Onglet 2":
    st.write("Contenu de l'onglet 2")
elif onglet == "Onglet 3":
    st.write("Contenu de l'onglet 3")
elif onglet == "Démo":
    
    # Charger le modèle entraîné
    regressor_lin = joblib.load('Model/regressor_lin.joblib')  

    # Variables ProperCase et StopCodeDescription et PropertyCategory
    proper_case_values = ["Barnet", "Bromley", "Camden", "Enfield", "Hillingdon", "Kensington And Chelsea", "Lambeth", "Southwark", "Tower Hamlets"]
    stop_code_description_values = ["AFA", "False alarm - Good intent"]
    property_category_values = ["Non Residential", "Other Residential", "Outdoor", "Road Vehicle"]

    # Mois, année, jour de la semaine et heure de la journée
    #months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]  
    #days_of_week = [1, 2, 3, 4, 5, 6, 7]
    #hours_of_day = list(range(24))

    # Interface utilisateur avec Streamlit
    st.title("Prédiction de la variable cible avec un modèle de régression linéaire")
    st.write("### Entrez les valeurs des variables explicatives :")

    # Variables explicatives temporelles 
    #st.write("Variables explicatives temporelles :")
    #jour_sem_num = st.selectbox("Jour de la semaine (Numéro 1-7)", options=days_of_week)
    #mois = st.selectbox("Mois", options=months)
    #année = st.selectbox("Année", options=years)
    
    #hour_of_call = st.selectbox("Heure d'appel", options=hours_of_day)

    # Variables ProperCase et StopCodeDescription et property category
    st.write("**Variables explicatives de lieu :**")
    proper_case_selected = st.selectbox("Choisissez un qartier de survenance de l'incident", options=proper_case_values)
    stop_code_description_selected = st.selectbox("Choisissez un type d'incident", options=stop_code_description_values)

    st.write("**Variable explicative de type de propriété :**")
    property_category_selected = st.selectbox("Choisissez un type de propriété", options=property_category_values)
   
    # Encodage des variables ProperCase, Mois, Année, Jour de la semaine et Heure de la journée
    proper_case_encoded = [1 if proper_case == proper_case_selected else 0 for proper_case in proper_case_values]
    #mois_encoded = [1 if month == mois else 0 for month in months]
    #année_encoded = [1 if year == année else 0 for year in years]
    #jour_sem_num_encoded = [1 if day == jour_sem_num else 0 for day in days_of_week]
    #hour_of_call_encoded = [1 if hour == hour_of_call else 0 for hour in hours_of_day]
    property_category_encoded = [1 if category == property_category_selected else 0 for category in property_category_values]
    stop_code_description_encoded = [1 if code == stop_code_description_selected else 0 for code in stop_code_description_values]

    # Autres variables explicatives 
    st.write("**Autres variables explicatives :**")
    num_stations = st.number_input(label="Nombre de stations avec pompes intervenantes", min_value=1, max_value=10, step=1, format="%d")
    pump_count = st.number_input(label="Nombre de pompes utilisées", min_value=1, step=1, format="%d")
    pump_hours = st.number_input(label="Nombre d'heures d'intervention (arrondies)", min_value=1, step=1, format="%d")
    turnout_time = st.number_input(label="Temps d'intervention (en secondes)", min_value=60, step=1, format="%d")
    pump_order = st.number_input(label="Numéro de la pompe", min_value=1, step=1, format="%d")

    # Créer un tableau NumPy avec les valeurs saisies par l'utilisateur
    user_input = np.array([[*proper_case_encoded,
                            *property_category_encoded, *stop_code_description_encoded, num_stations, pump_count, pump_hours,
                            turnout_time, pump_order]])

    # Faire une prédiction avec le modèle chargé
    prediction = regressor_lin.predict(user_input)

    # Afficher la prédiction
    st.write("Prédiction de la variable cible :", prediction[0][0])

