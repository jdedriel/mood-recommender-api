# Mood Recommender API
Flask Python License

A simple Mood Recommender API built with Flask, allowing users to get activity suggestions based on their current mood. Supports multiple moods and provides JSON responses for easy integration with frontend apps or other services.

---

## Features
📝 **Get Recommendations** – Users provide a mood query parameter and receive a list of suggested activities.  
📄 **Multiple Moods** – Supports 15 moods including happy, sad, bored, anxious, tired, motivated, angry, relaxed, stressed, lonely, excited, confused, grateful, curious, and inspired.  
⚡ **Error Handling** – Returns proper JSON errors for missing or unsupported moods.  
📂 **moods.json** – Mood data stored in a separate JSON file for easy updates.

---

## Installation / Setup
Clone the repository:
```bash
git clone <your-repo-url>
cd mood-recommender-api

# Mood Recommender API
Flask Python License

A simple Mood Recommender API built with Flask, allowing users to get activity suggestions based on their current mood. Supports multiple moods and provides JSON responses for easy integration with frontend apps or other services.

---

## Features
📝 **Get Recommendations** – Users provide a mood query parameter and receive a list of suggested activities.  
📄 **Multiple Moods** – Supports 15 moods including happy, sad, bored, anxious, tired, motivated, angry, relaxed, stressed, lonely, excited, confused, grateful, curious, and inspired.  
⚡ **Error Handling** – Returns proper JSON errors for missing or unsupported moods.  
📂 **moods.json** – Mood data stored in a separate JSON file for easy updates.

---

## Installation / Setup
Clone the repository:
```bash
git clone <your-repo-url>
cd mood-recommender-api


Run the API

Start the Flask server:

flask run


The API will be accessible at:

http://127.0.0.1:5000


API Endpoints
1. Home

Request:

GET /


Response (200 OK):

"Welcome to the Mood Recommender API! Try /recommendations?mood=happy"

2. Get Recommendations

Request:

GET /recommendations?mood=<mood>


Response (200 OK, valid mood):

{
  "mood": "happy",
  "recommendations": ["Dance", "Call a friend", "Go outside"]
}


Error (missing mood):

{
  "error": "Mood query parameter is required."
}


Error (unsupported mood):

{
  "error": "Mood 'unknown' not supported."
}

Testing

Run unit tests with pytest:

pytest test_app.py

Example Usage

Request in browser or curl:

http://127.0.0.1:5000/recommendations?mood=happy


Response:

{
  "mood": "happy",
  "recommendations": ["Dance", "Call a friend", "Go outside"]
}