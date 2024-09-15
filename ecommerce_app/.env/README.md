# E-Commerce App

This is a basic e-commerce application built with FastAPI, SQLAlchemy, and Alembic for database migrations. It includes features for managing products, orders, carts, categories, and user authentication.

## Features

- Product management (add, update, delete, list)
- Category management (add, update, delete, list)
- Cart management for buyers
- Order placement and status updates for sellers
- Secure authentication and user registration

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ecommerce-app.git
   cd ecommerce-app
2. Install the required dependencies:

pip install -r requirements.txt

3. Set up your environment variables in the .env file:

DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key

4. Apply database migrations:

alembic upgrade head

5. Run the application:

uvicorn app.main:app --reload


Here is the structure and content for the requested files:

File Structure:
bash
Copy code
.env/
├── alembic.ini
├── README.md
└── requirements.txt
1. alembic.ini
This is the Alembic configuration file that sets up the migration environment.

ini
Copy code
[alembic]
script_location = alembic

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console

[logger_sqlalchemy]
level = WARN
handlers = console
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers = console
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stdout,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(asctime)s %(levelname)-5.5s [%(name)s] %(message)s
2. README.md
This is the documentation file that explains how to use the project.

markdown
Copy code
# E-Commerce App

This is a basic e-commerce application built with FastAPI, SQLAlchemy, and Alembic for database migrations. It includes features for managing products, orders, carts, categories, and user authentication.

## Features

- Product management (add, update, delete, list)
- Category management (add, update, delete, list)
- Cart management for buyers
- Order placement and status updates for sellers
- Secure authentication and user registration

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ecommerce-app.git
   cd ecommerce-app
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your environment variables in the .env file:

bash
Copy code
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key
Apply database migrations:

bash
Copy code
alembic upgrade head
Run the application:

uvicorn app.main:app --reload

API Endpoints
Authentication
POST /auth/register: Register a new user
POST /auth/login: Log in with email and password
Product Management
POST /product/add: Add a new product (Seller)
PUT /product/update/{product_id}: Update a product (Seller)
DELETE /product/delete/{product_id}: Delete a product (Seller)
GET /product/list: List products
Cart Management
POST /cart/add: Add a product to cart (Buyer)
DELETE /cart/remove/{cart_item_id}: Remove a product from cart (Buyer)
GET /cart/view: View the cart (Buyer)
Order Management
POST /order/place: Place an order (Buyer)
PUT /order/update_status/{order_id}: Update order status (Seller)
GET /order/view: View orders (Buyer)
