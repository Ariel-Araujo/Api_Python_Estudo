import requests

# data = {"username":"Ariel", "secret": "@admin456", "cargo": "Engenheiro", "nome": "Jose", "salario": "5000"}
# response = requests.post("http://127.0.0.1:5000/register", data=data)

response = requests.get("http://127.0.0.1:5000/empregados")

if response.status_code == 200:
    message = response.json()
    print(message['empregados'])
else:
    print(response.status_code)