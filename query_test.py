import db_utils as dbu
import pprint

category_collection = dbu.get_collection('category')
product_collection = dbu.get_collection('product')
user_collection = dbu.get_collection('user')
order_collection = dbu.get_collection('order')
review_collection = dbu.get_collection('review')

def find_query_test():
    sample_product = product_collection.find_one({"slug": "wheel-barrow-9092"})
    category = category_collection.find_one({"_id": sample_product['main_cat_id']})
    reviews = review_collection.find({"product_id": sample_product['_id']})

    print('===============================================================================')
    print('Sample product')
    print('===============================================================================')
    pprint.pprint(sample_product)
    print('===============================================================================')
    print('Category')
    print('===============================================================================')
    pprint.pprint(category)
    print('===============================================================================')
    print('Review')
    print('===============================================================================')
    for review in reviews:
        pprint.pprint(review)
    print('===============================================================================')

if __name__ == "__main__":
    find_query_test()