import requests

def generate_athena_query(query):
    # Preprocess and format the query as necessary
    # Make a request to the Metabase API to generate the Athena query
    url = 'https://your-metabase-url/api/card/123'
    headers = {'Content-Type': 'application/json', 'X-Metabase-Session': 'YOUR_SESSION_ID'}
    payload = {'parameters': {'query': query}}

    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()
    athena_query = response_json['query']
    return athena_query

