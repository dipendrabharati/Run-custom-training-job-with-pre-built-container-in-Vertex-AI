# Endpoint model deployed. Resource name: projects/your-project-id/locations/us-central1/endpoints/your-endpoint-id

from google.cloud import aiplatform

endpoint = aiplatform.Endpoint(
    endpoint_name="ENDPOINT_STRING"
)

# A test example we'll send to our model for prediction
test_mpg = []

response = endpoint.predict([test_mpg])

print('API response: ', response)

print('Predicted MPG: ', response.predictions[0][0])

# ENDPOINT=$(cat deploy-output.txt | sed -nre 's:.*Resource name\: (.*):\1:p' | tail -1)
# sed -i "s|ENDPOINT_STRING|$ENDPOINT|g" predict.py
# python3 predict.py