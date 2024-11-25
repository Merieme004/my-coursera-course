# features/steps/web_steps.py

from behave import when, then
from flask import jsonify

@when('I add a new product')
def step_impl(context):
    data = {
        "name": "Test Product",
        "description": "Test",
        "price
}