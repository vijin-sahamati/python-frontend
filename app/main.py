from flask import Flask, render_template, jsonify
import math
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return {'status': 'running', 'app': 'Dynamic 3D Frontend'}

@app.route('/api/cube-data')
def cube_data():
    """Generate dynamic cube rotation data"""
    return {
        'title': 'Interactive Cube',
        'rotationSpeed': 0.01,
        'colors': ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
    }

@app.route('/api/particles-data')
def particles_data():
    """Generate particle system data"""
    particles = []
    for i in range(500):
        particles.append({
            'x': random.uniform(-100, 100),
            'y': random.uniform(-100, 100),
            'z': random.uniform(-100, 100),
            'vx': random.uniform(-0.5, 0.5),
            'vy': random.uniform(-0.5, 0.5),
            'vz': random.uniform(-0.5, 0.5),
            'size': random.uniform(0.5, 2),
            'color': random.choice(['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
        })
    return {'title': 'Particle Galaxy', 'particles': particles[:100]}  # Return subset for efficiency

@app.route('/api/wave-data')
def wave_data():
    """Generate wave/terrain data"""
    wave = []
    for x in range(-50, 51, 5):
        for z in range(-50, 51, 5):
            y = 10 * math.sin(x * 0.1) * math.cos(z * 0.1)
            wave.append({'x': x, 'y': y, 'z': z})
    return {'title': 'Wave Terrain', 'vertices': wave}

@app.route('/api/torus-data')
def torus_data():
    """Generate torus geometry data"""
    return {
        'title': 'Interactive Torus',
        'majorRadius': 20,
        'minorRadius': 8,
        'tubeSegments': 100,
        'radialSegments': 100,
        'rotationSpeed': 0.005,
        'color': '#00FF88'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
