from app.helpers.password import generate_password


def test_generate_password():
    correct_hash = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
    assert correct_hash == generate_password('password')
