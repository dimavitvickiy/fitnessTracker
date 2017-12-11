import pytest

from app.helpers.password import (
    generate_password,
    generate_password_first_mutation,
    generate_password_second_mutation,
)


def test_generate_password():
    correct_hash = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
    assert correct_hash == generate_password('password')


@pytest.mark.xfail
def test_generate_password_first_mutation():
    correct_hash = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
    assert correct_hash == generate_password_first_mutation('password')


@pytest.mark.xfail
def test_generate_password_second_mutation():
    correct_hash = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
    assert correct_hash == generate_password_second_mutation('password')
