import pytest

@pytest.fixture(scope="module")
def login():
    print("I am inside test_sample_login function")
    yield

@pytest.fixture(scope="function")
def before_each_function():
    print("I am inside before_each_function function")
    yield

@pytest.fixture(scope="function")
def land_user_on_dashboard():
    print("I am inside land_user_on_dashboard function")
    yield

@pytest.fixture(scope="function")
def logout():
    print("I am inside test_logout function")
    yield
    
@pytest.mark.usefixtures("login", "before_each_function", "logout", "land_user_on_dashboard")
def test_all_scenarios():
    return "All the test scenarios are passed"