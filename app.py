from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

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

@app.route('/api/animals', methods=['GET'])
def get_animals():
    animals_with_descriptions = {}
    for animal, data in animals.items():
        animal_data = data.copy()
        animal_data['description'] = get_description(animal_data.pop('description_file'))
        animals_with_descriptions[animal] = animal_data
    return jsonify(animals_with_descriptions)

@app.route('/api/animals/<string:name>', methods=['GET'])
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
