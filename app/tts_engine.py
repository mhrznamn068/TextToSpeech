from flask import Flask, request, jsonify
import pyttsx3
import os

app = Flask(__name__)

class TextToSpeechEngine:
    def __init__(self):
        self.engine = pyttsx3.init()

    def text_to_speech(self, text, file_path):
        # Set properties (optional)
        # You can set various properties like rate, volume, voice, etc.
        # self.engine.setProperty('rate', 150)  # Speed of speech
        # self.engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

        # Convert text to speech
        self.engine.save_to_file(text, file_path)

        # Wait for the speech to finish
        self.engine.runAndWait()

        print(f"Speech saved as {file_path}")

engine_instance = TextToSpeechEngine()

@app.route('/tts', methods=['POST'])
def convert_text_to_speech():
    try:
        data = request.get_json()
        text = data.get('text', '')
        file_name = 'output.mp3'  # You can customize the file name if needed
        file_path = os.path.join('/tmp/audio/', file_name)

        engine_instance.text_to_speech(text, file_path)

        response = {
            'success': True,
            'message': 'Text converted to speech successfully.',
            'file_path': file_path
        }

    except Exception as e:
        response = {
            'success': False,
            'message': str(e),
            'file_path': None
        }

    return jsonify(response)

