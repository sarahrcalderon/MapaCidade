import folium

def criar_mapa(lat, lon, local, temperatura):
    mapa = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker(
        [lat, lon],
        popup=f"{local}: {temperatura}°C"
    ).add_to(mapa)
    return mapa
