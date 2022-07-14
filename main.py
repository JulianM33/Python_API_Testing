import requests
import json

url_top_movies = "https://developers.themoviedb.org/3/movies/get-top-rated-movies"
url_rate_movie = "https://developers.themoviedb.org/3/movies/rate-movie"
url_auth = "https://api.themoviedb.org/3/movie/550?api_key=54bb0787a703d69941a9db676179294f"

API_KEY = "54bb0787a703d69941a9db676179294f"


def test_basic():
    response = requests.get(url_top_movies)
    print(response)

    print("content = ", response.content)
    print("headers = ", response.headers)

    assert response.status_code == 200


def test_auth():
    response = requests.get(url_auth)
    # print("response = ", response)
    # # str = json.loads(response.json())
    response.json()

    assert response.status_code == 205320



