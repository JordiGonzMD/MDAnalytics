import streamlit as st
from PIL import Image
# from streamlit_dynamic_filters import DynamicFilters

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
image = Image.open("Images/Logos/MDLogo.png")
# Display the custom HTML
st.components.v1.html(custom_html)

st.title('Meeting Doctors - Performance Dashboard')

st.sidebar.image(image)
# st.sidebar.header("Company name")
st.sidebar.checkbox("Test")

st.markdown(
    """
        ### Bienvenido a MD Analytics
        MD Analytics es un app mediante que permite el seguimiento y análisis básico de los distintos servicios contratados.

        👈 Mediante este selector puede seleccionar el servicio que deseas analizar

        **IMPORTANTE: Este dashboard no dispone de datos real-time.** Los datos a analizar siempre son hasta último día cerrado

        *Si tienes cualquier duda o incidencia con el dashboard, ponte en contacto con nuestro equipo de [data](mailto:data@meetingdoctors.com)*
    """
  )