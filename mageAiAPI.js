const response = await fetch(
  'https://api.mage.ai/v1/predict',
  {
    body: JSON.stringify({
      api_key: 'G00GWJa65aPbmFKVp9Zv4GvIectoLwKaA5wl1aH5',
      model: 'recommendations_rank_1649534003947',
      version: '3',
      features: [{
        id = "AZ"
      }],
    }),
    method: 'POST',
  },
);

response.json().then(predictions => console.log(predictions))
