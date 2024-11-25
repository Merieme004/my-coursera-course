# features/steps/load_steps.py

from behave import given
from app import db
from app.models import Product

@given('the following products exist')
def step_impl(context):
    for row in context.table:
        product = Product(name=row['name'], description=row['description'], price=row['price'], category=row['category'], availability=row['availability'])
        db.session.add(product)
    db.session.commit()
