import pytest

def data_provider():
    return [
        ("admin", "jammi"),
        ("user", "lokesh"),
        ("guest", "jaasu")
    ]

@pytest.mark.parametrize("username, password", data_provider())
def test_login_flow(username, password):
    print(f"Given username is {username} and password is {password}")