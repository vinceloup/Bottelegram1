from datetime import datetime
from typing import NoReturn
import requests
import os
from dotenv import load_dotenv
load_dotenv()



def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'slt', 'salut', 'bonjour', 'yo',):
        return "Salut ! Que veux tu savoir ? (répond INFO pour savoir ce que je sais faire"

    if user_message in ('info'):
        return "Pour lheure, répond HEURE, pour la météo à Paris, répond WPARIS, pour celle à Annecy, répond WANNECY"
    
    #if user_message in ('HEURE', 'heure'):
        now = datetime.now
        date_time = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
        return str(date_time)

#MISE EN PLACE DE LA METEO A PARIS

    if user_message in ('WPARIS', 'meteo paris'):

        #on ajoute le token de paris
        url = f"https://api.openweathermap.org/data/2.5/forecast?id={os.environ['2988507']}&" \
              f"APPID={os.environ['f35ffc5f2d13c182cda1d4e3538b0055']}&mode=json&units=metric"
              # puis on ajoute le token du bot telegram

        data = requests.get(url).json()
        weather_message = "Hello Vincent,\n\nLa Meteo du jour est:\n"
        for forecast in data['list'][0:5]:
            time_as_dt = datetime.strptime(forecast['dt_txt'], '%d-%m-%Y %H:%M:%S')
            weather_message += (f"\nTime: {time_as_dt.strftime('%H:%M:%S')}\n"
                        f"Description: {forecast['weather'][0]['description'].title()}\n"
                        f"Teamperature: {int(forecast['main']['temp'])}\n"
                        f"Feels like: {int(forecast['main']['feels_like'])}\n"
                        f"Wind speed: {int(forecast['wind']['speed'] * 3.6)}Kph\n")
        send_message_url = ('https://api.telegram.org/bot' + os.environ['1837463071:AAEgQAJqqyKClQ0G4ln5qKnLUqbOP1IfW9Q'] +
            '/sendMessage?chat_id=' + os.environ['1141677322'] + #ID telegram de vincent (1141677322)
            '&text=' + weather_message.replace(' ', '+').replace('\n', '%0A')) # <- need to replace special characters
        requests.get(send_message_url)
        
        return weather_message








        return 'je ne comprends pas'


