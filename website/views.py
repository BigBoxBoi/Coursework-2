from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from flask_login import current_user, login_required
from .models import Products, User_accounts
from .dbinit import insert_products
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    try:
        # Insert initial data into database
        insert_products()
    except Exception as e:
        # Handle any errors that occur during insertion
        print("Error inserting data: ", e)

    # Retrieve all products from database
    products = Products.query.all()

    return render_template('home.html', products=products, user=current_user)


@views.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # get the current cart list from session or create an empty one
    cart = session.get('cart', [])

    # add the product_id to the cart list
    cart.append(product_id)

    # update the cart list in the session
    session['cart'] = cart

    # redirect to the cart page
    return redirect(url_for('views.cart'))


@views.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    # Retrieve the cart list from the Flask session
    cart = session.get('cart', [])

    # Create a dictionary to hold the product information
    products = {}

    # Query the database for the product information
    for product_id in set(cart):
        product = Products.query.filter_by(product_id=product_id).first()
        if product:
            products[product_id] = {
                'name': product.name,
                'price': product.price,
                'quantity': cart.count(product_id)
            }

    # Calculate the total price of all items in the cart
    total_price = sum(products[product_id]['price'] * products[product_id]['quantity'] for product_id in products)

    # Update the cart with the new quantity values
    if request.method == 'POST':
        for product_id, product in products.items():
            quantity = request.form.get('quantity{}'.format(product_id))
            if quantity:
                update_cart(product_id, int(quantity))

    return render_template('cart.html', products=products, total_price=total_price, user = current_user)


@views.route('/update_cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    # Retrieve the cart list from the Flask session
    cart = session.get('cart', [])

    # Update the quantity of the product in the cart
    for i, item in enumerate(cart):
        if item == product_id:
            cart[i] = product_id
            break

    # Remove any products from the cart with a quantity of 0
    cart = [item for item in cart if cart.count(item) > 0]

    # Update the cart list in the session
    session['cart'] = cart

    return redirect(url_for('views.cart'))



@views.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    # Retrieve the cart list from the Flask session
    cart = session.get('cart', [])

    # Remove the product_id from the cart list
    cart.remove(product_id)

    # update the cart list in the session
    session['cart'] = cart

    # redirect to the cart page
    return redirect(url_for('views.cart'))


