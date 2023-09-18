import requests
import pytest
import json

token= "9d0eb672e2b8cb2b6febf3a4a49f652d7c6506ef"
headers = {
    "Authorization": "Bearer {}".format(token)
}

@pytest.fixture
def test_get_all_projects():
    #act
    url = "https://api.todoist.com/rest/v2/projects"
    response = requests.get(url, headers=headers)
    print(response.json())
    list_projects = response.json()
    id_project = list_projects[1]["id"]
    #assert
    assert response.status_code == 200
    return id_project

@pytest.mark.smoke
def test_create_project():
    body_project = {
        "name":"Project 1"
    }
    url = "https://api.todoist.com/rest/v2/projects"
    response = requests.post(url, headers=headers, data=body_project)
    print(response.json())
    #assert
    assert response.status_code == 200
@pytest.mark.smoke
def test_get_project(test_get_all_projects):
    #print(test_get_all_projects)
    url = "https://api.todoist.com/rest/v2/projects"
    response = requests.post(url, headers=headers)
    print(response.json())
    #assert
    assert response.status_code == 200

@pytest.mark.update
def test_update_project(test_get_all_projects):
    url = "https://api.todoist.com/rest/v2/projects" + test_get_all_projects
    data_update = {
        "name": "Project 2",
        "Color": "red"
    }
    response = requests.post(url, headers=headers, data= data_update)
    print(response.json())
    #assert
    assert response.status_code == 200
@pytest.mark.smoke
def test_delete_project(test_get_all_projects):
    url = "https://api.todoist.com/rest/v2/projects" + test_get_all_projects
    response = requests.delete(url, headers=headers)
    #print(response.json())
    #assert
    assert response.status_code == 204