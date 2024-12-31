from flask import Flask, render_template, request, jsonify
import folium
from geopy.distance import geodesic

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (21.0285, 105.8542)  # Default to the center of India
    folium_map = folium.Map(location=start_coords, zoom_start=12)
    return render_template('index.html', map=folium_map._repr_html_())

@app.route('/calculate_center', methods=['POST'])
def calculate_center():
    locations = request.json['locations']
    latitudes = [loc['lat'] for loc in locations]
    longitudes = [loc['lng'] for loc in locations]
    avg_lat = sum(latitudes) / len(latitudes)
    avg_lng = sum(longitudes) / len(longitudes)
    return jsonify({'center': {'lat': avg_lat, 'lng': avg_lng}})

if __name__ == '__main__':
    app.run(debug=True)