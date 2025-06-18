# Pizza Restaurant API
A RESTful API for managing pizza restaurants, pizzas, and their associations, built with Flask, SQLAlchemy, and Flask-Migrate. This project follows the MVC pattern and includes models, routes, and validations, tested via Postman.

## Database Migration & Seeding
Migration: Run flask db init to set up migrations, flask db migrate -m "Initial migration" to generate migration scripts, and flask db upgrade to apply them, creating pizza.db.
Seeding: Run python server/seed.py to populate the database with sample restaurants, pizzas, and associations. Ensure PYTHONPATH=$PWD is set to resolve imports.