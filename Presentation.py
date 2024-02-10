import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="London Fire Brigade Project",
        page_icon="🎆",
    )

    st.write("# London Fire Brigade Project")

    st.write("La brigade des pompiers de Londres, comme mentionné dans la fiche projet est l’une des plus grandes au monde.")
    st.write("Dans le cadre de notre projet de recherche, nous devrons estimer et analyser les temps de réponse et d’intervention de la brigade.") 
    st.write("Les sources de données utilisées pour répondre à cette problématique proviennent du site ‘London Datastore’ et sont rafraichies sur une base mensuelle.")
    st.write("Elles fournissent le détail des incidents traités depuis janvier 2009.") 


    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
