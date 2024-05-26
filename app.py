from flask import Flask, jsonify, request, send_from_directory
import os
import functools
app = Flask(__name__)
# Your generated API key 
API_KEY = 'your_api_key'

# Sample data
animals = {
    "cow": {
        "image": "/static/images/cow.jpeg",
        "sound": "/static/sounds/cow.wav",
        "description_file": "/static/descriptions/cow.txt"
    },
    "horse": {
        "image": "/static/images/horse.jpeg",
        "sound": "/static/sounds/horse.wav",
        "description_file": "/static/descriptions/horse.txt"
    }
}

def get_description(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Description not available."

def require_api_key(view_function):
    @functools.wraps(view_function)
    def decorated_function(*args, **kwargs):
        key = request.args.get('api_key')
        if key and key == API_KEY:
            return view_function(*args, **kwargs)
        else:
            return jsonify({"error": "Unauthorized"}), 401
    return decorated_function

@app.route('/api/animals', methods=['GET'])
@require_api_key
def get_animals():
    animals_with_descriptions = {}
    for animal, data in animals.items():
        animal_data = data.copy()
        animal_data['description'] = get_description(animal_data.pop('description_file'))
        animals_with_descriptions[animal] = animal_data
    return jsonify(animals_with_descriptions)

@app.route('/api/animals/<string:name>', methods=['GET'])
@require_api_key
def get_animal(name):
    animal = animals.get(name)
    if animal:
        animal_data = animal.copy()
        animal_data['description'] = get_description(animal_data.pop('description_file'))
        return jsonify(animal_data)
    else:
        return jsonify({"error": "Animal not found"}), 404

# Serve static files from the 'static' directory
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
