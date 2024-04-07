import streamlit as st

st.image("Images/conclusion.png", width=500) 

st.header("Conclusion")

st.write("""Il convient de rappeler avant toute chose que la data quality des datasets pour construire le modèle final n’était
          pas très riche. En effet, beaucoup de variables redondantes et manquantes ont contribué à appauvrir l’information 
         disponible pour construire un modèle robuste et fiable.  """)

st.write("""De plus, les dictionnaires de données ne fournissaient pas de définition claire et ferme et il a fallu 
         aller ‘fouiller’, regarder les modalités de chaque variable afin d’essayer de comprendre et d’affiner un peu 
         plus la définition des champs. """)

st.write("""La première partie du travail, la data préparation a permis d’émettre dès le début le postulat que le modèle ne 
         serait pas très riche en ce sens que la suppression de beaucoup de champs et de lignes d’observations allaient 
         amoindrir la robustesse du modèle.  """)


st.write("""La seconde partie de l’étude a consisté à tâtonner avec des modèles naïfs en première intention afin d’avoir 
         des pistes de réflexion et d’améliorer de proche en proche les modèles étudiés. """)

st.write("""En effet, les modèles ‘naïfs’ ont permis de voir la contribution des variables et d’éliminer celles qui ne 
         participaient peu ou pas du tout au modèle. Le corollaire de cela est que la taille des datasets utilisés a pu
          être augmentée et ainsi améliorer la prédictibilité du modèle (toutes proportions gardées). """)

st.write("""Un Gridsearch sur des modèles linéaires et non linéaires avec les variables préalablement sélectionnées a permis 
         de conserver deux modèles qui fournissaient la meilleure combinaison en termes de minimisation de l’erreur, 
         d’évitement du surapprentissage et d’augmentation de l’ajustement du modèle aux données. """)

st.write("""C’est finalement un modèle linéaire (Lasso) qui a été sélectionné et a montré par le biais des magnitudes de 
         SHAP que les contributions des variables au modèle étaient pour la plupart assez intuitives. """)


def afficher_piste(piste):
    st.write(f"**{piste[0]}. {piste[1]} :**")
    st.write(piste[2])

def main():

    st.write('Idéalement, le processus aurait pu être le suivant :')
 
    pistes = [
        (1, "Analyse approfondie des données", "Évaluer la qualité des données pour identifier les lacunes et les erreurs."),
        (2, "Imputation judicieuse", "Remplir les données manquantes en utilisant des techniques adaptées pour préserver la distribution des données."),
        (3, "Traitement des valeurs aberrantes", "Détecter et traiter les valeurs extrêmes pour éviter les biais dans les modèles."),
        (4, "Normalisation et standardisation", "Mettre à l'échelle les données pour les rendre comparables et conformes aux hypothèses du modèle."),
        (5, "Choix de modèles robustes", "Opter pour des techniques de modélisation plus tolérantes aux données incomplètes."),
        (6, "Collecte ciblée de données", "Si possible, compléter l'ensemble de données avec des données supplémentaires pertinentes."),
        (7, "Consultation des experts du domaine", "Collaborer avec les experts pour comprendre la signification des données et identifier les meilleures pratiques.")
    ]

    for piste in pistes:
        afficher_piste(piste)

if __name__ == "__main__":
    main()

st.header("Piste de réflexion")

st.write("""Lors de l'analyse de données, il est courant de rencontrer des ensembles de données incomplets, incohérents ou mal
          renseignés. Ces données peuvent grandement affecter la performance et la fiabilité des modèles d'apprentissage 
         automatique, rendant ainsi les prédictions peu parlantes ou peu fiables. Face à de telles situations, plusieurs 
         pistes de réflexion peuvent être explorées pour améliorer la qualité des données et, par conséquent, des modèles.""")



def main_fin():
    

    texte = """
    En tant que producteur de données, la qualité de l'information qui est fournie est essentielle pour garantir la pertinence et la fiabilité des données. De fait, face à des données de mauvaise qualité, plusieurs pistes de réflexion peuvent être envisagées :

    1. **Évaluation et Transparence :** Fournir une évaluation transparente de la qualité des données, en identifiant les lacunes et les erreurs, afin de maintenir la confiance des utilisateurs.

    2. **Amélioration des Processus de Collecte :** Réviser et améliorer les processus de collecte des données pour minimiser les erreurs et garantir leur exactitude dès le départ.

    3. **Formation et Sensibilisation :** Sensibiliser le personnel aux enjeux de qualité des données et fournir une formation appropriée sur les bonnes pratiques de collecte et de gestion des données.

    4. **Implémentation de Contrôles Qualité :** Mettre en place des contrôles qualité rigoureux tout au long du processus de collecte et de traitement des données pour détecter et corriger les erreurs rapidement.

    5. **Collaboration avec les Utilisateurs :** Impliquer activement les utilisateurs dans l'identification et la résolution des problèmes de qualité des données, en recueillant leurs commentaires et leurs suggestions d'amélioration.

    6. **Fourniture des Métadonnées :** Mettre à disposition des utilisateurs un dictionnaire de données clair et intelligible.
    
    """

    st.markdown(texte, unsafe_allow_html=True)

if __name__ == "__main__":
    main_fin()
