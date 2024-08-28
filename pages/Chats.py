import streamlit as st

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
st.components.v1.html(custom_html)

st.title('Meeting Doctors - Performance Dashboard')

st.subheader('Chat - Indicadores generales')
