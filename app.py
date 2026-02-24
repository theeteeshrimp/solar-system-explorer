from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Solar system data
PLANETS = {
    "mercury": {
        "name": "Mercury",
        "emoji": "🌑",
        "order": 1,
        "distance_from_sun": "57.9 million km",
        "diameter": "4,879 km",
        "day_length": "59 Earth days",
        "year_length": "88 Earth days",
        "moons": 0,
        "temperature": "-180°C to 430°C",
        "description": "The smallest planet in our solar system and closest to the Sun.",
        "facts": [
            "Mercury has no atmosphere to retain heat",
            "It has a solid, cratered surface like the Moon",
            "A day on Mercury is longer than its year!",
            "It has the most extreme temperature variations"
        ],
        "color": "#8C8C8C"
    },
    "venus": {
        "name": "Venus",
        "emoji": "🌕",
        "order": 2,
        "distance_from_sun": "108.2 million km",
        "diameter": "12,104 km",
        "day_length": "243 Earth days",
        "year_length": "225 Earth days",
        "moons": 0,
        "temperature": "462°C (average)",
        "description": "The hottest planet with a thick, toxic atmosphere.",
        "facts": [
            "Venus spins backwards compared to other planets",
            "Its day is longer than its year",
            "Surface pressure is 92 times Earth's",
            "Visible as the brightest planet in the sky"
        ],
        "color": "#E6E600"
    },
    "earth": {
        "name": "Earth",
        "emoji": "🌍",
        "order": 3,
        "distance_from_sun": "149.6 million km",
        "diameter": "12,742 km",
        "day_length": "24 hours",
        "year_length": "365.25 days",
        "moons": 1,
        "temperature": "-88°C to 58°C",
        "description": "Our home! The only known planet to support life.",
        "facts": [
            "71% of Earth's surface is covered by water",
            "Earth has a powerful magnetic field",
            "It's the only planet not named after a god",
            "Earth has one natural satellite: the Moon"
        ],
        "color": "#4169E1"
    },
    "mars": {
        "name": "Mars",
        "emoji": "🌑",
        "order": 4,
        "distance_from_sun": "227.9 million km",
        "diameter": "6,779 km",
        "day_length": "24.6 hours",
        "year_length": "687 Earth days",
        "moons": 2,
        "temperature": "-125°C to 20°C",
        "description": "The Red Planet, target for future human exploration.",
        "facts": [
            "Mars has the largest volcano in the solar system: Olympus Mons",
            "It has two small moons: Phobos and Deimos",
            "Dust storms can cover the entire planet",
            "Evidence of ancient rivers and lakes found"
        ],
        "color": "#CD5C5C"
    },
    "jupiter": {
        "name": "Jupiter",
        "emoji": "🪐",
        "order": 5,
        "distance_from_sun": "778.5 million km",
        "diameter": "139,820 km",
        "day_length": "9.9 hours",
        "year_length": "11.9 Earth years",
        "moons": 95,
        "temperature": "-110°C (cloud tops)",
        "description": "The largest planet, a gas giant with a Great Red Spot.",
        "facts": [
            "Jupiter is 2.5 times more massive than all other planets combined",
            "The Great Red Spot is a storm larger than Earth",
            "It has a faint ring system",
            "Jupiter acts as a 'cosmic vacuum cleaner' protecting inner planets"
        ],
        "color": "#D2691E"
    },
    "saturn": {
        "name": "Saturn",
        "emoji": "🪐",
        "order": 6,
        "distance_from_sun": "1.4 billion km",
        "diameter": "116,460 km",
        "day_length": "10.7 hours",
        "year_length": "29.5 Earth years",
        "moons": 146,
        "temperature": "-140°C (cloud tops)",
        "description": "Famous for its beautiful, prominent ring system.",
        "facts": [
            "Saturn is less dense than water - it would float!",
            "Its rings are made of ice and rock particles",
            "Winds can reach 1,800 km/h",
            "Saturn's moon Titan has a thick atmosphere"
        ],
        "color": "#F4A460"
    },
    "uranus": {
        "name": "Uranus",
        "emoji": "🪐",
        "order": 7,
        "distance_from_sun": "2.9 billion km",
        "diameter": "50,724 km",
        "day_length": "17.2 hours",
        "year_length": "84 Earth years",
        "moons": 27,
        "temperature": "-195°C",
        "description": "An ice giant that rotates on its side.",
        "facts": [
            "Uranus rotates on its side (98° tilt)",
            "It has faint rings discovered in 1977",
            "Methane in its atmosphere gives it a blue-green color",
            "A season on Uranus lasts 21 Earth years"
        ],
        "color": "#4FD0E7"
    },
    "neptune": {
        "name": "Neptune",
        "emoji": "🪐",
        "order": 8,
        "distance_from_sun": "4.5 billion km",
        "diameter": "49,244 km",
        "day_length": "16.1 hours",
        "year_length": "165 Earth years",
        "moons": 14,
        "temperature": "-200°C",
        "description": "The windiest planet, a deep blue ice giant.",
        "facts": [
            "Neptune has the strongest winds in the solar system (2,100 km/h)",
            "It was the first planet predicted by math before being seen",
            "Its blue color comes from methane absorption",
            "Neptune has only completed one orbit since discovery in 1846"
        ],
        "color": "#4169E1"
    }
}

SUN = {
    "name": "The Sun",
    "emoji": "☀️",
    "type": "Yellow Dwarf Star",
    "diameter": "1.39 million km",
    "mass": "99.86% of solar system",
    "surface_temperature": "5,500°C",
    "core_temperature": "15 million°C",
    "age": "4.6 billion years",
    "description": "The heart of our solar system, providing light and heat to all planets.",
    "facts": [
        "The Sun accounts for 99.86% of the mass in our solar system",
        "Light takes 8 minutes to travel from Sun to Earth",
        "The Sun is actually white, but appears yellow through Earth's atmosphere",
        "Every second, the Sun converts 4 million tons of mass into energy"
    ]
}

@app.route('/')
def index():
    return render_template('index.html', planets=PLANETS, sun=SUN)

@app.route('/planet/<name>')
def planet_detail(name):
    planet = PLANETS.get(name.lower())
    if planet:
        return render_template('planet.html', planet=planet, all_planets=PLANETS)
    return render_template('404.html'), 404

@app.route('/api/planets')
def api_planets():
    return jsonify(PLANETS)

@app.route('/api/planet/<name>')
def api_planet(name):
    planet = PLANETS.get(name.lower())
    if planet:
        return jsonify(planet)
    return jsonify({"error": "Planet not found"}), 404

@app.route('/compare')
def compare():
    return render_template('compare.html', planets=PLANETS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
