import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64

# Créer les onglets
with st.sidebar:
    st.title('Navigation')
    onglet = st.radio("Choisir un onglet", ["Préparation et rappels", "Modèles étudiés", "Onglet 3", "Démo"])

# Afficher le contenu de l'onglet sélectionné
if onglet == "Préparation et rappels":
    st.title("Hypothèses de modélisation")
    st.write("""L'objectif de cette deuxième partie de rapport est d'offrir une analyse approfondie des résultats obtenus lors de la 
             modélisation des temps d'intervention de la brigade des pompiers. Notre approche a englobé un processus rigoureux, 
             débutant par un préprocessing des données et s'étendant jusqu'à l'utilisation de modèles sophistiqués de machine 
             learning. Chaque étape a été étudiée pour garantir la robustesse et la fiabilité des résultats.""")
    
    st.write("""Ces modèles bien que délibérément simplistes, ont joué un rôle crucial en offrant une première perspective 
             sur la dynamique des systèmes sous-jacents.""")
    
   
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
    st.write("""Pour rappel, un premier cleaning des NAs et des heures qui ne sont pas des multiples de 60 
             (d’après la notice de lecture fournie) des deux datasets a produit les résultats suivants""")

    choix_tableau = st.radio("Informations", ["Incidents", "Mobilisations", "Base de travail"])
    if choix_tableau == "Incidents":
        st.write("#### Rappel sur la table des Incidents")
        st.write("- Nombre de lignes : 1 287 593")
        st.write("- Nombre de colonnes : 21")
    
    if choix_tableau == "Mobilisations":
        st.write("#### Rappel sur la table des Mobilisations")
        st.write("- Nombre de lignes : 2 227 677")
        st.write("- Nombre de colonnes : 19")

    if choix_tableau == "Base de travail":
        st.write("#### Description de la base")
        st.write("- Nombre de lignes : 1 237 733")
        st.write("- Nombre de colonnes : 38")
        st.write("""Après la suppression des variables redondantes, 
                 il reste 18 colonnes. Mais après dichotomisation et standardisation, on repasse à 222 colonnes.""")

    
    

elif onglet == "Modèles étudiés":
    st.title("Modèles étudiés")
    choix_reg_non_reg = st.radio("Modèles", ["Modèles non linéaires", "Modèles linéaires", "Résultats"])
    if choix_reg_non_reg == "Modèles non linéaires": 
        st.write(""" Nous avons pris le parti de tester à la fois des modèles non linéaires et des modèles linéaires 
                    du fait des résultats produits lors de la data préparation. """)
        st.write("Les premiers modèles simples étudiés sont les suivants :")

        st.write("""- KNN : pour ce modèle, afin de connaître les contributions des variables, nous avons utilisé une permutation afin d’évaluer leur importance en mesurant 
                 comment le score du modèle change lorsque les valeurs d'une variable sont aléatoirement permutées. 
                 Cela implique de permuter les valeurs de chaque variable de manière aléatoire, recalculer les prédictions du
                 modèle et mesurer comment cela affecte les performances du modèle (par exemple, le score R²).
                 La différence entre les performances avant et après la permutation est utilisée comme mesure de l'importance de la 
                 variable. """)
            
        st.write("- Random Forest : même méthode")
        st.write("- Decision Tree : même méthode")
        st.write("- Gradient Boosting : même méthode")

    if choix_reg_non_reg == "Modèles linéaires":
        st.write("""Pour ce qui est des régressions linéaires, nous pourrions utiliser la même méthode. Cependant, les coefficients 
                 du modèle sont utilisés comme mesure de l’importance des variables. Ils indiquent déjà la contribution de chaque 
                 variable à la prédiction de la variable cible. """)
        st.write("- La régression linéaire : régression linéaire simple")
        st.write("Les régressions Lasso et Ridge permettent de prévenir le surajustement et d’assurer la stabilité du modèle.")
        st.write("""- La régression Lasso : elle intègre une pénalité de norme L1 ce qui peut conduire à une sélection des variables en faisant le split 
                 entre les variables qui ont une contribution nulle sur la prédiction du modèle et celles qui ont un impact 
                 significatif. """)
        st.write("""- La régression Ridge : elle intègre une pénalité de norme L2 qui a tendance à réduire l’impact des variables les moins 
                 importantes plutôt que de les éliminer complètement. Le modèle Ridge est particulièrement utile lorsque les 
                 variables explicatives sont fortement corrélées entre elles, car il permet de stabiliser les coefficients 
                 et d'éviter une sensibilité excessive aux fluctuations dans les données. Etant donné les résultats obtenus 
                 en partie , nous supposons à l’avance que ce modèle ne sera pas d’une grande efficacité.""")
        
    if choix_reg_non_reg=="Résultats": 
        st.write("Les résultats obtenus sont les suivants :")
        st.image("Model/Résultats modèles naifs.png")


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

