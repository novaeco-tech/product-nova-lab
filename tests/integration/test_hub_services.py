import requests
import os

# Service URLs are based on the docker-compose.yml service names
API_URL = "http://api:8000"
APP_URL = "http://app:8080" # This would be tested via E2E tests

def test_api_health_check():
    """
    Tests that the API service is alive and responding.
    """
    response = requests.get(f"{API_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_app_can_fetch_projects_from_api():
    """
    A simple integration test:
    1. (Mock) The API has a list of projects.
    2. The App (or in this case, a test pretending to be the app)
       can fetch that list.
    """
    
    # This test would be more complex in reality, 
    # likely hitting a /projects endpoint that
    # in turn depends on the /auth service from ecosystem-core.
    
    # For this intra-repo test, we'll assume a public /projects endpoint
    response = requests.get(f"{API_URL}/v1/projects")
    
    assert response.status_code == 200
    data = response.json()
    assert "projects" in data
    assert isinstance(data["projects"], list)