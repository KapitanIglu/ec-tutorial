# API Testing

## Name

api-testing

## Description

Write pytest-based tests for this repo's Flask API endpoints. Use this skill when asked to create, improve, or debug API tests for the Python backend.

## Instructions

When writing tests for this repo:

1. Use **pytest** with Flask's built-in test client
2. Place test files in the `python/` folder with a `test_` prefix
3. Use a `client` fixture that creates a test client from the app
4. Follow the **arrange / act / assert** pattern
5. Test both happy paths and error cases (404, 400)
6. Use descriptive test function names: `test_<endpoint>_<scenario>`
7. Check status codes AND response body structure

### Endpoints available

| Method | Path | Description |
|--------|------|-------------|
| GET | `/entries` | Returns all experiment entries |
| GET | `/entries/<id>` | Returns one entry by id |
| POST | `/entries` | Creates a new entry (requires: tool, task, expected, actual, verdict) |
| GET | `/summary` | Returns aggregated verdict counts |

### Resource

See [test_template.py](./test_template.py) for a reusable template with fixtures and example patterns.
