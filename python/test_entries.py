import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def sample_entry():
    """A valid entry payload for POST /entries."""
    return {
        "tool": "Copilot",
        "task": "Write a function",
        "expected": "Correct output",
        "actual": "Correct output",
        "verdict": "Faster",
    }


# --- GET /entries ---


def test_get_entries_returns_200(client):
    response = client.get("/entries")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


# --- GET /entries/<id> ---


def test_get_entry_returns_matching_entry(client):
    # Arrange: get an existing id from the entries list
    entries = client.get("/entries").get_json()
    if entries:
        entry_id = entries[0]["id"]

        # Act
        response = client.get(f"/entries/{entry_id}")

        # Assert
        assert response.status_code == 200
        data = response.get_json()
        assert data["id"] == entry_id


def test_get_entry_not_found_returns_404(client):
    response = client.get("/entries/nonexistent-id")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data


# --- POST /entries ---


def test_post_entry_returns_201(client, sample_entry):
    response = client.post("/entries", json=sample_entry)
    assert response.status_code == 201
    data = response.get_json()
    assert data["tool"] == sample_entry["tool"]
    assert data["task"] == sample_entry["task"]
    assert data["verdict"] == sample_entry["verdict"]
    assert "id" in data
    assert "timestamp" in data


def test_post_entry_missing_fields_returns_400(client):
    response = client.post("/entries", json={"tool": "Copilot"})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


def test_post_entry_empty_body_returns_400(client):
    response = client.post("/entries", json={})
    assert response.status_code == 400


def test_post_entry_no_json_returns_error(client):
    response = client.post("/entries", data="not json")
    assert response.status_code in (400, 415)


# --- GET /summary ---


def test_summary_returns_200_and_expected_shape(client):
    response = client.get("/summary")
    assert response.status_code == 200
    data = response.get_json()
    assert "total" in data
    assert "by_verdict" in data
    assert isinstance(data["total"], int)
    assert isinstance(data["by_verdict"], dict)


def test_summary_total_matches_entries_count(client):
    entries = client.get("/entries").get_json()
    summary = client.get("/summary").get_json()
    assert summary["total"] == len(entries)
