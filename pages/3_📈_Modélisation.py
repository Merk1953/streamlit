import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64
from sklearn.preprocessing import StandardScaler

# Créer les onglets
with st.sidebar:
    st.title('Navigation')
    onglet = st.radio("Choisir un onglet", ["Préparation et rappels", "Modèles étudiés", "Démo"])

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
        st.write("- Nombre de colonnes : 24")
    
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
    choix_reg_non_reg = st.radio("Modèles", ["Modèles non linéaires", "Modèles linéaires"])
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
        
    choix_res = st.radio("Résultats", ["Modèles naïfs", "Contributions", "Gridsearch", "Optimisation bayésienne"])
    
    if choix_res == "Modèles naïfs": 
        st.write("Les résultats obtenus sont les suivants :")
        st.dataframe(pd.read_csv("Model/Resultats_modeles_naifs.csv", index_col=0))
        st.write("""Il faut garder à l’esprit que les régressions linéaires et non linéaires ne sont pas réalisées sur des 
                 échantillons de tailles équivalentes (~10k lignes pour les modèles non linéaires et toute la base pour les modèles 
                 linéaires""")
        st.write("**Aucun modèle non linéaire ne semble produire de bons résultats. Surapprentissage, R2 négatifs…**")
        st.write("""Pour ce qui est des modèles linéaires, ils semblent tous montrer les mêmes résultats. Le modèle Lasso est celui qui présente le moins de surapprentissage. 
        Les R2 sont très bas mais le but de cette première étape de trouver les variables les plus contributives. Le modèle Lasso,
                  de par la pénalité qu’il utilise nous permet de constater quelles sont les variables qui contribuent le plus 
                 au modèle et vont nous permettre in fine d’affiner nos travaux.   """)
    if choix_res == "Contributions":
        st.write("En nous fiant au modèle Lasso simple pour les régresseurs linéaires, on constate qu’en réalité, peu de variables (par rapport au nombre initial) contribuent au modèle : ")
        st.dataframe(pd.read_csv("Model/Contributions variables.csv", index_col=0)) 
        
    if choix_res == "Gridsearch": 
        st.write(""" Les modèles dits naïfs ont servi de point de départ, offrant une compréhension initiale des relations 
                 linéaires et non linéaires entre les variables explicatives et les temps d'intervention.""")
        st.write("""Nous allons donc procéder à une optimisation approfondie des hyperparamètres, via le GridsearchCV  
                 pour garantir la performance du modèle avec une réduction drastique des dimensions et ce sur tous 
                 les modèles précédemment écartés dans l’optique de trouver les meilleurs modèles pour résoudre notre 
                 problématique.  La totalité de la base a été utilisée.""") 
        st.image("Model/Gridsearch.png", use_column_width=True)
        st.write("""On constate que les 3 modèles produisent peu ou prou les mêmes résultats. modèles linéaires sont ceux qui 
                 fournissent les meilleurs résultats compte tenu des postulats de départ. 
                Nous allons donc procéder à une optimisation bayésienne sur ces derniers, avec les variables sélectionnées.  
""")

    if choix_res == "Optimisation bayésienne":
        st.image("Model/Optimisation bayésienne.png", use_column_width=True)

        st.write("""Le tableau montre que les performances des 3 modèles sont identiques. 
                 Une cross validation opérée entre les 3 modèles avec les hyperparamètres alpha optimaux n’a guère permis 
                 de faire la différence. """)
        

        st.write("**Régression Linéaire - Scores de validation croisée: [0.11237435 0.09124155 0.07112321 0.08179717 0.08109262]**")
        st.write("_Moyenne des scores: 0.08752578036176409_")
        st.write("**Lasso - Scores de validation croisée: [0.11235916 0.09123184 0.07113139 0.08180792 0.08109975]**")
        st.write("_Moyenne des scores: 0.08752601128969313_")
        st.write("**Ridge - Scores de validation croisée: [0.11237435 0.09124155 0.07112321 0.08179717 0.08109262]**")
        st.write("_Moyenne des scores: 0.08752578036210472_") 

        st.write("""Le seul critère de ségrégation serait celui du temps de traitement. Le modèle de régression linéaire simple est celui qui produit des résultats le 
                 plus rapidement. Il convient de rappeler que le dataset de départ a dû être amputé de beaucoup de variables et 
                 d’observations. En outre, les variables utilisées dans les modèles ne sont pas très parlantes en termes d’information
                  orientée. """)


elif onglet == "Démo":
    
    
    # Chargement du modèle
    regressor_lin = joblib.load('Model/regressor_lin.joblib')

    # Variables ProperCase et StopCodeDescription et PropertyCategory
    proper_case_values = ["Barnet", "Bromley", "Camden", "Enfield", "Hillingdon", "Kensington And Chelsea", "Lambeth", "Southwark", "Tower Hamlets"]
    stop_code_description_values = ["AFA", "False alarm - Good intent"]
    property_category_values = ["Non Residential", "Other Residential", "Outdoor", "Road Vehicle"]

    # Variables explicatives de lieu et type de propriété
    st.title("Prédiction de la variable cible avec un modèle de régression linéaire")
    st.write("### Entrez les valeurs des variables explicatives :")

    proper_case_selected = st.selectbox("Choisissez un qartier de survenance de l'incident", options=proper_case_values)
    stop_code_description_selected = st.selectbox("Choisissez un type d'incident", options=stop_code_description_values)
    property_category_selected = st.selectbox("Choisissez un type de propriété", options=property_category_values)

    # Encodage des variables ProperCase, StopCodeDescription et PropertyCategory
    proper_case_encoded = [1 if proper_case == proper_case_selected else 0 for proper_case in proper_case_values]
    stop_code_description_encoded = [1 if code == stop_code_description_selected else 0 for code in stop_code_description_values]
    property_category_encoded = [1 if category == property_category_selected else 0 for category in property_category_values]


    # Autres variables explicatives
    st.write("**Autres variables explicatives :**")

    # Collecte des variables
    num_stations = st.number_input(label="Nombre de stations avec pompes intervenantes", min_value=1, max_value=10, step=1, format="%d", key="num_stations")
    pump_count = st.number_input(label="Nombre de pompes utilisées", min_value=1, step=1, format="%d", key="pump_count")
    pump_hours = st.number_input(label="Nombre d'heures d'intervention (arrondies)", min_value=1, max_value=24*60, step=1, format="%d", key="pump_hours") * 60
    notional_cost = st.number_input(label="Coût notionnel (£)", min_value=0.0, step=1.0, format="%.2f", key="notional_cost")
    turnout_time = st.number_input(label="Temps d'intervention (en secondes)", min_value=60, step=1, format="%d", key="turnout_time")

  
    user_input = np.array([[*proper_case_encoded, *property_category_encoded, *stop_code_description_encoded]])

    means_dict = {
    'num_stations': 1.311029,
    'pump_count': 1.480532,
    'pump_hours': 60.275488,
    'notional_cost': 311.731550,
    'turnout_time': 78.760321
}

    stds_dict = {
    'num_stations': 0.556083,
    'pump_count': 0.694558,
    'pump_hours': 27.297307,
    'notional_cost': 143.869867,
    'turnout_time': 45.250354
}

    def standardize_user_input(user_input, means_dict, stds_dict):
        standardized_user_input = {}
        for variable, value in user_input.items():
            if variable in means_dict and variable in stds_dict:
                mean = means_dict[variable]
                std = stds_dict[variable]
                standardized_value = (value - mean) / std
                standardized_user_input[variable] = standardized_value
            else:
                standardized_user_input[variable] = value  
        return standardized_user_input

    # Collecte des variables d'entrée de l'utilisateur
    user_input2 = {
        'num_stations': num_stations,
        'pump_count': pump_count,
        'pump_hours': pump_hours,
        'notional_cost': notional_cost,
        'turnout_time': turnout_time
    }


    standardized_user_input = standardize_user_input(user_input2, means_dict, stds_dict)
    standardized_values = np.array(list(standardized_user_input.values()))

 
    standardized_values_reshaped = standardized_values.reshape(1, -1)
    user_input_scaled = np.concatenate((user_input, standardized_values_reshaped), axis=1)

    
    # Prédiction avec le modèle chargé
    prediction = regressor_lin.predict(user_input_scaled)
  
    # Affichage
    st.write("**Prédiction de la variable cible :**", prediction[0][0])

