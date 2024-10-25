E-Shop Project

This is an e-commerce web application built with Django. The project allows users to browse products, add items to a shopping cart, apply discount coupons, and proceed to a checkout process.


*Features:
    -User authentication and authorization
    -Product listing and detailed view
    -Shopping cart management
    -Coupon system for discounts
    -Order creation and checkout process
    -Asynchronous task handling using Celery with RabbitMQ as the message broker
    -Admin management for products, orders, and coupons


*Technology Stack:
    -Backend: Django 5, Django templates
    -Frontend: HTML, CSS, Bootstrap
    -Message Broker: RabbitMQ (for Celery tasks)
    -Database: SQLite (development), supports other databases like PostgreSQL for production


*Prerequisites:
    -Python 3.8+
    -Django 4+
    -RabbitMQ (for Celery)
    -Redis (optional for caching)



*Installation:
    1.Clone the repository:
        git clone https://github.com/seela-2001/e-shop.git
        cd e-shop

    2.Create a virtual environment and install dependencies using Poetry (you can use virtualenv ):
        pip install poetry
    
    3.Activate the virtual environment:
        poetry shell
    
    4.Configure environment variables:
        Copy .env.example to .env and configure the required settings (e.g., database URL, RabbitMQ configuration).

    5.Apply migrations:
        python manage.py migrate

    6.Run the development server:
        python manage.py runserver

    7.Run Celery worker (ensure RabbitMQ is running):
        celery -A e_shop worker -l info



*Usage:
    -Access the app at http://127.0.0.1:8000.
    -Admin site is available at http://127.0.0.1:8000/admin.
    -Use the admin site to manage products, orders, and coupons.
