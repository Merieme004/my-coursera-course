# tests/factories.py

from faker import Faker
import random

fake = Faker()

class ProductFactory:
    @staticmethod
    def create_fake_product():
        """Generate a fake product"""
        return {
            "name": fake.word(),
            "description": fake.text(),
            "price": round(random.uniform(10, 100), 2),
            "category": fake.word(),
            "availability": random.choice([True, False]),
        }

# Example of generating a fake product
if __name__ == "__main__":
    product = ProductFactory.create_fake_product()
    print(product)
