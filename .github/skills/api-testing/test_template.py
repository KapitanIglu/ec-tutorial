"""
Template for API tests in this repo.
Copy this file to python/test_<feature>.py and adapt as needed.
"""

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


# --- Happy path tests ---


def test_get_entries_returns_200(client):
    response = client.get("/entries")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_post_entry_returns_201(client, sample_entry):
    response = client.post("/entries", json=sample_entry)
    assert response.status_code == 201
    data = response.get_json()
    assert data["tool"] == sample_entry["tool"]
    assert "id" in data
    assert "timestamp" in data


# --- Error case tests ---


def test_get_entry_not_found_returns_404(client):
    response = client.get("/entries/nonexistent-id")
    assert response.status_code == 404


def test_post_entry_missing_fields_returns_400(client):
    response = client.post("/entries", json={"tool": "Copilot"})
    assert response.status_code == 400
