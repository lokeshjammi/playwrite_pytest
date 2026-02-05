import pytest

#Marking a function with a marker(marker is nothing but user defined fixture)
@pytest.mark.login
def test_login():
    print("I am inside test_login function")
    return "Login successful"

@pytest.mark.logout
def test_logout():
    print("I am inside test_logout function")
    return "Logout successful"

@pytest.mark.create_user
def test_create_user():
    print("I am inside test_create_user function")
    return "User created successfully"

@pytest.mark.skip
def test_edit_user():
    print("I am inside test_edit_user function")
    return "User edited successfully"