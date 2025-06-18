from server.config import db, create_app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed Restaurants
    r1 = Restaurant(name="Kiki's Pizza", address="123 Main St")
    r2 = Restaurant(name="Pizza Palace", address="456 Oak Ave")
    db.session.add_all([r1, r2])

    # Seed Pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    db.session.add_all([p1, p2])

    # Seed RestaurantPizzas
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r2, pizza=p2)
    db.session.add_all([rp1, rp2])

    db.session.commit()
    print("Database seeded successfully!")