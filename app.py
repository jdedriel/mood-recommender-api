from flask import Flask, request, jsonify
import difflib  # for closest mood matches

app = Flask(__name__)

mood_activities = {
    "happy": ["Dance", "Call a friend", "Go outside"],
    "sad": ["Watch a feel-good movie", "Journal", "Listen to music"],
    "bored": ["Try a new recipe", "Play a game", "Read a book"],
    "anxious": ["Meditate", "Take deep breaths", "Walk around"],
    "tired": ["Take a nap", "Drink water", "Stretch lightly"],
    "motivated": ["Start a new project", "Make a to-do list", "Exercise"],
    "angry": ["Go for a run", "Listen to calming music", "Write your thoughts"],
    "relaxed": ["Take a bath", "Read poetry", "Sip some tea"],
    "stressed": ["Do yoga", "Listen to nature sounds", "Write in a journal"],
    "lonely": ["Call family", "Chat online", "Join a local event"],
    "excited": ["Plan a trip", "Celebrate with friends", "Start a hobby"],
    "confused": ["Write pros/cons list", "Talk to a mentor", "Take a short walk"],
    "grateful": ["Write gratitude notes", "Help someone", "Spend time with loved ones"],
    "curious": ["Read an article", "Watch a documentary", "Experiment with coding"],
    "inspired": ["Draw or paint", "Write a poem", "Work on your passion project"]
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
            # Suggest closest matches
            close_matches = difflib.get_close_matches(mood, mood_activities.keys(), n=3, cutoff=0.6)
            return jsonify({
                "error": f"Mood '{mood}' not supported.",
                "did_you_mean": close_matches if close_matches else "No similar moods found."
            }), 400
    else:
        return jsonify({"error": "Mood query parameter is required."}), 400


if __name__ == "__main__":
    app.run(debug=True)
