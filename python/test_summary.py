import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_summary_returns_200_and_expected_shape(client):
    response = client.get('/summary')
    assert response.status_code == 200
    data = response.get_json()
    assert 'total' in data
    assert 'by_verdict' in data


# Lab 2 Challenge: add more tests below this line


def test_summary_contains_by_tool(client):
    response = client.get('/summary')
    data = response.get_json()
    assert 'by_tool' in data


def test_summary_total_is_integer(client):
    response = client.get('/summary')
    data = response.get_json()
    assert isinstance(data['total'], int)


def test_summary_by_verdict_is_dict_with_counts(client):
    response = client.get('/summary')
    data = response.get_json()
    assert isinstance(data['by_verdict'], dict)
    for value in data['by_verdict'].values():
        assert isinstance(value, int)


def test_summary_by_tool_has_correct_structure(client):
    response = client.get('/summary')
    data = response.get_json()
    assert isinstance(data['by_tool'], dict)
    for tool_name, verdicts in data['by_tool'].items():
        assert isinstance(tool_name, str)
        assert isinstance(verdicts, dict)
        for count in verdicts.values():
            assert isinstance(count, int)
