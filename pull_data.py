import requests
import pandas as pd

# Your API key
api_key = 'j1nb8GuGlLxN4qqAVIeEq8FrXztBeox7306XE1WR'

# Base URL for the API
url = 'https://developer.nrel.gov/api/alt-fuel-stations/v1.json'

# Parameters for the request
params = {
    'api_key': api_key   # API key
    #'city': 'San Diego',
    # 'status':'E',
    # 'fuel_type':'ELEC'         # Optional: Limit the number of results
}

# Send the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Optionally save the JSON to a file for later
    with open('stations_data.json', 'w') as json_file:
        json_file.write(response.text)

    # Convert JSON data to pandas DataFrame
    stations_df = pd.json_normalize(data['fuel_stations'])

    # Optionally save the DataFrame to a CSV file
    stations_df.to_csv('stations_data.csv')

    # Print or display the DataFrame
    print(stations_df)
else:
    print(f"Error: {response.status_code}, {response.text}")
