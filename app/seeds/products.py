# from faker import Faker
from ..models import User, Product, db, environment, SCHEMA
from random import randint
from datetime import date
from sqlalchemy.sql import text

# fake = Faker()


def seed_products():
    new_product_1 = Product(
        owner_id=1,
        title="2023 Home Kit",
        photo_url="https://galictogear.s3.us-west-1.amazonaws.com/2023.jpeg",
        description="Classic white home kit for the 2023/24 Season.",
        size='Small',
        price=250,
        created_at=date.today()
    )

    db.session.add(new_product_1)

    db.session.commit()

def undo_products():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
