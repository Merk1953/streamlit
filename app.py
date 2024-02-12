import streamlit as st
from pages.Contexte_et_enjeux import contexte
from pages.Analyse_des_données import analyse

# Afficher les onglets dans la barre latérale
st.sidebar.markdown("<br>",unsafe_allow_html = True)
page = st.sidebar.radio("", options = ['Contexte', 'Analyse des données'])
# Afficher le contenu de la page sélectionnée
if page == "Contexte":
    contexte()
elif page == "Analyse des données":
    analyse()
