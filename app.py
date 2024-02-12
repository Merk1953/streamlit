import streamlit as st
from pages.Contexte_et_enjeux import contexte
from pages.Analyse_des_données import analyse

st.set_page_config(page_title="Mon application Streamlit", page_icon=":fire:")
# Afficher les onglets dans la barre latérale

page = st.sidebar.radio("", options=['Contexte', 'Analyse des données'])
    
# Afficher le contenu de la page sélectionnée
if page == "Contexte":
    contexte()
    
if page == "Analyse des données":
        analyse()