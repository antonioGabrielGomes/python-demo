# save this as app.py
from flask import Flask, render_template, request, jsonify, send_from_directory
import json
from conversor import text_to_audio
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route("/")
def hello(name=None):
    return render_template('home.html', name=name)


@app.route("/audios", methods=['POST'])
def audio_create():
    if request.method == 'POST':
        data = request.json
        audio = text_to_audio(data['text'])
    
        return jsonify({'mensagem': 'Texto recebido'}), 200
    else:
        return jsonify({'erro': 'Método não permitido'}), 405 


@app.route('/public/<path:path>')
def serve_static(path):
    return send_from_directory('public', path)


if __name__ == '__main__':
    app.run(debug=True)
