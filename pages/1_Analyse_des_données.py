
from typing import Any

import numpy as np
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code
import os

st.set_page_config(page_title="Analyse des données", page_icon="📊")

   
st.markdown("# Analyse des données")
st.sidebar.header("Données à disposition")
st.write(
    """L'étape primordiale avant une data visualisation est la compréhension des données : 
       nous disposions de 2 datasets avec chacun leur métadonnées. 
""")

st.write(
    """L'un fournissant des informations sur les incidents : heure d'arrivée, type d'incident, localisation de l'incident 
    etc. et l'autre contenant des informations sur les mobilisations à savoir la date d'arrivée sur les lieux de l'incident, 
    les raisons d'un éventuel retard etc. 
"""
)

st.write(
    """L'analyse des métadonnées a permis d'aboutir aux dictionnaires de données présents dans la sidebar. Il convient néanmoins 
    de rappeler que certaines fois, malgré les différents croisements opérés pour appréhender les variables, il n'a pas été 
    possible de les comprendre réellement.  
"""
)

chemin_dossier = "C:/Users/rymat"
nom_fichier_inc = "Incidents_dico.csv"
chemin_fichier_inc = os.path.join(chemin_dossier, nom_fichier_inc)


onglet_selectionne = st.sidebar.radio("Dictionnaires", ["Incidents", "Mobilisations"])
if onglet_selectionne == "Incidents":
    st.write("#### Contenu du dictionnaire des Incidents")
    df_inc = pd.read_csv("Incidents_dico.csv")
#st.table(df_inc)
if onglet_selectionne == "Mobilisations":
    st.write("#### Contenu du dictionnaire des Mobilisations")

