import requests
import json

API_KEY = "54bb0787a703d69941a9db676179294f"
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGJiMDc4N2E3MDNkNjk5NDFhOWRiNjc2MTc5Mjk0ZiIsInN1YiI6IjYyY2VmYmFlZDRjYzhlMDZjZGY3MGJlMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bxrxL9PtGZZWLaIDq8TaTCovLCbycDQuQ6trlt6CPvc"

url_top_movies = "https://developers.themoviedb.org/3/movies/get-top-rated-movies"
url_rate_movie = "https://developers.themoviedb.org/3/movies/rate-movie"
url_auth = "https://api.themoviedb.org/3/movie/550?api_key={}".format(API_KEY)
url_img = "https://image.tmdb.org/t/p/original/wwemzKWzjKYJFfCeiB57q3r4Bcm.png"

url_language = "https://api.themoviedb.org/3/movie/76341?api_key={}&language=".format(API_KEY)
url_post = "https://api.themoviedb.org/3/account/favorite?api_key={}&session_id=3".format(API_KEY)
url_review = "https://api.themoviedb.org/3/movie/278/reviews?api_key={}&language=en-US&page=1".format(API_KEY)



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
    # response.json()

    assert response.status_code == 200


def test_img():
    response = requests.get(url_img)
    print("headers ", response.headers)

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "image/png"


def test_review():
    response = requests.get(url_img)
    print("headers ", response.headers)

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "image/png"


def test_body_post_favorite():
    response = requests.post("https://api.themoviedb.org/3/movie/278/rating?api_key=54bb0787a703d69941a9db676179294f",
                             # data={"value": 8.5},
                             data="{\"value\": 8.5}",
                             headers={'Authorization': 'Bearer {}'.format(TOKEN)}
                             )
    print(response)
    print(response.text)


# c8315bec7e32adcfd35e0abb75f55f9362d761de
def test_get_token():
    url_get_token = "https://api.themoviedb.org/3/authentication/token/new?api_key={}".format(API_KEY)
    response = requests.get(url_get_token)
    print(response)
    # print(response.text)
    NEW_TOKEN = response.json()["request_token"]
    # NEW_TOKEN = "4e94d7348015b159140e9ca35556f9ed469a4656"
    print(NEW_TOKEN)
    print()

    url_authenticate = "https://www.themoviedb.org/authenticate/{}".format(NEW_TOKEN)
    print(url_authenticate)

    # response = requests.get(url_authenticate)
    # print(response)
    # print(response.headers)
    # print()

    request_body = "\"request_token\": \"{token}\"".format(token=NEW_TOKEN)
    request_body = "{" + request_body + "}"
    print(request_body)

    url_authenticate = "https://api.themoviedb.org/3/authentication/session/new?api_key={}".format(API_KEY)
    response = requests.post(url_authenticate,
                             data=request_body
                             )
    print(url_authenticate)
    print(response)
    print(response.text)


test_get_token()
# def test_language_codes():
#     for iso_code in iso_codes:
#         request = url_language + iso_code
#         response = requests.get(request)
#         assert response.status_code == 200
