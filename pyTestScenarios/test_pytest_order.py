import pytest
import pytest_order

@pytest.mark.order(1)
def test_login():
    print("I am inside test_login function")
    return "Login successful"

@pytest.mark.order(4)
def test_logout():
    print("I am inside test_logout function")
    return "Logout successful"

@pytest.mark.order(before="test_login")
def test_search():
    print("I am inside test_search function")
    return "Search successful"

@pytest.mark.order(2)
def test_add_user():
    print("I am inside test_add_user function")
    return "User added successfully"
