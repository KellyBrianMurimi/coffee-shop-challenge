# ☕ Coffee Shop Challenge

## Project Overview

This is a Python-based Object-Oriented Programming (OOP) challenge that models a Coffee Shop system using three main classes:

- `Customer`
- `Coffee`
- `Order`

These classes reflect a real-world many-to-many relationship between `Customer` and `Coffee` through `Order`. Each `Order` belongs to a single `Customer` and a single `Coffee`. The project also includes aggregate methods and data validation to simulate core behaviors in a coffee shop system.

## 📁 Folder Structure
coffee-shop-challenge/
├── Pipfile
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
├── customer_test.py
├── coffee_test.py
└── order_test.py

## 🛠 Setup Instructions

1. **Clone the repository**
   git clone git@github.com:<your-username>/coffee-shop-challenge.git
   cd coffee-shop-challenge
2. **Initialize Python environment**
pipenv install
pipenv shell
3. **Initial commit**
git add .
git commit -m "chore: scaffold project structure"

## 🧩 Models and Requirements
Customer

__init__(self, name)
Stores a name (must be str, 1–15 characters).
Properties
name:
Getter: returns the customer’s name.
Setter: enforces str type and 1–15 character limit.
Methods
orders(): returns all Order instances for that customer.
coffees(): returns a unique list of Coffee instances ordered.
create_order(coffee, price): creates a new Order.

Coffee

__init__(self, name)
Stores a name (must be str, at least 3 characters).

Properties
name:
Getter: returns the coffee name.
Immutable after initialization.
Methods
orders(): returns all Order instances for this coffee.
customers(): returns a unique list of Customer instances who’ve ordered it.
num_orders(): total number of orders for this coffee.
average_price(): mean of all order prices (0 if none).

Order

__init__(self, customer, coffee, price)
Accepts a Customer instance, a Coffee instance, and a price (float between 1.0–10.0).

Properties
customer: Getter returns the associated Customer (type-checked).
coffee: Getter returns the associated Coffee (type-checked).
price: Getter returns the order price (immutable, validated).

## ⭐ Bonus Feature
Customer.most_aficionado(coffee)
Class method
Returns the customer who spent the most on a given coffee.
Returns None if no orders exist.

## ✅ Testing
Unit tests for each class are located in the tests/ directory:

tests/customer_test.py
tests/coffee_test.py
tests/order_test.py

### 🧪 Running Tests
Run "python -m unittest discover -s tests -p "*_test.py" -v" to run all the tests.

## Running code
Run python debug.py in the terminal to execute and display output from the script.

## Technologies used
Python

## License

Copyright <2025> <Kelly>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

