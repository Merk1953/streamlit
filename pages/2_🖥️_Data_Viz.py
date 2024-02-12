import streamlit as st
import pandas as pd
import altair as alt

# Charger les données depuis les fichiers CSV pour les années et les temps d'arrivée
datafile_years1 = "Data/histogram_data_inc.csv"
datafile_years2 = "Data/histogram_data_mob.csv"
datafile_times1 = "Data/histogram_data_inc_duree.csv"
datafile_times2 = "Data/histogram_data_mob_duree.csv"

# Lire les données CSV
df_years1 = pd.read_csv(datafile_years1)
df_years2 = pd.read_csv(datafile_years2)
df_times1 = pd.read_csv(datafile_times1)
df_times2 = pd.read_csv(datafile_times2)

# Sélecteur pour choisir entre les années et les temps d'arrivée
selection = st.sidebar.selectbox("Sélectionner les données à visualiser", ["Années", "Temps d'arrivée"])

# Afficher les histogrammes correspondants en fonction de la sélection
if selection == "Années":
    st.write("### Répartition du nombre d'appels par année")
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

else:
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
