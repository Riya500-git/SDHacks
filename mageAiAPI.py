# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import json
import requests


response = requests.post(
    url='https://api.mage.ai/v1/predict',
    headers={
        'Content-Type': 'application/json',
    },
    data=json.dumps({
        'api_key': 'G00GWJa65aPbmFKVp9Zv4GvIectoLwKaA5wl1aH5',
        'model': 'recommendations_rank_1649534003947',
        'version': '3',
        'features': [{
            "id": "AZ"
        }],
    }),
)
#{
  #"api_key": "G00GWJa65aPbmFKVp9Zv4GvIectoLwKaA5wl1aH5",
  #"features": [
    #{"state_": "AZ"}
  #],
  #"include_features": false,
  # "model": "recommendations_rank_1649534003947",
  # "version": "3"
#}

predictions = response.json()
print(predictions)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
