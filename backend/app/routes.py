from flask import Blueprint, request, jsonify
from app.services.google_shopping import GoogleShoppingAPI
from app.services.product_matcher import ProductMatcher

api = Blueprint('api', __name__)
google_shopping = GoogleShoppingAPI()
product_matcher = ProductMatcher()

@api.route('/api/search', methods=['POST'])
def search_deals():
    data = request.get_json()
    product_info = data.get('productInfo')
    
    # Search for similar products
    similar_products = product_matcher.find_similar_products(product_info)
    
    # Get prices from Google Shopping
    deals = google_shopping.search_products(similar_products)
    
    return jsonify(deals) 