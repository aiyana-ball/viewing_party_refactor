import pytest
from viewing_party.movie import Movie

def test_return_correct_attributes():
    # Arrange

    mulan = Movie("Mulan", "Animation", 5)

    # Act

    # Assert

    assert mulan.title == "Mulan"
    assert mulan.genre == "Animation"
    assert mulan.rating == 5
