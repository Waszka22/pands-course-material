import requests

# Replace the placeholder values with your actual CSO API credentials
api_key = "YOUR_API_KEY"
headers = {
    "Ocp-Apim-Subscription-Key": api_key
}

# Make a GET request to the CSO API endpoint for population statistics
response = requests.get("https://data.cso.ie/census-rest-api/action/datastore_search?resource_id=96752403-3f91-4309-bbf9-c25b7da04ef6&limit=1000", headers=headers)

# Check if the API call was successful
if response.status_code == 200:
    # Parse the response JSON data
    data = response.json()
    # Filter the data to only include records for 18-year-olds and since 1990
    records = [record for record in data["result"]["records"] if record["Age"] == "18 years" and int(record["Year"]) >= 1990]
    # Group the records by year and calculate the total number of 18-year-olds for each year
    by_year = {}
    for record in records:
        year = record["Year"]
        if year not in by_year:
            by_year[year] = 0
        by_year[year] += int(record["Value"])
    # Print the number of 18-year-olds for each year
    for year, value in by_year.items():
        print("Year:", year)
        print("Number of 18-year-olds:", value)
        print("------------------------------")
else:
    # If the API call was unsuccessful, print the error message
    print("Failed to retrieve population statistics:", response.text)
