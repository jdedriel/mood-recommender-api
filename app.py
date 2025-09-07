from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load moods from moods.json
moods_file_path = os.path.join(os.path.dirname(__file__), "moods.json")
with open(moods_file_path, "r") as f:
    mood_activities = json.load(f)

@app.route('/')
def home():
    return "Welcome to the Mood Recommender API! Try /recommendations?mood=happy"

@app.route('/recommendations')
def get_recommendations():
    mood = request.args.get('mood')
    if not mood:
        return jsonify({"error": "Mood query parameter is required."}), 400

    mood = mood.lower()
    if mood not in mood_activities:
        return jsonify({"error": f"Mood '{mood}' not supported."}), 400

    return jsonify({"mood": mood, "recommendations": mood_activities[mood]})

if __name__ == "__main__":
    app.run(debug=True)
