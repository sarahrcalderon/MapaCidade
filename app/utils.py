import os
import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("Erro: A chave da API não foi encontrada. Configure-a no arquivo .env.")

def obter_lat_lon(local):
    geolocator = Nominatim(user_agent="geo_locator")
    try:
        resultado = geolocator.geocode(local)
        if resultado:
            return resultado.latitude, resultado.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None

def obter_temperatura_atual(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        return dados["main"]["temp"]
    else:
        return None
