from flask import Flask, jsonify, request, send_from_directory
import os
import functools
app = Flask(__name__)
# Your generated API key 
API_KEY = 'your_api_key'

# Sample data
animals = {
    "bat": {
        "image": "/static/images/bat.jpeg",
        "sound": "/static/sounds/bat.wav",
        "description_file": "/static/descriptions/bat.txt"
    },
    "bear": {
        "image": "/static/images/bear.jpeg",
        "sound": "/static/sounds/bear.wav",
        "description_file": "/static/descriptions/bear.txt"
    },
    "buffalo" : {
        "image": "/static/images/buffalo.jpeg",
        "sound": "/static/sounds/buffalo.wav",
        "description_file": "/static/descriptions/buffalo.txt"
    },
    "cat": {
        "image": "/static/images/cat.jpeg",
        "sound": "/static/sounds/cat.wav",
        "description_file": "/static/descriptions/cat.txt"
    },
    "chimpanzee": {
        "image": "/static/images/chimpanzee.jpeg",
        "sound": "/static/sounds/chimpanzee.wav",
        "description_file": "/static/descriptions/chimpanzee.txt"
    },
    "cock": {
        "image": "/static/images/cock.jpeg",
        "sound": "/static/sounds/cock.wav",
        "description_file": "/static/descriptions/cock.txt"
    },
    "cow": {
        "image": "/static/images/cow.jpeg",
        "sound": "/static/sounds/cow.wav",
        "description_file": "/static/descriptions/cow.txt"
    },
    "cricket": {
        "image": "/static/images/cricket.jpeg",
        "sound": "/static/sounds/cricket.wav",
        "description_file": "/static/descriptions/cricket.txt"
    },
    "crow": {
        "image": "/static/images/crow.jpeg",
        "sound": "/static/sounds/crow.wav",
        "description_file": "/static/descriptions/crow.txt"
    },
    "cuckoo": {
        "image": "/static/images/cuckoo.jpeg",
        "sound": "/static/sounds/cuckoo.wav",
        "description_file": "/static/descriptions/cuckoo.txt"
    },
    "deer": {
        "image": "/static/images/deer.jpeg",
        "sound": "/static/sounds/deer.wav",
        "description_file": "/static/descriptions/deer.txt"
    },
    "dog": {
        "image": "/static/images/dog.jpeg",
        "sound": "/static/sounds/dog.wav",
        "description_file": "/static/descriptions/dog.txt"
    },
    "dolphin": {
        "image": "/static/images/dolphin.jpeg",
        "sound": "/static/sounds/dolphin.wav",
        "description_file": "/static/descriptions/dolphin.txt"
    },
    "duck": {
        "image": "/static/images/duck.jpeg",
        "sound": "/static/sounds/duck.wav",
        "description_file": "/static/descriptions/duck.txt"
    },
    "eagle": {
        "image": "/static/images/eagle.jpeg",
        "sound": "/static/sounds/eagle.wav",
        "description_file": "/static/descriptions/eagle.txt"
    },
    "elephant": {
        "image": "/static/images/elephant.jpeg",
        "sound": "/static/sounds/elephant.wav",
        "description_file": "/static/descriptions/elephant.txt"
    },
    "flamingo": {
        "image": "/static/images/flamingo.jpeg",
        "sound": "/static/sounds/flamingo.wav",
        "description_file": "/static/descriptions/flamingo.txt"
    },
    "fox": {
        "image": "/static/images/fox.jpeg",
        "sound": "/static/sounds/fox.wav",
        "description_file": "/static/descriptions/fox.txt"
    },
    "frog": {
        "image": "/static/images/frog.jpeg",
        "sound": "/static/sounds/frog.wav",
        "description_file": "/static/descriptions/frog.txt"
    },
    "giraffe": {
        "image": "/static/images/giraffe.jpeg",
        "sound": "/static/sounds/giraffe.wav",
        "description_file": "/static/descriptions/giraffe.txt"
    },
    "goat": {
        "image": "/static/images/goat.jpeg",
        "sound": "/static/sounds/goat.wav",
        "description_file": "/static/descriptions/goat.txt"
    },
    "gorilla": {
        "image": "/static/images/gorilla.jpeg",
        "sound": "/static/sounds/gorilla.wav",
        "description_file": "/static/descriptions/gorilla.txt"
    },
    "hippo": {
        "image": "/static/images/hippo.jpeg",
        "sound": "/static/sounds/hippo.wav",
        "description_file": "/static/descriptions/hippo.txt"
    },
    "horse": {
        "image": "/static/images/horse.jpeg",
        "sound": "/static/sounds/horse.wav",
        "description_file": "/static/descriptions/horse.txt"
    },
    "hyenas": {
        "image": "/static/images/hyenas.jpeg",
        "sound": "/static/sounds/hyenas.wav",
        "description_file": "/static/descriptions/hyenas.txt"
    },
    "kangaroo": {
        "image": "/static/images/kangaroo.jpeg",
        "sound": "/static/sounds/kangaroo.wav",
        "description_file": "/static/descriptions/kangaroo.txt"
    },
    "koala": {
        "image": "/static/images/koala.jpeg",
        "sound": "/static/sounds/koala.wav",
        "description_file": "/static/descriptions/koala.txt"
    },
    "leopard": {
        "image": "/static/images/leopard.jpeg",
        "sound": "/static/sounds/leopard.wav",
        "description_file": "/static/descriptions/leopard.txt"
    },
    "lion": {
        "image": "/static/images/lion.jpeg",
        "sound": "/static/sounds/lion.wav",
        "description_file": "/static/descriptions/lion.txt"
    },
    "llama": {
        "image": "/static/images/llama.jpeg",
        "sound": "/static/sounds/llama.wav",
        "description_file": "/static/descriptions/llama.txt"
    },
    "orca": {
        "image": "/static/images/orca.jpeg",
        "sound": "/static/sounds/orca.wav",
        "description_file": "/static/descriptions/orca.txt"
    },
    "owl": {
        "image": "/static/images/owl.jpeg",
        "sound": "/static/sounds/owl.wav",
        "description_file": "/static/descriptions/owl.txt"
    },
    "parrot": {
        "image": "/static/images/parrot.jpeg",
        "sound": "/static/sounds/parrot.wav",
        "description_file": "/static/descriptions/parrot.txt"
    },
    "peacock": {
        "image": "/static/images/peacock.jpeg",
        "sound": "/static/sounds/peacock.wav",
        "description_file": "/static/descriptions/peacock.txt"
    },
    "penguin": {
        "image": "/static/images/penguin.jpeg",
        "sound": "/static/sounds/penguin.wav",
        "description_file": "/static/descriptions/penguin.txt"
    },
    "pigeon": {
        "image": "/static/images/pigeon.jpeg",
        "sound": "/static/sounds/pigeon.wav",
        "description_file": "/static/descriptions/pigeon.txt"
    },
    "sea lion": {
        "image": "/static/images/sea_lion.jpeg",
        "sound": "/static/sounds/sea_lion.wav",
        "description_file": "/static/descriptions/sea_lion.txt"
    },
    "seal": {
        "image": "/static/images/seal.jpeg",
        "sound": "/static/sounds/seal.wav",
        "description_file": "/static/descriptions/seal.txt"
    },
    "sheep": {
        "image": "/static/images/sheep.jpeg",
        "sound": "/static/sounds/sheep.wav",
        "description_file": "/static/descriptions/sheep.txt"
    },
    "sparrow": {
        "image": "/static/images/sparrow.jpeg",
        "sound": "/static/sounds/sparrow.wav",
        "description_file": "/static/descriptions/sparrow.txt"
    },
    "tiger": {
        "image": "/static/images/tiger.jpeg",
        "sound": "/static/sounds/tiger.wav",
        "description_file": "/static/descriptions/tiger.txt"
    },
    "vulture": {
        "image": "/static/images/vulture.jpeg",
        "sound": "/static/sounds/vulture.wav",
        "description_file": "/static/descriptions/vulture.txt"
    },
    "wolf": {
        "image": "/static/images/wolf.jpeg",
        "sound": "/static/sounds/wolf.wav",
        "description_file": "/static/descriptions/wolf.txt"
    },
    "zebra": {
        "image": "/static/images/zebra.jpeg",
        "sound": "/static/sounds/zebra.wav",
        "description_file": "/static/descriptions/zebra.txt"
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
