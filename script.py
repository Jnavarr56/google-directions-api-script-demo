import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()


origin_query_param = "26-07 160th Street, Queens, NY 11358"
destination_query_param = "41-02 Main St, Queens, NY 11355"
api_key = os.getenv("API_KEY")
api_url = "https://maps.googleapis.com/maps/api/directions/json"

request_url = f'{api_url}?mode=transit&origin={origin_query_param}&destination={destination_query_param}&key={api_key}'

request_response = requests.get(request_url)

response_data_as_dict = json.loads(request_response.content)
response_data_as_json = json.dumps(response_data_as_dict, indent=2)

output_file = open("results.json", "w")
output_file.write(response_data_as_json)

print("Done!")
