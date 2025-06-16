# text_to_speech.py

import requests
import json

API_KEY = "sk_f4434c961bc6bb6b7ce48e162001d4a21490c3ff5cb1f407"#ENTER YOUR ELEVENLABS API KEY
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"

STYLE_SETTINGS = {
    "Default": {"stability": 0.7, "similarity_boost": 0.75},
    "Serious": {"stability": 0.3, "similarity_boost": 0.85},
    "Friendly": {"stability": 0.7, "similarity_boost": 0.95},
    "Aggressive": {"stability": 0.9, "similarity_boost": 0.5},
    "Announcer": {"stability": 0.4, "similarity_boost": 0.9},
}

def generate_tts(text: str, style: str = "Default") -> str:
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
            "stability": settings["stability"],
            "similarity_boost": settings["similarity_boost"]
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        audio_path = "output.wav"
        with open(audio_path, "wb") as f:
            f.write(response.content)
        return audio_path
    else:
        print("TTS API error:")
        print("Status code:", response.status_code)
        print("Response text:", response.text)
        raise Exception(f"Error {response.status_code}: {response.text}")
