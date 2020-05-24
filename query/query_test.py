from utils import db_utils as dbu
import pymongo
import pprint

category_collection = dbu.get_collection('category')
product_collection = dbu.get_collection('product')
user_collection = dbu.get_collection('user')
order_collection = dbu.get_collection('order')
review_collection = dbu.get_collection('review')


def find_query_test():
    review_collection.create_index([('product_id', pymongo.ASCENDING)])

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


def paging_test():
    sample_product = product_collection.find_one({"slug": "wheel-barrow-9092"})
    reviews_count = review_collection.count_documents({"product_id": sample_product['_id']})
    num_item_per_page = 2
    total_page = int(reviews_count / num_item_per_page) if reviews_count % num_item_per_page == 0 else int(reviews_count / num_item_per_page) + 1

    print('===============================================================================')
    for num_page in range(total_page):
        print('Review Page', num_page + 1)
        print('===============================================================================')
        reviews = review_collection.find({"product_id": sample_product['_id']}) \
            .skip((num_page) * num_item_per_page) \
            .limit(num_item_per_page) \
            .sort([('rating', pymongo.DESCENDING)])
        for review in reviews:
            pprint.pprint(review)
            print('===============================================================================')


if __name__ == "__main__":
    paging_test()
