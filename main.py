import requests

url_top_movies = "https://developers.themoviedb.org/3/movies/get-top-rated-movies"
url_rate_movie = "https://developers.themoviedb.org/3/movies/rate-movie"


def test_answer():
    response = requests.get(url_top_movies)
    print(response)

    print("content = ", response.content)
    print("headers = ", response.headers)

    assert(response.status_code == 200)
