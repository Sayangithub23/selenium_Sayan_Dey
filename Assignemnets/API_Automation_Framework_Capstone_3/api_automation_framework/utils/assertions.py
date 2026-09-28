def assert_status(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status {expected_status}, "
        f"got {response.status_code}. Response: {response.text}"
    )


def assert_json_response(response):
    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type, (
        f"Expected JSON response but got: {content_type}"
    )


def assert_has_keys(data, keys):
    for key in keys:
        assert key in data, f"Missing key: {key}"
