# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests

model_inputs = {'prompt': 'My friends are cool but they eat too many carbs.'}

res = requests.post('http://localhost:8000/', json = model_inputs)

print(res.json())