import streamlit as st
from pages.P0_Contexte_et_enjeux import contexte
from pages.P1_Analyse_des_données import analyse

# Afficher les onglets dans la barre latérale
page = st.sidebar.radio("", options = ['Contexte', 'Analyse des données'])
# Afficher le contenu de la page sélectionnée
if page == "Contexte":
    contexte()
elif page == "Analyse des données":
    analyse()
