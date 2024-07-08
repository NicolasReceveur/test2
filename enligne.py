import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu


# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()


def accueil():
      st.title("Bienvenue sur ma page")
        

if st.session_state["authentication_status"]:
  accueil()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')



# Création du menu qui va afficher les choix qui se trouvent dans la variable options

with st.sidebar:
      # Le bouton de déconnexion
    authenticator.logout("Déconnexion")
    st.write("Bonjour root")
    selection = option_menu(
                menu_title=None,
                options = ["Accueil", "Les photos de mon chat"],
                orientation= "vertical"

            )


# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.write("") 
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwQZco420OYXOQcoiNa_xgumc0KEaCM-qJMQ&s")
elif selection == "Les photos de mon chat":
    st.write("Bienvenue sur mon album de mon chat")
    col1, col2, col3 = st.columns(3)

    with col1:
        
        st.image("https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg?cs=srgb&dl=pexels-pixabay-104827.jpg&fm=jpg")

    with col2:
        
        st.image("https://www.assuropoil.fr/wp-content/uploads/2023/07/avoir-un-chat-sante.jpg")

    with col3:
       
        st.image("https://lemagduchat.ouest-france.fr/images/dossiers/2023-06/mini/chat-cinema-061232-650-400.jpg")
   
   
 