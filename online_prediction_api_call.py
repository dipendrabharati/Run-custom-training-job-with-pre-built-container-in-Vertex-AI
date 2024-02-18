# Endpoint model deployed. Resource name: projects/your-project-id/locations/us-central1/endpoints/your-endpoint-id

from google.cloud import aiplatform

# endpoint_name  = projects/your-project-id/locations/us-central1/endpoints/your-endpoint-id
endpoint = aiplatform.Endpoint(
    endpoint_name="projects/rugged-research-400319/locations/us-central1/endpoints/550382535515832320"
)

# using total room as a feature
# my_feature = [[1960], [3400], [3677], [2202], [2403], [5652], [3318], [2552], [1364], [3468]]
# this is the format we are using while training the model (model.fit())
my_feature = [[1960], [3400]]

response = endpoint.predict(my_feature)

print('API response: ', response)

for i in range(len(my_feature)):
    print("Number of rooms" + "   " + " Predicted House Price")
    print( my_feature[i][0], "               ", response.predictions[i][0])

# ENDPOINT=$(cat deploy-output.txt | sed -nre 's:.*Resource name\: (.*):\1:p' | tail -1)
# sed -i "s|ENDPOINT_STRING|$ENDPOINT|g" predict.py
# python3 predict.py