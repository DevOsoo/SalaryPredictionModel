import streamlit as st
import streamlit_authenticator as stauth
from streamlit_login_auth_ui.widgets import __login__
import warnings

from predict_page import show_predict_page
from explore_page import show_explore_page
 


import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "pk_prod_PACD91PXQC4SBGK4EF2P7BT7QCVK", 
                    company_name = "SalaryPredictor",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()


if LOGGED_IN == True:

    page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
    
    if page == "Predict":
     show_predict_page()
    else:       
                 show_explore_page()

# Suppress the specific warning about st.cache deprecation
warnings.filterwarnings("ignore", category=DeprecationWarning, module="streamlit")
