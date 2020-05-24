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

def sibling_category_test():
    outdoor_category = category_collection.find_one({"slug": "outdoors"})
    sibling_categories = category_collection.find({"parent_id": outdoor_category['_id']})

    print('===============================================================================')
    print('Sibling Category(Parent : outdoors)')
    print('===============================================================================')
    for category in sibling_categories:
        pprint.pprint(category)
        print('===============================================================================')

def null_field_test():
    categories = category_collection.find({"parent_id": None})

    print('===============================================================================')
    print('None Parent Category')
    print('===============================================================================')
    for category in categories:
        pprint.pprint(category)
        print('===============================================================================')

def project_test():
    user_with_full_field = user_collection.find_one({"username": "kbanker1", "hashed_password": "bd1cfa194c3a603e7186780824b044191"})
    user_with_only_id_field = user_collection.find_one({"username": "kbanker1", "hashed_password": "bd1cfa194c3a603e7186780824b044191"}, {'_id': 1})

    print('===============================================================================')
    print('User with Full Field')
    print('===============================================================================')
    pprint.pprint(user_with_full_field)

    print('===============================================================================')
    print('User with Only Id Field')
    print('===============================================================================')
    pprint.pprint(user_with_only_id_field)

if __name__ == "__main__":
    project_test()
