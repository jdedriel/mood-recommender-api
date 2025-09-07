from flask import Flask, request, jsonify

app = Flask(__name__)

mood_activities = {
    "happy": ["Dance", "Call a friend", "Go outside"],
    "sad": ["Watch a feel-good movie", "Journal", "Listen to music"],
    "bored": ["Try a new recipe", "Play a game", "Read a book"],
    "anxious": ["Meditate", "Take deep breaths", "Walk around"]
}

@app.route('/')
def home():
    return "Welcome to the Mood Recommender API! Try /recommendations?mood=happy"


@app.route('/recommendations')
def get_recommendations():
    mood = request.args.get('mood')
    if mood:
        mood = mood.lower()
        if mood in mood_activities:
            return jsonify({"mood": mood, "recommendations": mood_activities[mood]})
        else:
            return jsonify({"error": f"Mood '{mood}' not supported."}), 400
    else:
        return jsonify({"error": "Mood query parameter is required."}), 400

if __name__ == "__main__":
    app.run(debug=True)
