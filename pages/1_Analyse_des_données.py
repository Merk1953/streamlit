
from typing import Any

import numpy as np
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code
import os

st.set_page_config(page_title="Analyse des données", page_icon="📊")

st.image("Images/Data_analyse.png", width=400)   
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

onglet_selectionne = st.sidebar.radio("Sélectionner un onglet", ["Dictionnaires", "Gestion des NaN", "Statistiques descriptives"])

if onglet_selectionne == "Dictionnaires":
    choix_dictionnaire = st.radio("Dictionnaires", ["Incidents", "Mobilisations"])
    if choix_dictionnaire == "Incidents":
        st.write("#### Contenu du dictionnaire des Incidents")
        st.dataframe(pd.read_csv("Data/Incidents_dico.csv", index_col=0))

        st.write("###### La table contient 2 227 677 entrées.")
        st.write(""" Elle contient des détails sur les incidents traités depuis 2009.Elles incluent des informations 
        importantes telles que la date, le lieu de l’incident et le type d’incident traité. Cette base de données constituera 
        la pierre angulaire de notre analyse car elle nous permet de comprendre la nature des situations auxquelles les pompiers 
        de Londres sont confrontés.  
        Pour information, il y a une colonne supplémentaire dans la table des Incidents (39 colonnes) vs les métadonnées 
        (38 noms de variables). 
        La dernière colonne a donc été supprimée car elle ne semblait correspondre à rien dans les métadonnées.  
        """)
    
    elif choix_dictionnaire == "Mobilisations":
        st.write("#### Contenu du dictionnaire des Mobilisations")
        st.dataframe(pd.read_csv("Data/Mob_dico.csv", index_col=0))

        st.write("###### La table contient : 1 602 834 entrées.")
        st.write(""" Le deuxième jeu de données fournit des informations sur chaque camion de pompiers envoyé sur les lieux d’un incident depuis janvier 2009. Il inclut 
                notamment des détails sur l’appareil mobilisé, son lieu de déploiement et les heures d’arrivées sur les lieux de 
                l’incident.  
        """)

elif onglet_selectionne == "Gestion des NaN":    
    choix_gestion_nan = st.radio("Gestion des NaN", ["Incidents", "Mobilisations", "Synthèse"])
    st.write("""Le pourcentage global des valeurs manquantes pour les incidents est de 12.57% 
             et est  un peu plus bas pour les mobilisations avec 9.66%. Une vision plus détaillée, 
             au niveau variable est nécessaire.""")
    if choix_gestion_nan == "Incidents":
        st.write("#### Analyse des valeurs manquantes dans la table des Incidents")
        st.write(""" On peut classer les NAs en 3 groupes à savoir le groupe de ceux qui ont une valeur très faible (inférieure 
                 à 1%), le groupe de ceux qui ont valeur faible (entre 1 et 15%) et le groupe de ceux qui ont une valeur de NA 
                 significative (plus de 40%) :""")
        st.write("##### Groupe des variables avec un pourcentage de NaN inférieur à 1%")
        st.dataframe(pd.read_csv("Data/NaN/Inc_1.csv", index_col=0))

        st.write("##### Groupe des variables avec un pourcentage de NaN compris entre 1 et 15%")
        st.dataframe(pd.read_csv("Data/NaN/Inc_2.csv", index_col=0))

        st.write("##### Groupe des variables avec un pourcentage de NaN supérieur à 40%")
        st.dataframe(pd.read_csv("Data/NaN/Inc_3.csv", index_col=0))

        st.write("*[1] Il s'agit de la variable à modéliser*")

    elif choix_gestion_nan == "Mobilisations":
        st.write("#### Analyse des valeurs manquantes dans la table des Mobilisations")
        st.write("""La répartition des NAs dans le dataset « Mobilisations » laisse apparaitre une polarisation en ce sens 
                 que l’on a soit de très petites valeurs de NA, entre 0 et 2 %, soit de très grandes valeurs, supérieures à 50%.""") 
        
        st.write("##### Groupe des variables avec un pourcentage de NaN compris entre 0 et 2%")
        st.dataframe(pd.read_csv("Data/NaN/Mob_1.csv", index_col=0))

        st.write("##### Groupe des variables avec un pourcentage de NaN supérieur à 50%")
        st.dataframe(pd.read_csv("Data/NaN/Mob_2.csv", index_col=0))


    elif choix_gestion_nan == "Synthèse":
        st.write("#### Synthèse sur les valeurs manquantes")
        st.write(" La règle de gestion est la suivante :")
        st.write("- Très faibles valeurs de NaN => suppression des lignes concernées")
        st.write("- Très fortes valeurs de NaN => suppression des variables concernées")
        st.write("De plus, parfois certaines variables sont redondantes et apportent la même information.")
        st.write("Voici donc un tableau récapitulatif qui reprend la liste des variables dont on se sépare et en détaille les raisons :")
        st.dataframe(pd.read_csv("Data/NaN/Synt_na.csv", index_col=0))

elif onglet_selectionne == "Statistiques descriptives":    
    choix_gestion_stat = st.radio("Tableau récapitulatif", ["Incidents", "Mobilisations"])

    if choix_gestion_stat == "Incidents":
        st.dataframe(pd.read_csv("Data/Stat_desc_inc.csv", index_col=0))
        st.write("""On constate  qu’en moyenne,  les pompiers mettent 5.25 minutes à arriver sur les lieux de l’incident et 
                 qu’il faut que 1.3 stations envoient un contingent et que cela représente 1.5 camions. 
                La médiane du temps d’intervention reste proche de la moyenne ce qui suggère mois d’asymétrie des données. 
                La moyenne étant une mesure de centralité qui est sensible aux valeurs extrêmes et la médiane étant plus robuste aux valeurs extrêmes, leur proximité suggère que les valeurs aberrantes n’ont pas un impact significatif sur la mesure de la centralité en ce qui concerne le temps d’arrivée. 
""")
        
    if choix_gestion_stat == "Mobilisations":
        st.dataframe(pd.read_csv("Data/Stat_desc_mob.csv", index_col=0))
        st.write(""" On constate que la moyenne du temps d’intervention de la table des Mobilisations est sensiblement proche 
                 de celle de la table des Incidents. Il y va de même pour la médiane. 
                 Les valeurs de la table des Mobilisations semblent juste un peu au-dessus de la celle des Incidents. 	
                 On constate également que Attendance time  = Turnout time + Travel time à savoir Temps d’intervention = Temps de 
                 trajet + Temps de sortie de la station. 
                 La variable qui contribue le plus au temps d’intervention semble être le temps de trajet. 
                 Les distributions des variables communes aux deux tables semblent similaires. 
""")