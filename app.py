from flask import Flask, jsonify, render_template
import json
import random

app = Flask(__name__)

# Load affirmations from JSON file
def load_affirmations():
    with open('affirmations.json', 'r') as file:
        data = json.load(file)
        return data['affirmations']

@app.route('/api/hello', methods=['GET'])
def hello_world_api():
    affirmations = load_affirmations()
    random_affirmation = random.choice(affirmations)
    return jsonify(message=random_affirmation)

@app.route('/', methods=['GET'])
def home():
    affirmations = load_affirmations()
    random_affirmation = random.choice(affirmations)
    return render_template('index.html', message=random_affirmation)

if __name__ == '__main__':
    # Use this for local development
    app.run(debug=True)
    
    # When deployed to production, Gunicorn will be used instead
    # so this code block won't run
