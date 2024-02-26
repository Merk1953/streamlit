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



# Bloc de texte sur les données temporelles
st.sidebar.write("### Données")

# Sélecteur pour choisir entre les données temporelles, les corrélations, et les tests statistiques
selection_text = st.sidebar.selectbox("Comparatif des données entre les 2 tables", ["Données temporelles", "Corrélations"])

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


st.sidebar.write("### Tests statistiques")


