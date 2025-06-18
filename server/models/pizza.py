from server.config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)

    # Relationships
    restaurant_pizzas = relationship('RestaurantPizza', back_populates='pizza')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }