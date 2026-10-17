import requests

# GET request
response_get = requests.get('http://localhost:8080/exp.txt')
print(response_get.status_code)
if response_get.status_code == 200:
    print(response_get.text)
else:
    print("Resource not found")

# POST request
data = "This is a new content."
response_post = requests.post('http://localhost:8080/new_file.txt', data=data)
print(response_post.status_code)
print(response_post.text)

# PUT request
data = "Updated content."
response_put = requests.put('http://localhost:8080/new_file.txt', data=data)
print(response_put.status_code)
print(response_put.text)

# DELETE request
response_delete = requests.delete('http://localhost:8080/new_file.txt')
print(response_delete.status_code)
print(response_delete.text)
