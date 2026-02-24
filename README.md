# Solar System Explorer

🚀 A beautiful Flask demo website exploring our solar system!

![Flask](https://img.shields.io/badge/Flask-3.0-black)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)

## 🌟 Features

- 🪐 **All 8 Planets** - Detailed information about each planet
- ☀️ **The Sun** - Learn about our star
- 📊 **Comparisons** - See how planets stack up against each other
- 🎨 **Space Theme** - Beautiful dark UI with animated stars
- 📱 **Responsive** - Works on desktop and mobile
- 🐳 **Docker Ready** - Easy deployment

## 🚀 Quick Start

### Option 1: Local Python

```bash
# Clone the repo
git clone https://github.com/theeteeshrimp/solar-system-explorer.git
cd solar-system-explorer

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Open http://localhost:5000
```

### Option 2: Docker

```bash
# Build and run
docker build -t solar-system .
docker run -p 5000:5000 solar-system

# Or use docker-compose
docker-compose up -d
```

## 🗺️ Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with all planets |
| `/planet/<name>` | Detailed planet page |
| `/compare` | Compare planets side-by-side |
| `/api/planets` | JSON API - all planets |
| `/api/planet/<name>` | JSON API - specific planet |

## 📊 Data Includes

- ☀️ Distance from Sun
- 📏 Diameter
- 🕐 Day length
- 📅 Year length
- 🌙 Number of moons
- 🌡️ Temperature
- 🌟 Fun facts

## 🎨 Customization

### Add a new planet (hypothetical!)

Edit `app.py` and add to the `PLANETS` dictionary:

```python
"planet9": {
    "name": "Planet 9",
    "emoji": "🪐",
    "order": 9,
    "distance_from_sun": "X billion km",
    "diameter": "X km",
    # ... etc
}
```

### Change styling

- `static/css/style.css` - Main styles
- `static/css/planet.css` - Planet detail styles
- `static/js/main.js` - Animations and interactions

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Templates:** Jinja2
- **Styling:** Pure CSS (no frameworks)
- **Animations:** CSS + Vanilla JS
- **Icons:** Unicode emoji

## 📸 Screenshots

*Home page showing all planets in a grid*

*Planet detail page with stats and facts*

*Comparison page with charts*

## 🌐 API Usage

```bash
# Get all planets
curl http://localhost:5000/api/planets

# Get specific planet
curl http://localhost:5000/api/planet/mars
```

## 🐳 Docker Details

```yaml
# docker-compose.yml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
```

## 📝 TODO Ideas

- [ ] Add more dwarf planets (Pluto, Ceres, etc.)
- [ ] Interactive orbital simulation
- [ ] Planet size comparison visualization
- [ ] Day/night mode toggle
- [ ] Search functionality
- [ ] Quiz game about planets

## 🦐 Credits

Made by **Kimi-Claw** ([@theeteeshrimp](https://github.com/theeteeshrimp))

For **T** - exploring the cosmos one Flask app at a time! 🚀

Data based on NASA information.

---

*"We are all in the gutter, but some of us are looking at the stars."* - Oscar Wilde
