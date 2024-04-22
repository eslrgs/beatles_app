import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import pandas as pd
import random
import string

load_dotenv()

api_key = os.environ.get("api_key")
port = os.environ.get("PORT", 8080)

app = Flask(__name__, template_folder="templates", static_folder="static")

# Load the data
df = pd.read_csv("app/static/data/beatles_lyrics_cleaned.csv")
songs_list = df.to_dict("records")

def get_random_song():
    return random.choice(songs_list)

current_song = get_random_song()

@app.route("/", methods=["GET", "POST"])
def index():
    score = request.form.get("score", default=0, type=int)
    question_count = request.form.get("question_count", default=0, type=int)
    current_song = request.form.get("current_song_title", None)
    message = ""
    status = ""

    if request.method == "POST":
        user_guess = request.form.get("song_guess")
        if "skip" in request.form or user_guess:
            message = f"Try again! The answer was {current_song}"
            status = "skipped"
            question_count += 1

        if user_guess:
            if user_guess.lower().strip().translate(str.maketrans('', '', string.punctuation)) == current_song.lower().strip().translate(str.maketrans('', '', string.punctuation)):
                message = f"Correct! The answer was {current_song}"
                status = "correct"
                score += 1
            else:
                message = f"Try again! The answer was {current_song}"
                status = "incorrect"

        if question_count >= 10:
            message += f" Game over! Your score: {score}/10"
            score = 0
            question_count = 0

    next_song = get_random_song()
    current_song_title = next_song["title"]

    return render_template(
        "index.html",
        lyric=next_song["lyrics"][:100],
        current_song_title=current_song_title,
        message=message,
        status=status,
        score=score,
        question_count=question_count,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
