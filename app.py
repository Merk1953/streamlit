import streamlit as st
from pages import P0_Contexte_et_enjeux, P1_Analyse_des_données 

def main():

# Masquer le titre de la page
    st.set_page_config(page_title=" ", layout="wide")

# Afficher les onglets dans la barre latérale
    selected_tab = st.sidebar.selectbox("Choisir une page", ["Contexte et enjeux", "Analyse des données"])

# Afficher le contenu de l'onglet sélectionné
    if selected_tab == "Contexte et enjeux":
        P0_Contexte_et_enjeux.contexte()
    elif selected_tab == "Analyse des données":
        P1_Analyse_des_données.analyse()
    

if __name__ == "__main__":
    main()

