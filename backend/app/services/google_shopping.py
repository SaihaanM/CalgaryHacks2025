import requests
from config import Config

class GoogleShoppingAPI:
    def __init__(self):
        self.api_key = Config.GOOGLE_SHOPPING_API_KEY
        self.base_url = "https://shopping.googleapis.com/v1/products"

    def search_products(self, query):
        try:
            params = {
                'key': self.api_key,
                'q': query,
                'country': 'US'
            }
            response = requests.get(self.base_url, params=params)
            return response.json()
        except Exception as e:
            print(f"Error searching Google Shopping: {e}")
            return [] 