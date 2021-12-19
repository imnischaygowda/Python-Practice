'''
Author: Nischay Gowda
Date: 2021-12-18 20:05:49
'''
import requests
from requests import sessions
from requests.models import HTTPBasicAuth



people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)
print('\n')
people_json = people.json()
print(people_json)

print("Number of people in space:",people_json['number'])

# response.content
# response.text
# response.json

# # Query
# query = {'lat':'45','lon':'180'}
# response = requests.get('http://api.open-notify.org/iss-pass.json',params=query)
# print(response.json())

# # create and modify data
# response = requests.post('https://httpbin.org/post',data = {'key':'value'})

# # Update an existing resource
# requests.put('https://httpbin.org/put',data = {'key':'value'})

# # Access REST Headers
# print(response.headers["date"])


# # Authenticate Rest API
# requests.get('https://api.github.com/user',auth=HTTPBasicAuth('thenischaygowda','Nischay@105'))
# my_headers = {'Authorization':'Bearer {access_token}'}
# response = requests.get('http://httpbin.org/headers',headers=my_headers)
# print(response)

# # Sessions
# session = requests.Session()
# session.headers.update({'Authorization':'Bearer{access_token}'})
# response = session.get('https://httpbin.org/headers')


# # HTTP errors
# response = requests.get("http://api.open-notify.org/astrs.json")
# if (response.status_code == 200):
#     print("The request was a sucess!")
#     # Code here will only run if request is successful
# elif (response.status_code == 404):
#     print("Result not found!")
#     # Code here will react to failed requests


# # To catch specific error
# try:
#     response = requests.get('http://api.open-notify.org/astros.json')
#     response.raise_for_status()
#     # 
# except requests.exceptions.HTTPError as error:
#     print(error)

# # Too many redirects
# try:
#     response = requests.get('http://api.open-notify.org/astros.json')
#     response.raise_for_status()
# except requests.exceptions.TooManyRedirects as error:
#     print(error)




# # Robust API
# try:
#     response = requests.get('http://api.open-notify.org/astro.json',timeout=5)
#     response.raise_for_status()
# except requests.exceptions.HTTPError as errh:
#     print(errh)
# except  requests.exceptions.ConnectionError as errc:
#     print(errc)
# except  requests.exceptions.Timeout as errt:
#     print(errt)
# except requests.exceptions.RequestException as err:
#     print(err)



