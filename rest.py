# #Restful APIs
# # Write a first program with API interaction

# import requests
# import json

# api_url ="https://api.stackexchange.com/docs/badges#order=desc&sort=rank&filter=default&site=stackoverflow"
# response = requests.get(api_url)
# response.json()

#POST METHOD
import requests 
import json 

post_url = "https://jsonplaceholder.typicode.com/posts"

post = {"userId": 1, "id": 101, "title": "RESTFul API", "body": "This is an api class"}

response = requests.post(post_url, json=post)
# print(response.json())

#DELETE POST
post_url = "https://jsonplaceholder.typicode.com/posts/101"
response = requests.delete(post_url)
print(response.json())