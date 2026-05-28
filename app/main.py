from flask import Flask, render_template, jsonify
from flask_cors import CORS
import math
import random
import json

app = Flask(__name__)
CORS(app)

# Store game state
game_state = {
    'user_score': 0,
    'achievements': [],
    'collected_items': []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pages/dinosaurs')
def dinosaurs():
    return render_template('dinosaurs.html')

@app.route('/pages/planets')
def planets():
    return render_template('planets.html')

@app.route('/pages/ocean')
def ocean():
    return render_template('ocean.html')

@app.route('/pages/space')
def space():
    return render_template('space.html')

@app.route('/api/status')
def status():
    return {'status': 'running', 'app': 'Kids 3D Interactive World', 'version': '2.0'}

@app.route('/api/game-state')
def get_game_state():
    return game_state

@app.route('/api/add-score', methods=['POST'])
def add_score():
    import request
    data = request.get_json()
    points = data.get('points', 0)
    game_state['user_score'] += points
    return {'score': game_state['user_score']}

@app.route('/api/dinosaurs-data')
def dinosaurs_data():
    """Generate dinosaur data"""
    return {
        'title': 'Dinosaur World',
        'dinosaurs': [
            {'name': 'T-Rex', 'color': 0xFF6B6B, 'size': 2, 'y': 0},
            {'name': 'Triceratops', 'color': 0x45B7D1, 'size': 1.8, 'y': 0},
            {'name': 'Stegosaurus', 'color': 0xF7DC6F, 'size': 1.6, 'y': 0},
            {'name': 'Brachiosaurus', 'color': 0x4ECDC4, 'size': 2.5, 'y': 1}
        ]
    }

@app.route('/api/planets-data')
def planets_data():
    """Generate planet data"""
    planets = [
        {'name': 'Mercury', 'radius': 3.8, 'color': 0x8C7853, 'distance': 40, 'speed': 0.4},
        {'name': 'Venus', 'radius': 9.5, 'color': 0xFFC649, 'distance': 70, 'speed': 0.15},
        {'name': 'Earth', 'radius': 10, 'color': 0x4A90E2, 'distance': 100, 'speed': 0.1},
        {'name': 'Mars', 'radius': 5.3, 'color': 0xE27B58, 'distance': 130, 'speed': 0.08},
        {'name': 'Jupiter', 'radius': 11, 'color': 0xC88B3A, 'distance': 170, 'speed': 0.05}
    ]
    return {'title': 'Solar System', 'planets': planets}

@app.route('/api/ocean-data')
def ocean_data():
    """Generate ocean creatures data"""
    creatures = [
        {'name': 'Dolphin', 'color': 0x4ECDC4, 'size': 2},
        {'name': 'Shark', 'color': 0x556270, 'size': 2.5},
        {'name': 'Turtle', 'color': 0x6ABB86, 'size': 1.5},
        {'name': 'Jellyfish', 'color': 0xFF69B4, 'size': 1}
    ]
    return {'title': 'Ocean World', 'creatures': creatures}

@app.route('/api/space-data')
def space_data():
    """Generate space data"""
    return {
        'title': 'Galaxy Explorer',
        'stars': 1000,
        'asteroids': 50
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
