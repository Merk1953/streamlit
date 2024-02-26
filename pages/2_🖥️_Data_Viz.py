import streamlit as st
import pandas as pd
import altair as alt

# Charger les données depuis les fichiers CSV pour les années et les temps d'arrivée
datafile_years1 = "Data/histogram_data_inc.csv"
datafile_years2 = "Data/histogram_data_mob.csv"
datafile_times1 = "Data/histogram_data_inc_duree.csv"
datafile_times2 = "Data/histogram_data_mob_duree.csv"
datafile_hour1 = "Data/histogram_data_inc_hour.csv"
datafile_hour2 = "Data/histogram_data_mob_hour.csv"


# Lire les données CSV
df_years1 = pd.read_csv(datafile_years1)
df_years2 = pd.read_csv(datafile_years2)
df_times1 = pd.read_csv(datafile_times1)
df_times2 = pd.read_csv(datafile_times2)
df_hour1 = pd.read_csv(datafile_hour1)
df_hour2 = pd.read_csv(datafile_hour2)


selection = st.sidebar.radio("Type d' analyse", ["Données", "Croisements", "Tests statistiques"])
# Bloc de texte sur les données temporelles
if selection == "Données":
    st.sidebar.write("### Données")

    # Sélecteur pour choisir entre les données temporelles, les corrélations, et les tests statistiques
    selection_text = st.sidebar.selectbox("Comparatif entre les 2 tables", ["Données temporelles", "Corrélations"])

    if selection_text == "Données temporelles":
        st.write(""" **Les distributions des variables communes aux deux tables semblent similaires. 
                En effet, si l’on met côte à côte les histogrammes des distributions des années ou des heures d'appel
                ou même des temps d'arrivée, on constate visuellement que les distributions se ressemblent même si 
                l'ordre de grandeur est différent.** 
    """)
        selection = st.sidebar.selectbox("Pas de temps", ["Années", "Heure d'appel", "Temps d'arrivée"])

        # Afficher les histogrammes correspondants en fonction de la sélection
        if selection == "Années":
            st.write("### Répartition du nombre d'incidents par année")
            # Tracer les histogrammes des années avec Altair
            histogram_years1 = alt.Chart(df_years1).mark_bar().encode(
                x=alt.X("Modalité:O", title="Année"),
                y=alt.Y("Effectif:Q", title="Effectif"),
                color=alt.value("skyblue")
            ).properties(
                width=300,
                height=400,
                title="Histogramme des incidents par année"
            )

            histogram_years2 = alt.Chart(df_years2).mark_bar().encode(
                x=alt.X("Modalité:O", title="Année"),
                y=alt.Y("Effectif:Q", title="Effectif"),
                color=alt.value("lightgreen")
            ).properties(
                width=300,
                height=400,
                title="Histogramme des mobilisations par année"
            )

            # Afficher les histogrammes des années côte à côte dans Streamlit
            st.write(alt.hconcat(histogram_years1, histogram_years2).configure_axis(
                labelAngle=45
            ))

        elif selection == "Heure d'appel":
            # Tracer les histogrammes des heures d'appel avec Altair
            st.write("### Répartition des heures d'appel")
            histogram_hour1 = alt.Chart(df_hour1).mark_bar().encode(
                x=alt.X("Modalité:O", title="Heure d'appel"),
                y=alt.Y("Effectif:Q", title="Effectif"),
                color=alt.value("skyblue")
            ).properties(
                width=300,
                height=400,
                title="Histogramme des heures d'appel de la table des incidents"
            )

            histogram_hour2 = alt.Chart(df_hour2).mark_bar().encode(
                x=alt.X("Modalité:O", title="Heure d'appel"),
                y=alt.Y("Effectif:Q", title="Effectif"),
                color=alt.value("lightgreen")
            ).properties(
                width=300,
                height=400,
                title="Histogramme des heures d'appel de la table des mobilisations"
            )

            # Afficher les histogrammes des temps d'arrivée côte à côte dans Streamlit
            st.write(alt.hconcat(histogram_hour1, histogram_hour2).configure_axis(
                labelAngle=45
            ))


        elif selection == "Temps d'arrivée":
            # Tracer les histogrammes des temps d'arrivée avec Altair
            st.write("### Répartition des temps d'arrivée")
            histogram_times1 = alt.Chart(df_times1).mark_bar().encode(
                x=alt.X("Modalité:O", title="Temps d'arrivée"),
                y=alt.Y("Effectif:Q", title="Effectif"),
                color=alt.value("skyblue")
            ).properties(
                width=300,
                height=400,
                title="Histogramme des temps d'arrivée des incidents"
            )

            histogram_times2 = alt.Chart(df_times2).mark_bar().encode(
                x=alt.X("Modalité:O", title="Temps d'arrivée"),
                y=alt.Y("Effectif:Q", title="Effectif"),
                color=alt.value("lightgreen")
            ).properties(
                width=300,
                height=400,
                title="Histogramme des temps d'arrivée des mobilisations"
            )

            # Afficher les histogrammes des temps d'arrivée côte à côte dans Streamlit
            st.write(alt.hconcat(histogram_times1, histogram_times2).configure_axis(
                labelAngle=45
            ))
    elif selection_text == "Corrélations":
        st.write("""**Pour aller plus loin dans le croisement de variables, la mesure de corrélation entre celles-ci peut également nous permettre de comprendre 
                les interactions potentielles entre les variables et in fine nous mettre sur la piste des variables à privilégier.*** """)
        st.write("_Il s'agit de corrélations calculées sur la totalité de la table_")
        selection_cor = st.sidebar.selectbox("Table", ["Incidents", "Mobilisations"])
        # Tracer la heatmap de la matrice de corrélation dans Streamlit
        if selection_cor == "Incidents": 
            # Chemin vers l'image
            image_path1 = "Images/matrice_correlation_incidents.png"

            # Afficher l'image dans Streamlit
            st.image(image_path1, caption= "Heatmap des données numériques de la table des incidents", use_column_width=True)
            st.write("""On constate une zone de corrélation forte dans le carré bas et à droite entre le nombre de camions 
                    en intervention, le nombre total de camions, le PumpHoursRoundUp et le Notional Cost. Ces variables forment 
                    un cluster et pourraient par exemple être traitées ensemble. Entre le PumpHoursRoundUp et le Notional Cost, 
                    la corrélation est proche de 1 ce qui est normal car ils ont une relation de type aX. 
                    Il semble y avoir une corrélation nulle dans le reste du carré ce qui indique une absence de relation linéaire entre les variables. 
                    On peut donc postuler que ces variables sont indépendantes les unes des autres. La question se pose maintenant sur la sélection des variables, i.e. si nous allons choisir seulement les variables qui ont une corrélation significative avec la variable cible. 
    """)
        elif selection_cor == "Mobilisations": 
            # Chemin vers l'image
            image_path2 = "Images/matrice_correlation_mobilisations.png"

            # Afficher l'image dans Streamlit
            st.image(image_path2, caption= "Heatmap des données numériques de la table des mobilisations", use_column_width=True)
            st.write("""Comme remarqué précédemment, il y a une très forte corrélation entre le temps de trajet et le temps d’intervention. 
                    On pourrait donc s’intéresser de près à tout ce qui pourrait impacter le temps de trajet notamment les raisons de 
                    retard ou encore si les adresses étaient bonnes ou non. Cependant, ces variables sont très peu renseignées.""")
elif selection == "Croisements": 
    st.sidebar.write("### Croisements")
    selection_rep = st.sidebar.radio("", ["Par type d'incidents", "Par type d'incidents x temps d'intervention", "Localisation et temps d'intervention"])
    if selection_rep == "Par type d'incidents": 

        
        st.write("""On constate que les alarmes incendie automatiques constituent le plus gros contingent de cause de recours 
                 aux pompiers. Viennent ensuite les services spéciaux puis les fausses alertes mais dans une bonne intention, 
                 puis le feu secondaire et enfin le feu primaire  et la fausse alerte dans un but malveillant. 
                 Au final, tout comme précédemment, la répartition reste la même d’une année sur l’autre. Bien que les effectifs
                  changent, les répartitions restent peu ou prou identiques. """)
        st.image("Images/répartition type d'incidents.png",use_column_width=True)
    elif selection_rep == "Par type d'incidents x temps d'intervention": 
        st.write("On a grosso modo un temps d’intervention moyen identique excepté pour le Special Operations Room.") 

        st.write("Un test anova peut nous permettre de valider ou d’invalider statistiquement notre constat.")
        
        st.image("Images/type d'incident x temps d'intervention.png", use_column_width=True)

        st.write("Les résultats sont les suivants avec une p value à 5% :") 
        
        st.write("<div style='text-align: center;'>f statistic: 2045.138681298415</div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'> p_value: 0.0</div>", unsafe_allow_html=True)
        st.write("""
                 
                 """)
        st.write("""**L'ANOVA montre qu'il existe une différence statistiquement significative entre les types d’incidents.
        Cela signifie que le temps d'intervention varie en fonction du type d’incident.**
        """)

        st.write("""<sub id="note">Primary fires are generally more serious fires that harm people or cause damage to property
                  and meet at least one of the following conditions: any fire that occurred in a (non-derelict) building, vehicle or (some) outdoor structures, 
                 or fire that occurred in a (non-derelict) building, vehicle or (some) outdoor structures or 
                fire attended by five or more pumping appliances</sub>""", unsafe_allow_html=True)

        st.write("""<sub id="note">Secondary fires are generally small outdoor fires, not involving people or property. These include refuse fires, grassland fires and fires in derelict buildings or vehicles, unless these fires involved casualties or rescues, or five or more pumping appliances attended, in which case they become primary fires.
            Source: Fire Statistics definitions – GOV.UK
            </sub>
        """, unsafe_allow_html=True)


    elif selection_rep=="Localisation et temps d'intervention": 
        st.write("""La longitude étant une variable manquante prépondérante, on ne peut utiliser les coordonnées GPS afin de 
                 pouvoir avoir une représentation en carte afin de voir les quartiers de Londres où le temps d’intervention 
                 est le plus élevé et pouvoir caractériser les zones de la ville. 
                Pour ce faire, nous sommes obligés de supprimer toutes les lignes avec des coordonnées GPS manquantes. 
                 Les statistiques descriptives de ce subset montrent le résultat suivant : 
""")
        st.image("Images/Map des temps d'intervention.png", use_column_width=True)

        
        

elif selection == "Tests statistiques":
    st.sidebar.write("### Tests statistiques")
    st.write("### On souhaite savoir si le pas de temps fait que les temps d'intervention diffèrent.")

    st.write(""" _L'ANOVA est une technique statistique utilisée pour analyser si les moyennes de trois groupes ou plus sont 
             égales ou différentes dans le contexte de plusieurs groupes ou conditions. 
             C'est un outil précieux dans l'analyse des données pour répondre à des questions telles 
             que "Y a-t-il une différence significative entre les groupes ?" ou 
             "Quel groupe est significativement différent des autres ?"._""" )

    selection_test = st.sidebar.selectbox("", ["Par mois", "Par jour", "Par heure"])
    if selection_test == "Par mois":
        st.image("Images/temps d'intervention par mois.png", use_column_width=True)
        st.write("""On constate avec ces statistiques très simples que, en moyenne le temps d’intervention est quasi identique d’un mois sur l’autre et varie 
                 de 8.2 à  8.5%. S’il n y avait pas eu les légendes, nous aurions pu croire que les éléments du pie chart étaient 
                 identiques.""")
        st.write("""L’analyse du graphique met en exergue une légère différence d’un mois sur l’autre. Un test statistique permettrait 
                 d’avoir une assise plus précise quant à ce constat. Pour cela, nous allons procéder à un test anova.""" )

        st.write("Les résultats sont les suivants avec une p value à 5% :") 
        
        st.write("<div style='text-align: center;'>f statistic: 80.46816007306143</div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'> p_value: 1.120431674796777e-182</div>", unsafe_allow_html=True)
        st.write ("""
                  
                  """)

        st.write("""L'ANOVA montre qu'il existe une différence statistiquement significative entre les mois.
                 Cela signifie que le temps d'intervention varie en fonction du mois de l'année ce qui confirme le constat 
                 précédent qui a été orienté par la représentation en histogramme. """)
    elif selection_test == "Par jour": 
        st.write("La même conclusion est faite en ce qui concerne les jours de la semaine : ")

        st.image("Images/temps d'intervention par jour.png", use_column_width=True)

        st.write("<div style='text-align: center;'>f statistic: 93.45732788231139 </div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'> p_value: 7.238724984128987e-118</div>", unsafe_allow_html=True)
        st.write ("""
                  
                  """)

        st.write("""L'ANOVA montre qu'il existe une différence statistiquement significative entre les jours.
                Cela signifie que le temps d'intervention varie en fonction du jour de la semaine.""")

    elif selection_test == "Par heure": 
        st.image("Images/temps d'intervention par heure.png",  use_column_width=True)

        st.write("<div style='text-align: center;'>f statistic: 423.5404032545424 </div>", unsafe_allow_html=True)
        st.write("<div style='text-align: center;'> p_value: 0.0 </div>", unsafe_allow_html=True)
        st.write ("""
                  
                  """)

        st.write("""L'ANOVA montre qu'il existe une différence statistiquement significative entre les heures.
                Cela signifie que le temps d'intervention varie en fonction de l'heure de la journée. 
                On constate de visu, que le plus gros contingent d’appels a lieu de la fin de matinée jusqu’en fin de soirée. """)
