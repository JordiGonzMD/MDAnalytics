import streamlit as st
from PIL import Image
# from streamlit_dynamic_filters import DynamicFilters

def MDSetAppCFG():
    st.set_page_config(layout="wide")
    custom_html = """
    <div class="banner">
        <img src="https://meetingdoctors.com/app/themes/custom_theme/build/assets/img/logo_meeting_doctors.png" alt="Banner Image">
    </div>
    <style>
        .banner {
            width: 100%;
            height: 200px;
            overflow: hidden;
            background-color: #001042
        }
        .banner img {
            width: 100%;
            object-fit: cover;
            background-color: #001042
        }
    </style>
    """
    # Display the custom HTML
    # st.components.v1.html(custom_html)

def MDSidebar():
    image = Image.open("Images/Logos/MDLogo.png")
    st.sidebar.image(image)
    st.sidebar.header("Servicios")
    st.sidebar.page_link("pages/Inicio.py", label="Inicio")
    st.sidebar.page_link("pages/Chats.py", label="Chats")
    st.sidebar.page_link("pages/Videocalls.py", label="Videocalls")
    st.sidebar.page_link("pages/NPS.py", label="NPS")

def MDFilters():
    st.sidebar.header("Filtros")
    st.sidebar.multiselect(
        "Año",
        ["2024", "2023", "2022"]
    )
    st.sidebar.multiselect(
        "Mes",
        ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    )
    st.sidebar.multiselect(
        "Grupos de usuario",
        ["Grupo A", "Grupo B", "Grupo C"]
    )
    st.sidebar.multiselect(
        "Especialidad",
        ["Medicina General", "Pediatria", "Dermatologia", "Ginecologia"]
    )

MDSetAppCFG()
MDSidebar()
MDFilters()

st.title('Meeting Doctors Analytics')
st.subheader('NPS - Indicadores generales')