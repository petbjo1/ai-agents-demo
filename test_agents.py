import pytest
from unittest.mock import patch, Mock

from agents import geocode_location, calculate_city_distance, haversine_distance


# ----------------------------
# Test geocode_location
# ----------------------------

@patch("agents.requests.get")
def test_geocode_location_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = [
        {"lat": "59.3293", "lon": "18.0686"}
    ]
    mock_get.return_value = mock_response

    result = geocode_location("Stockholm")

    assert result == {"lat": 59.3293, "lon": 18.0686}
    mock_get.assert_called_once()


@patch("agents.requests.get")
def test_geocode_location_not_found(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = []
    mock_get.return_value = mock_response

    result = geocode_location("UnknownCity")

    assert result is None


# ----------------------------
# Test haversine_distance
# ----------------------------

def test_haversine_distance_stockholm_lulea():
    stockholm = {"lat": 59.3293, "lon": 18.0686}
    lulea = {"lat": 65.5848, "lon": 22.1547}

    distance = haversine_distance(stockholm, lulea)

    # Real distance ≈ 725 km (allow small margin)
    assert 700 < distance < 750


# ----------------------------
# Test calculate_city_distance
# ----------------------------

@patch("agents.geocode_location")
@patch("agents.haversine_distance")
def test_calculate_city_distance_success(mock_haversine, mock_geocode):
    stockholm = {"lat": 59.3293, "lon": 18.0686}
    lulea = {"lat": 65.5848, "lon": 22.1547}

    mock_geocode.side_effect = [stockholm, lulea]
    mock_haversine.return_value = 725.0

    result = calculate_city_distance("Stockholm", "Luleå")

    assert result == 725.0
    assert mock_geocode.call_count == 2
    mock_haversine.assert_called_once_with(stockholm, lulea)


@patch("agents.geocode_location")
def test_calculate_city_distance_failure(mock_geocode):
    mock_geocode.side_effect = [None, None]

    result = calculate_city_distance("City1", "City2")

    assert result is None