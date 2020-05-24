from utils import db_utils as dbu
import datetime

dbu.init()

category_collection = dbu.get_collection('category')
product_collection = dbu.get_collection('product')
user_collection = dbu.get_collection('user')
order_collection = dbu.get_collection('order')
review_collection = dbu.get_collection('review')

home_category = {
    "_id": "1001",
    "name": "Home",
    "slug": "home"
}

category_collection.insert_one(home_category)

outdoors_category = {
    "_id": "1002",
    "name": "Outdoors",
    "slug": "outdoors"
}

category_collection.insert_one(outdoors_category)

gardening_category = {
    "_id": "1003",
    "slug": "gardening-tools",
    "name": "Gardening Tools",
    "description": "Gardening gadgets galore!",
    "parent_id": outdoors_category["_id"],
    "ancestors": [home_category, outdoors_category]
}

category_collection.insert_one(gardening_category)

lawn_trimmer_category = {
    "_id": "1004",
    "slug": "lawn-trimmers",
    "name": "Lawn Trimmers",
    "description": "Lawn trimmers galore!",
    "parent_id": outdoors_category["_id"],
    "ancestors": [home_category, outdoors_category]
}

category_collection.insert_one(lawn_trimmer_category)

sample_product_detail = {
    "weight": 45,
    "weight_units": "lbs",
    "model_num": 4039283402,
    "manufacturer": "Acme",
    "color": "Green"
}

sample_product = {
    "_id": "2001",
    "slug": "wheel-barrow-9092",
    "sku": "9092",
    "name": "Extra Large Wheelbarrow",
    "description": "Heavy duty wheelbarrow...",
    "details": sample_product_detail,
    "total_reviews": 4,
    "average_review": 4.5,
    "pricing": {
        "retail": 589700,
        "sale": 489700
    },
    "price_history": [
        {
            "retail": 529700,
            "sale": 429700,
            "start": datetime.datetime(year=2010, month=4, day=1),
            "end": datetime.datetime(year=2010, month=4, day=8)
        },
        {
            "retail": 529700,
            "sale": 529700,
            "start": datetime.datetime(year=2010, month=4, day=9),
            "end": datetime.datetime(year=2010, month=4, day=16)
        }
    ],
    "primary_category": gardening_category["_id"],
    "category_ids": [
        gardening_category["_id"],
        outdoors_category["_id"]
    ],
    "main_cat_id": gardening_category["_id"],
    "tags": ["tools", "gardening", "soil"]
}

product_collection.insert_one(sample_product)

sample_product2 = {
    "_id": "2002",
    "slug": "wheel-barrow-9093",
    "sku": "9093",
    "name": "Extra Small Wheelbarrow",
    "description": "Light duty wheelbarrow...",
    "details": sample_product_detail,
    "total_reviews": 4,
    "average_review": 4.5,
    "pricing": {
        "retail": 589700,
        "sale": 489700
    },
    "price_history": [
        {
            "retail": 529700,
            "sale": 429700,
            "start": datetime.datetime(year=2010, month=4, day=1),
            "end": datetime.datetime(year=2010, month=4, day=8)
        },
        {
            "retail": 529700,
            "sale": 529700,
            "start": datetime.datetime(year=2010, month=4, day=9),
            "end": datetime.datetime(year=2010, month=4, day=16)
        }
    ],
    "primary_category": gardening_category["_id"],
    "category_ids": [
        gardening_category["_id"],
        outdoors_category["_id"]
    ],
    "main_cat_id": gardening_category["_id"],
    "tags": ["tools", "gardening", "soil"]
}

product_collection.insert_one(sample_product2)

user = {
    "_id": "3001",
    "username": "kbanker",
    "email": "kylebanker@gmail.com",
    "first_name": "Kyle",
    "last_name": "Banker",
    "hashed_password": "bd1cfa194c3a603e7186780824b04419",
    "addresses": [
        {
            "name": "home",
            "street": "588 5th Street",
            "city": "Brooklyn",
            "state": "NY",
            "zip": 11215
        },
        {
            "name": "work",
            "street": "1 E. 23rd Street",
            "city": "New York",
            "state": "NY",
            "zip": 10010
        }
    ],
    "payment_methods": [
        {
            "name": "VISA",
            "payment_token": "43f6ba1dfda6b8106dc7"
        }
    ]
}

user2 = {
    "_id": "3002",
    "username": "kbanker",
    "email": "kylebanker@gmail.com",
    "first_name": "Kyle",
    "last_name": "Banker",
    "hashed_password": "bd1cfa194c3a603e7186780824b04419",
    "addresses": [
        {
            "name": "home",
            "street": "588 5th Street",
            "city": "Brooklyn",
            "state": "NY",
            "zip": 11215
        },
        {
            "name": "work",
            "street": "1 E. 23rd Street",
            "city": "New York",
            "state": "NY",
            "zip": 10010
        }
    ],
    "payment_methods": [
        {
            "name": "VISA",
            "payment_token": "43f6ba1dfda6b8106dc7"
        }
    ]
}

user3 = {
    "_id": "3003",
    "username": "kbanker",
    "email": "kylebanker@gmail.com",
    "first_name": "Kyle",
    "last_name": "Banker",
    "hashed_password": "bd1cfa194c3a603e7186780824b04419",
    "addresses": [
        {
            "name": "home",
            "street": "588 5th Street",
            "city": "Brooklyn",
            "state": "NY",
            "zip": 11215
        },
        {
            "name": "work",
            "street": "1 E. 23rd Street",
            "city": "New York",
            "state": "NY",
            "zip": 10010
        }
    ],
    "payment_methods": [
        {
            "name": "VISA",
            "payment_token": "43f6ba1dfda6b8106dc7"
        }
    ]
}

user_collection.insert_one(user)
user_collection.insert_one(user2)
user_collection.insert_one(user3)

order = {
    "_id": "4001",
    "user_id": user["_id"],
    "state": "CART",
    "line_items": [
        {
            "_id": sample_product["_id"],
            "sku": sample_product["sku"],
            "name": sample_product["name"],
            "quantity": 1,
            "pricing": sample_product["pricing"]
        },
        {
            "_id": sample_product2["_id"],
            "sku": sample_product2["sku"],
            "name": sample_product2["name"],
            "quantity": 2,
            "pricing": sample_product2["pricing"]
        }
    ],
    "shipping_address": user["addresses"][0],
    "sub_total": 6196
}

order_collection.insert_one(order)

review = {
    "_id": "5001",
    "product_id": sample_product["_id"],
    "date": datetime.datetime(year=2010, month=5, day=7),
    "title": "Amazing",
    "text": "Has a squeaky wheel, but still a darn good wheelbarrow.",
    "rating": 4,
    "user_id": user["_id"],
    "username": "dgreenthumb",
    "helpful_votes": 3,
    "voter_ids": [
        user["_id"],
        user2["_id"],
        user3["_id"]
    ]
}

review_collection.insert_one(review)

review2 = {
    "_id": "5002",
    "product_id": sample_product["_id"],
    "date": datetime.datetime(year=2010, month=5, day=7),
    "title": "Amazing",
    "text": "Has a squeaky wheel, but still a darn good wheelbarrow.",
    "rating": 3.5,
    "user_id": user["_id"],
    "username": "dgreenthumb",
    "helpful_votes": 2,
    "voter_ids": [
        user["_id"],
        user2["_id"]
    ]
}

review_collection.insert_one(review2)


review3 = {
    "_id": "5003",
    "product_id": sample_product["_id"],
    "date": datetime.datetime(year=2010, month=5, day=9),
    "title": "Amazing",
    "text": "Has a squeaky wheel, but still a darn good wheelbarrow.",
    "rating": 2,
    "user_id": user["_id"],
    "username": "dgreenthumb",
    "helpful_votes": 1,
    "voter_ids": [
        user["_id"]
    ]
}

review_collection.insert_one(review3)
