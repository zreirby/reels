# text_to_speech.py

import requests
import json

API_KEY = "sk_c8aec745b265e14620c932769e4efb26a26a2ee102f207d7"#ENTER YOUR ELEVENLABS API KEY
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"

STYLE_SETTINGS = {
    "Default": {"stability": 0.7, "similarity_boost": 0.75},
    "Serious": {"stability": 0.3, "similarity_boost": 0.85},
    "Friendly": {"stability": 0.7, "similarity_boost": 0.95},
    "Aggressive": {"stability": 0.9, "similarity_boost": 0.5},
    "Announcer": {"stability": 0.4, "similarity_boost": 0.9},
}

def generate_tts(text: str, style: str = "Default") -> str:
    # Your text-to-speech code here
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    settings = STYLE_SETTINGS.get(style, STYLE_SETTINGS["Default"])

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        audio_path = "output.wav"
        with open(audio_path, "wb") as f:
            f.write(response.content)
        return audio_path
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
