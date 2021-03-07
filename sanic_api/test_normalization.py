import json

from sanic_api.normalization import normalize_list


def test_example():
    # Given not normalized json
    # When running normalize_list
    # Then return normalized value
    test_value = """
    [
        {
            "name": "device",
            "strVal": "iPhone",
            "metadata": "not interesting"
        },
        {
            "name": "isAuthorized",
            "boolVal": "false",
            "lastSeen": "not interesting"
        }
    ]
    """
    expected = {
        "device": "iPhone",
        "isAuthorized": "false"
    }
    value = json.loads(test_value)
    assert expected == normalize_list(value)
