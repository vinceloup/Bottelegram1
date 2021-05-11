from datetime import datetime
from typing import NoReturn

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'slt', 'salut', 'bonjour', 'yo',):
        return "Salut ! Que veux tu savoir ? (répond INFO pour savoir ce que je sais faire"

    if user_message in ('info'):
        return "Pour lheure, répond HEURE, pour la météo à Paris, répond WPARIS, pour celle à Annecy, répond WANNECY"
    
    if user_message in ('HEURE', 'heure'):
        now = datetime.now
        date_time = now.strftime("%H:%M:%S ")
        return str(date_time)
    
    return 'je ne comprends pas'


