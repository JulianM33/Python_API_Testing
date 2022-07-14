import requests
import json

API_KEY = "54bb0787a703d69941a9db676179294f"

url_top_movies = "https://developers.themoviedb.org/3/movies/get-top-rated-movies"
url_rate_movie = "https://developers.themoviedb.org/3/movies/rate-movie"
url_auth = "https://api.themoviedb.org/3/movie/550?api_key={}".format(API_KEY)

url_language = "https://api.themoviedb.org/3/movie/76341?api_key={}&language=".format(API_KEY)

iso_codes = ["ab", "aa", "af", "ak", "sq", "am", "ar", "an", "hy", "as", "av", "ae", "ay", "az", "bm", "ba", "eu",
             "be", "bn", "bi", "bs", "br", "bg", "my", "ca", "ch", "ce", "ny", "zh", "cu", "cv", "kw", "co", "cr",
             "hr", "cs", "da", "dv", "nl", "dz", "en", "eo", "et", "ee", "fo", "fj", "fi", "fr", "fy", "ff", "gd",
             "gl", "lg", "ka", "de", "el", "kl", "gn", "gu", "ht", "ha", "he", "hz", "hi", "ho", "hu", "is", "io",
             "ig", "id", "ia", "ie", "iu", "ik", "ga", "it", "ja", "jv", "kn", "kr", "ks", "kk", "km", "ki", "rw",
             "ky", "kv", "kg", "ko", "kj", "ku", "lo", "la", "lv", "li", "ln", "lt", "lu", "lb", "mk", "mg", "ms",
             "ml", "mt", "gv", "mi", "mr", "mh", "mn", "na", "nv", "nd", "nr", "ng", "ne", "no", "nb", "nn", "ii",
             "oc", "oj", "or", "om", "os", "pi", "ps", "fa", "pl", "pt", "pa", "qu", "ro", "rm", "rn", "ru", "se",
             "sm", "sg", "sa", "sc", "sr", "sn", "sd", "si", "sk", "sl", "so", "st", "es", "su", "sw", "ss", "sv",
             "tl", "ty", "tg", "ta", "tt", "te", "th", "bo", "ti", "to", "ts", "tn", "tr", "tk", "tw", "ug", "uk",
             "ur", "uz", "ve", "vi", "vo", "wa", "cy", "wo", "xh", "yi", "yo", "za", "zu"]


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

    assert response.status_code == 200


def test_language_codes():
    for iso_code in iso_codes:
        request = url_language + iso_code
        response = requests.get(request)
        assert response.status_code == 200
