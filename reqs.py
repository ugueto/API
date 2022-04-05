import requests

# Short script to try multiple requests from Flask API - manual testing.

api_base = 'http://127.0.0.1:5000/customers/'

# GET all current customers
response = requests.get(api_base)
print(response.json())
input()  # Hit Enter to continue with requests

# DELETE David Soria
response = requests.delete(api_base + "dsoria@gmail.com")
print(response)
input()  # Should output 204

# UPDATE Pilar Martin to Pedro Martin
response = requests.put(api_base + "mvelez@yahoo.es", json={"name": "Miguel",
                                                            "surname": "Velez",
                                                            "birthdate": "10/10/1998"})
print(response)  # Should output 200 - if 400 error check http and not https.
input()

# POST Esteban Martinez
response = requests.post(api_base + "emartinez@gmail.com", json={"name": "Esteban",
                                                                 "surname": "Martinez",
                                                                 "birthdate": "13/02/2001"})
print(response)  # Should output 201- if 400 error check http and not https.
input()

# GET all current customers finally
response = requests.get(api_base)
print(response.json())
