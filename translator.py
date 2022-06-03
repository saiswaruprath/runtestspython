"""code to translate english to french and french to english texts"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('p4yDVl-ytrq8ryq2HQDYxSzTjzx7D6idgAVjjt33TFUy')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/4b9bf062-4927-478d-9532-483562ecf014')

def english_to_french(english_text):
    """translates english texts to french"""
    french_translate = language_translator.translate(
    text = english_text,
    model_id='en-fr').get_result()
    return french_translate.get("translations")[0].get("translate")


def french_to_english(french_text):
    """translates english texts to french"""
    english_translate = language_translator.translate(
    text = french_text,
    model_id='fr-en').get_result()
    return english_translate.get("translations")[0].get("translate")
