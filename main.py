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

url_403 = "https://www.themoviedb.org/random/page/error"
url_404 = "https://api.themoviedb.org/3/movie/2131513/images?api_key=54bb0787a703d69941a9db676179294f"



# Test basic GET API
def test_basic():
    response = requests.get(url_top_movies)
    assert response.status_code == 200


# Test simple usage of the given Auth_API key
def test_auth():
    response = requests.get(url_auth)
    assert response.status_code == 200


# Test bad request
def test_403():
    response = requests.get(url_403)
    assert response.status_code == 403


# Test not found request
def test_404():
    response = requests.get(url_404)
    assert response.status_code == 404


# Test API returning an image
def test_img():
    response = requests.get(url_img)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "image/png"


def test_get_token():
    # Begin by obtaining initial auth token
    url_get_token = "https://api.themoviedb.org/3/authentication/token/new?api_key={}".format(API_KEY)
    response = requests.get(url_get_token)

    assert response.status_code == 200

    # Store token obtained given in the JSON response
    NEW_TOKEN = response.json()["request_token"]

    # Approving token requires manual user approval, we print link so that we can authenticate
    # In order to prevent proceeding before the user approval, we can run in debug mode and put a
    #  breakpoint before the last  requests.post() call in line 89
    url_authenticate = "https://www.themoviedb.org/authenticate/{}".format(NEW_TOKEN)
    print(url_authenticate)

    # Make the request body needed for obtained the session_id
    request_body = "\"request_token\": \"{token}\"".format(token=NEW_TOKEN)
    request_body = "{" + request_body + "}"
    print(request_body)

    # This should be the URL at which we obtain the session_id, but link is not working
    # When trying the same POST request in Postman, the same result is still obtained
    url_session = "https://api.themoviedb.org/3/authentication/session/new?api_key={}".format(API_KEY)
    response = requests.post(url_session,
                             data=request_body
                             )
    print(url_authenticate)
    print(response)
    print(response.text)
