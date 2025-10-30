from flask import Flask, jsonify, request

app = Flask(__name__)
favorites = []

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    # fake response for demo purposes
    return jsonify({"city": city, "temperature": "20°C"})

@app.route('/favorites', methods=['GET', 'POST'])
def manage_favorites():
    if request.method == 'POST':
        city = request.json.get('city')
        favorites.append(city)
        return jsonify({"status": "added", "city": city})
    return jsonify(favorites)

if __name__ == "__main__":
    app.run(port=5000)

