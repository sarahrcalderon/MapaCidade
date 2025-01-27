import streamlit as st
from streamlit_folium import folium_static
from app.utils import obter_lat_lon, obter_temperatura_atual
from app.mapa import criar_mapa

def run_app():
    st.title("Busca de Temperatura no Mapa Mundial")
    st.write("Digite uma cidade, país ou estado para ver a temperatura atual no mapa.")

    local = st.text_input("Digite uma cidade, país ou estado:")

    if local:
        # latitude e longitude
        lat, lon = obter_lat_lon(local)
        if lat and lon:
            temperatura = obter_temperatura_atual(lat, lon)
            if temperatura:
                st.success(f"Temperatura atual em {local}: {temperatura}°C")

                mapa = criar_mapa(lat, lon, local, temperatura)
                folium_static(mapa)
            else:
                st.error("Não foi possível obter os dados de temperatura. Tente novamente.")
        else:
            st.error("Local não encontrado. Tente novamente.")
