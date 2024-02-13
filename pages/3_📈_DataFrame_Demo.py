import streamlit as st
import pandas as pd
import numpy as np

# Définir une fonction pour convertir les variables 'property' en valeurs numériques
def convert_to_numeric(df):
    property_cols = [col for col in df.columns if col.startswith('property')]
    df[property_cols] = df[property_cols].astype(int)
    return df

# Créer les onglets
with st.sidebar:
    st.title('Navigation')
    onglet = st.radio("Choisir un onglet", ["Onglet 1", "Onglet 2", "Onglet 3", "Démo"])

# Afficher le contenu de l'onglet sélectionné
if onglet == "Onglet 1":
    st.write("Contenu de l'onglet 1")
elif onglet == "Onglet 2":
    st.write("Contenu de l'onglet 2")
elif onglet == "Onglet 3":
    st.write("Contenu de l'onglet 3")
elif onglet == "Démo":
    
    df = pd.read_csv("Data/features3.csv")
    
    df['PropertyCategory_Non Residential'] = df['PropertyCategory_Non Residential'].astype(int)
    df['PropertyCategory_Other Residential'] = df['PropertyCategory_Other Residential'].astype(int)
    df['PropertyCategory_Outdoor'] = df['PropertyCategory_Outdoor'].astype(int)
    df['PropertyCategory_Road Vehicle'] = df['PropertyCategory_Road Vehicle'].astype(int)
    y_train = pd.read_csv("Data/target3.csv")
    y_train = y_train.apply(pd.to_numeric, errors='coerce')

    # Afficher le formulaire pour entrer les valeurs des variables explicatives
    st.title("Prédiction de la variable cible avec un modèle de régression linéaire")
    st.write("Entrez les valeurs des variables explicatives :")

    cal_year = st.number_input(label="Année", key="cal_year",min_value = 2009, step=1, format="%d")
    hour_of_call = st.number_input(label="Heure d'appel", key="hour_of_call", min_value = 0, step=1, format="%d")
    num_stations = st.number_input(label="Nombre de stations avec pompes intervenantes", key="num_stations", min_value = 1, max_value = 10,step=1, format="%d")
    pump_count = st.number_input(label="Nombre de pompes", key="pump_count", min_value = 1, step=1, format="%d")
    pump_hours = st.number_input(label="Nombre d'heures de pompage (arrondies)", key="pump_hours", min_value = 1, step=1, format="%d")
    turnout_time = st.number_input(label="Temps d'intervention (en secondes)", key="turnout_time", min_value = 60, step=1, format="%d")
    pump_order = st.number_input(label="Ordre de la pompe", key="pump_order", min_value = 1, step=1, format="%d")
    property_category_non_residential = st.number_input(label="Catégorie de propriété (non résidentiel 0 : Non,  1 : Oui)", key="property_category_non_residential", step=1, format="%d")
    property_category_other_residential = st.number_input(label="Catégorie de propriété (autre résidentiel 0 : Non,  1 : Oui)", key="property_category_other_residential", step=1, format="%d")
    property_category_outdoor = st.number_input(label="Catégorie de propriété (extérieur 0 : Non,  1 : Oui)", key="property_category_outdoor",step=1, format="%d")
    property_category_road_vehicle = st.number_input(label="Catégorie de propriété (véhicule routier 0 : Non,  1 : Oui)", key="property_category_road_vehicle", step=1, format="%d")

    # Créer un tableau NumPy avec les valeurs saisies par l'utilisateur
    user_input = np.array([[cal_year, hour_of_call, num_stations, pump_count, pump_hours, turnout_time,
                            pump_order, property_category_non_residential, property_category_other_residential,
                            property_category_outdoor, property_category_road_vehicle]])

    # Charger les données cibles
    y_train = y_train["FirstPumpArriving_AttendanceTime"].values

    # Charger le modèle de régression linéaire
    class LinearRegression:
        def fit(self, X, y):
            self.coefficients = np.linalg.lstsq(X, y, rcond=None)[0]

        def predict(self, X):
            return np.dot(X, self.coefficients)

    # Instancier et entraîner le modèle
    model = LinearRegression()
    model.fit(df.values, y_train)

    # Prédire la variable cible pour les valeurs saisies par l'utilisateur
    prediction = model.predict(user_input)

    # Afficher la prédiction
    st.write("La prédiction de la variable cible (FirstPumpArriving_AttendanceTime) est :", prediction[0])
