import requests
url = "http://0.0.0.0:9696"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
requests.post(url, json=client).json()