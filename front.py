import requests

headers = {'Accept': 'application/json'}

# res = requests.get('http://127.0.0.1:5000/api/tasks/0')
res = requests.put('http://127.0.0.1:5000/api/tasks/1' , {"title": "Buy groceries"})
# res = requests.post('http://127.0.0.1:5000/api/tasks/3',{"title": "Go to the gym"})
# res = requests.delete('http://127.0.0.1:5000/api/tasks/1',{"title": "Buy some milk"})


print(res.json())

