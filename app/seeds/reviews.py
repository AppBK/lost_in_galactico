from faker import Faker
from ..models import User, Product, Review, db, environment, SCHEMA
from random import randint
from datetime import date
from sqlalchemy.sql import text

fake = Faker()


def seed_reviews():
    new_Review1 = Review(
        user_id=1,
        product_id=1,
        review=fake.text(),
        created_at=date.today()
    )

    db.session.add(new_Review1)
    db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
