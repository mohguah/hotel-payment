#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
from itertools import product
from locale import currency
import os
from flask import Flask, redirect, request

import stripe
# This is a public sample test API key.
# Don’t submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.
stripe.api_key = 'sk_test_51LsUfGCpUbUMkUvohMy9I5yYVldD0sPXiK3bu7IKb5ych41AnqxHQOcWzTVVq8zB6K3yiM7SkOdNK0LD8QNwppdN00094VN0s6'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:4242'

peisestua = stripe.Product.create(name="Peisestua, 1 natt")

price = stripe.Price.create(
    unit_amount=140000,
    currency="nok", 
    product=peisestua
)


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': price,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '?success=true',
            cancel_url=YOUR_DOMAIN + '?canceled=true',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(port=4242)