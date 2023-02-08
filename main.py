import requests

r = requests.get('https://dummy.restapiexample.com/api/v1/employees')

result = r.json()

print(result)
