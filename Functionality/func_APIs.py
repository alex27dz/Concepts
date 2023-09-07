import requests
import pytest
'''
API requests are the mechanisms by which one software application sends a request to another application's API to perform certain actions or retrieve specific information

Components of an API Request:

* HTTP Method (Request Verb): The HTTP method specifies the type of action you want to perform on the resource. Common methods include:
    * GET: Retrieve data from the server.
    * POST: Send data to the server to create a new resource.
    * PUT: Update an existing resource on the server.
    * DELETE: Delete a resource on the server.

* URL (Uniform Resource Locator): The URL identifies the specific endpoint (resource) on the server that the request is targeting.

* Headers: Headers provide additional information about the request, such as authentication tokens, content type, and more.

* Request Body (Optional): For methods like POST and PUT, the request body contains the data you're sending to the server.

API Response:
After sending an API request, the server processes the request and sends back an API response. 

The response typically includes:
    * Status Code: A three-digit code indicating the outcome of the request (e.g., 200 for success, 404 for not found, 500 for internal server error).
    * Headers: Additional metadata about the response.
    * Response Body: The actual data sent by the server in response to the request. This can be in various formats like JSON, XML, HTML, etc.

Authentication:
Many APIs require authentication to ensure only authorized users can access their resources. 
This is often done using tokens (API keys, access tokens, etc.) that are included in the request headers.
'''

def postman_API():
    print('Add Learning Record API')
    url = "http://postman-echo.com/get"
    headers = {"Content-Type": "application/json"}
    body = {
            "args": {},
            "headers": {
                "x-forwarded-proto": "http",
                "x-forwarded-port": "80",
                "host": "postman-echo.com",
                "x-amzn-trace-id": "Root=1-64e9370b-0ae159ae79b5d3ef3ff1afa2",
                "user-agent": "PostmanRuntime/7.32.3",
                "accept": "*/*",
                "postman-token": "37cf0a76-fa63-4f5e-9565-d370db89298e",
                "accept-encoding": "gzip, deflate, br"
            },
            "url": "http://postman-echo.com/get"
    }

    # sending get request
    response = requests.get(url, json=body, headers=headers)
    print(response.status_code)  # 200 success
    print(response.json())
    print(response.text)
postman_API()



def test_get_user_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    print(response.status_code)  # 200 success
    data = response.json()
    print(data)
    print(data['username'])
    assert response.status_code == 200
    assert data["username"] == "Bret"



def test_post_with_authentication():
    url = "https://api.example.com/resource"
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    data = {"key": "value"}
    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)  # 200 success
    data = response.json()
    print(data)

    assert response.status_code == 201
    assert data["message"] == "Success"



def test_error_handling():
    response = requests.get("https://jsonplaceholder.typicode.com/nonexistent")
    assert response.status_code == 404
    error_data = response.json()
    assert error_data["message"] == "Resource not found"


import pytest
import requests


def test_put_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {"title": "Updated Title"}

    response = requests.put(url, json=data)

    assert response.status_code == 200
    updated_post = response.json()
    assert updated_post["title"] == "Updated Title"



def test_delete_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "Post deleted successfully"








def test_create_post_no_authentication():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "New alex Post",
        "body": "This is a new post.",
        "userId": 1
    }
    response = requests.post(url, json=data)

    print(response.status_code)
    assert response.status_code == 201
    response_data = response.json()
    print(response_data)
    assert response_data["title"] == "New alex Post"
    assert response_data["body"] == "This is a new post."
    assert response_data["userId"] == 1







