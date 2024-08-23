from flask import Flask, render_template
from apis.api import Api
from dotenv import load_dotenv
import os

load_dotenv(".env")

API_KEY = os.environ["API_KEY"]
API_URL = "https://api.themoviedb.org"
IMAGE_PATH = "https://image.tmdb.org/t/p/w500/"
api_obj = Api(api_url=API_URL, api_key=API_KEY)

app = Flask(__name__)


@app.route("/")
def home():
    trending_movies_response = api_obj.call_api(
        endpoint="/3/trending/movie/day?language=en-US\"&",
        payload={},
        headers={"api_key": API_KEY},
    )
    trending_movies_response = trending_movies_response.json()["results"]


    now_playing_movies_response = api_obj.call_api(
        endpoint="/3/movie/now_playing?language=en-US&page=1&",
        payload={},
        headers={"api_key": API_KEY},
    )
    now_playing_movies_response = now_playing_movies_response.json()["results"]

    trending_shows_response = api_obj.call_api(
        endpoint="/3/trending/tv/day?language=en-US&",
        payload={},
        headers={"api_key": API_KEY},
    )
    trending_shows_response = trending_shows_response.json()["results"]

    trending_people_response = api_obj.call_api(
        endpoint="/3/trending/person/day?language=en-US&",
        payload={},
        headers={"api_key": API_KEY},
    )
    trending_people_response = trending_people_response.json()["results"]

    return render_template("index.html", 
                           trending_movies="trending_movies_response", 
                           now_playing_movies = now_playing_movies_response, 
                           trending_shows = trending_shows_response,
                           trending_people = trending_people_response,
                           )


if __name__ == "__main__":
    app.run(debug=True)
