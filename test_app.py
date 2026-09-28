from app import add, multiply

def test_add():
    assert add(10, 20) == 30

def test_multiply():
    assert multiply(5, 4) == 20


from app import register_user

def test_register_user():
    assert register_user("Nidhi") == "User Nidhi registered successfully"
