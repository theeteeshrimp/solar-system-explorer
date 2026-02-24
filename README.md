# 🚀 Solar System Explorer

> *A beautiful Flask demo website exploring our solar system*

![Flask](https://img.shields.io/badge/Flask-3.0-black)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)

## ✨ Features

- 🪐 **All 8 Planets** - Detailed information about each planet
- ☀️ **The Sun** - Learn about our star
- 📊 **Compare Page** - Side-by-side planet comparisons
- 🎨 **Beautiful Design** - Space-themed with animated stars
- 📱 **Responsive** - Works on all devices
- 🐳 **Docker Ready** - Easy deployment

## 🚀 Quick Start

### Option 1: Docker (Easiest)

```bash
# Clone the repo
git clone https://github.com/theeteeshrimp/solar-system-explorer.git
cd solar-system-explorer

# Run with Docker Compose
docker-compose up -d

# Open http://localhost:5000
```

### Option 2: Local Python

```bash
# Clone the repo
git clone https://github.com/theeteeshrimp/solar-system-explorer.git
cd solar-system-explorer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Open http://localhost:5000
```

## 🌍 What's Included

### Pages

| Page | Description |
|------|-------------|
| `/` | Homepage with Sun info and planet grid |
| `/planet/<name>` | Detailed planet page |
| `/compare` | Compare all planets side-by-side |

### Planet Data

Each planet includes:
- 📏 Diameter
- ☀️ Distance from Sun
- 🌅 Day length
- 📅 Year length
- 🌙 Number of moons
- 🌡️ Temperature
- 🎯 Fun facts

## 🎨 Screenshots

*Homepage - Explore all planets at a glance*

*Planet Detail - Deep dive into each world*

*Compare - See how planets stack up*

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, Vanilla JS
- **Styling:** Custom CSS with CSS variables
- **Animations:** CSS keyframes + Intersection Observer
- **Deployment:** Docker + Gunicorn

## 📝 Project Structure

```
solar-system-explorer/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container config
├── docker-compose.yml    # Docker orchestration
├── README.md             # This file
├── static/
│   ├── css/
│   │   ├── style.css     # Main styles
│   │   ├── planet.css    # Planet detail page
│   │   └── compare.css   # Compare page
│   └── js/
│       ├── main.js       # Homepage animations
│       └── compare.js    # Compare page animations
└── templates/
    ├── index.html        # Homepage
    ├── planet.html       # Planet detail
    ├── compare.html      # Compare page
    └── 404.html          # Error page
```

## 🌟 Features Detail

### Interactive Elements
- ✅ Hover effects on planet cards
- ✅ Scroll animations
- ✅ Animated starfield background
- ✅ Responsive grid layouts

### Design Highlights
- 🌌 Animated twinkling stars
- 🎨 Gradient backgrounds
- 🌈 Each planet has its own color theme
- 📱 Mobile-friendly navigation

## 🔧 Customization

### Add a New Planet
Edit `app.py` and add to the `PLANETS` dictionary:

```python
"newplanet": {
    "name": "New Planet",
    "emoji": "🪐",
    "order": 9,
    "distance_from_sun": "X billion km",
    "diameter": "X km",
    ...
}
```

### Change Colors
Edit `static/css/style.css` and modify CSS variables:

```css
:root {
    --bg-primary: #0a0a1a;
    --accent-gold: #ffd700;
    ...
}
```

## 🛑 Stopping

```bash
# If using Docker
docker-compose down

# If running locally
# Press Ctrl+C
```

## 📚 Learning Resources

This project demonstrates:
- Flask routing and templates
- Jinja2 templating
- CSS Grid and Flexbox
- CSS animations
- Responsive design
- Docker containerization

## 🦐 Credits

Made with 🚀 by **Kimi-Claw** ([@theeteeshrimp](https://github.com/theeteeshrimp))

For **T** - because space is cool! 🌌

---

*"The cosmos is within us. We are made of star-stuff."* - Carl Sagan
