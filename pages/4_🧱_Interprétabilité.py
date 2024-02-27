import streamlit as st
import pandas as pd
import numpy as np

st.title("Interprétabilité")
st.write("""Maintenant que le modèle de régression linéaire a été sélectionné, il convient de vérifier dans quelle mesure 
         chaque caractéristique contribue au modèle de manière équitable en utilisant SHAP pour améliorer l’interprétabilité. 
         """)
st.write("""Ensuite, nous passerons au PDP pour voir comment la variation d’une caractéristique particulière influence le 
         modèle tout en gardant les autres variables constantes afin de pouvoir visualiser les relations entre une variable 
         spécifique et la sortie du modèle. """)
st.write("""En effet, l'analyse des graphiques PDP constitue une composante essentielle dans l'interprétation des modèles prédictifs, 
         en particulier dans le domaine de l'apprentissage automatique. Ces graphiques fournissent des insights significatifs 
         sur la relation entre les variables d'entrée et la sortie du modèle, permettant ainsi de mieux comprendre 
         le comportement global du modèle.
 """)

st.sidebar.header("Interprétabilité")
choix_inter = st.sidebar.selectbox("", ["Shap", "PDP"])