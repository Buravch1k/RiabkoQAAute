import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object(sign_in_page):
    sign_in_page.try_login("test@gmail.com", "wrong_password")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()
