import streamlit as st
import pandas as pd
import numpy as np

st.title("Interprétabilité")
st.write("""Maintenant que le modèle de régression linéaire a été sélectionné, il convient de vérifier dans quelle mesure 
         chaque caractéristique contribue au modèle de manière équitable en utilisant SHAP pour améliorer l’interprétabilité. 
         """)


st.write("## Shap")
st.write(""" Si l’on veut prendre un exemple, quand la valeur SHAP associée à une modalité particulière d'une variable 
             augmente, cela signifie que la présence ou l'augmentation de cette modalité a une contribution positive à la 
             prédiction du modèle par rapport à la valeur moyenne de la variable cible. En d'autres termes, cette modalité est 
             associée à une augmentation de la variable cible (dans notre cas, le temps d'intervention en secondes).""")
     
    
choix_rep = st.radio('', ['Tableau des magnitudes', 'Histogramme horizontal', 'Graphique Shap', 'Echantillons'])
if choix_rep =='Tableau des magnitudes':
    st.write(""" Il convient de regarder dans quelle mesure chaque ligne de notre set de données contribue à la prédictibilité 
                du modèle. De ce fait, on utilisera la magnitude pour mesurer l'impact global de cette caractéristique sur 
                la sortie du modèle, en tenant compte de toutes les observations dans l'ensemble de données.""")
    st.dataframe(pd.read_csv("Model/Contributions shap.csv", index_col=0))

    st.write("Mis en parallèle avec le graphique des features importances (plus parlant): ")
    
if choix_rep =='Histogramme horizontal':
    st.image("Model/feature importances.png", use_column_width=True)


    # Fonction pour afficher les informations
    def afficher_info(numero, titre, magnitude, description):
        if magnitude is not None:
            magnitude_str = format(magnitude, ',').replace(',', ' ')
            st.write(f"**{numero}. {titre} ({magnitude_str}):**")
        else:
            st.write(f"**{numero}. {titre} :**")
        st.write(description)
        st.write("")

    # Affichage
    infos = [
        (1, "TurnoutTimeSeconds", 3_799_423.15, "Avec la magnitude SHAP la plus élevée, cette variable est la plus déterminante pour le modèle. Cela signifie que le temps écoulé depuis l'appel jusqu'à l'arrivée de la brigade des pompiers est le facteur le plus significatif pour prédire le temps d'intervention."),
        (2, "PumpCount", 3_745_790.27, "Cette variable a une magnitude SHAP très proche de celle de TurnoutTimeSeconds, ce qui indique qu'elle est également très influente dans la prédiction du temps d'intervention. Le nombre de pompes utilisées pendant l'intervention semble avoir un impact significatif sur la durée totale de l'intervention."),
        (3, "NumStationsWithPumpsAttending", 2_454_214.28, "Bien que légèrement inférieure en magnitude par rapport à PumpCount, cette variable reste très importante dans la prédiction du temps d'intervention. Elle suggère que le nombre de stations avec des pompes intervenantes est un facteur clé pour prédire la durée de l'intervention."),
        (4, "PumpOrder", 2_319_695.67, "Cette variable a une magnitude SHAP élevée, mais légèrement inférieure à celle de NumStationsWithPumpsAttending. Cela implique que l'ordre dans lequel les pompes sont utilisées peut également avoir une influence significative sur le temps d'intervention."),
        (5, "Variables ProperCase et PropertyCategory", None, "Ces variables ont des magnitudes SHAP variées mais toutes sont significatives. Cela suggère que la localisation géographique (ProperCase) et la catégorie de propriété (PropertyCategory) jouent un rôle important dans la prédiction du temps d'intervention des pompiers."),
        (6, "StopCodeDescription", None, "Les différents types d'incidents ont également des magnitudes SHAP élevées, indiquant qu'ils sont des prédicteurs importants du temps d'intervention. Cela signifie que le type d'incident peut avoir une influence significative sur la durée de l'intervention."),
        (7, "PumpHoursRoundUp", 7_155.64, "Cette variable a la magnitude SHAP la plus faible parmi toutes, mais elle reste significative. Cela pourrait indiquer que le nombre d'heures d'intervention (arrondi) a une influence moindre sur le temps d'intervention par rapport aux autres variables.")
    ]

        
    for info in infos:
        afficher_info(*info)

    st.write(""" On peut conclure en disant que la caractéristique qui contribue le plus au modèle qui permet de prédire le temps d’intervention est le temps entre le moment où l’alerte arrive à la caserne et le moment où les pompiers partent.
                  En effet, il semble logique que la caractéristiques de temps de réponse influence considérablement le temps 
                 d’intervention. """)
        
    st.write("""Vient ensuite le nombre de pompes utilisées. En effet, plus il y a de pompes près du lieu d’incident,
                plus grandes seront les chances de diminuer le temps d’intervention.""")
        
    st.write("""Dans une moindre mesure, le nombre de stations intervenant contribue également en ce sens que plus de stations 
             seront contactées, plus grandes seront les chances de diminuer le temps d’intervention. """)


    st.write("""Parmi les quartiers conservés, la plupart sont des quartiers centraux autour de la Tamise à l’exception de 
             3 qui sont à la périphérie et vastes. Les quartiers les plus centraux sont ceux qui contribuent le plus. 
             On peut penser qu'une localisation de l'incident en centre-ville contribue plus à la prédictabilité de la 
             variable cible que les quartiers périphériques.  """)        

if choix_rep == "Graphique Shap":
        st.image('Model/feature importances 2.png', use_column_width=True)

    st.write("""Pour faire écho à ce qui a été dit précédemment sur la variable _TurnoutTimeSeconds_, on constate à quel point elle peut 
                 contribuer aussi bien à la hausse et à la baisse au temps d’intervention. A l’instar de _TurnoutTimeSeconds_, 
                le graphique montre la grande amplitude d’influence qu’a aussi la variable du nombre de pompes à l’intervention. 
                 Elle contribue très positivement et très négativement également. Cela signifie que la variable à expliquer 
                 est très sensible à cette dernière et rejoint le point évoqué sur la magnitude. """)
        
if choix_rep =="Echantillons":
    st.write("""On constate que sur 5 échantillons, la variable _TurnoutTime_ contribue le plus en valeur absolue. Idem 
                 pour le nombre de pompes. Cela conforte la conclusion faite au niveau macro. En fait, toutes les autres 
                 variables se comportent comme dans le graphique précédent. """)
    st.image("Model/feature importances sample.png", use_column_width=True)
