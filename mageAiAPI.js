const response = await fetch(
  'https://api.mage.ai/v1/predict',
  {
    body: JSON.stringify({
      api_key: 'G00GWJa65aPbmFKVp9Zv4GvIectoLwKaA5wl1aH5',
      model: 'awesome_house_predictor',
      version: '1',
      features: [{
        floor_count: 4,
        year_built: 1967,
      }],
    }),
    method: 'POST',
  },
);

response.json().then(predictions => console.log(predictions))
