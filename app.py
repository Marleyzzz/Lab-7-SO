from flask import Flask, request, render_template, send_from_directory
import redis
import os

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

# Rute principale
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    text = request.form.get('text', '')
    if not text:
        return render_template('index.html', error="Introduceți un text valid!")
    processed_text = text[::-1]
    redis_client.set('last_text', processed_text)
    return render_template('index.html', original=text, processed=processed_text)

@app.route('/last', methods=['GET'])
def last_text():
    last = redis_client.get('last_text')
    if not last:
        return render_template('index.html', error="Niciun text procesat anterior!")
    return render_template('index.html', last=last)

# Rute pentru resurse statice
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
