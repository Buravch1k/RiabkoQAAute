import pytest
import requests


@pytest.mark.http
def test_first_request():
    response = requests.get("https://api.github.com/zen")
    print(f"Response is:{response.text}")


@pytest.mark.http
def test_second_request():
    response = requests.get("https://api.github.com/users/defunkt")
    body = response.json()
    headers = response.headers

    assert body["name"] == "Chris Wanstrath"
    assert response.status_code == 200
    assert headers["Server"] == "GitHub.com"


@pytest.mark.http
def test_status_code_request():
    response = requests.get("https://api.github.com/users/sergii_butenko")

    assert response.status_code == 404
