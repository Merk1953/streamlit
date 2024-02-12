import streamlit as st
from pages import P0_Contexte_et_enjeux, P1_Analyse_des_données 

def main():
    st.sidebar.title("Agenda")
    page = st.sidebar.radio("Choisissez une page", options=["Contexte et enjeux", "Analyse des données"])

# Afficher le contenu de la page sélectionnée
    if page == "Contexte et enjeux":
        P0_Contexte_et_enjeux.contexte()
    elif page == "Analyse des données":
        P1_Analyse_des_données.analyse()

if __name__ == "__main__":
    main()

