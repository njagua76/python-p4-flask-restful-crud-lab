from app import app
from models import db, Plant

with app.app_context():
    print("Clearing old plants...")
    Plant.query.delete()

    print("Seeding plants...")

    plants = [
        Plant(name="Aloe", image="./images/aloe.jpg", price=11.50, is_in_stock=True),
        Plant(name="ZZ Plant", image="./images/zz-plant.jpg", price=25.00, is_in_stock=True),
        Plant(name="Pothos", image="./images/pothos.jpg", price=15.00, is_in_stock=False),
    ]

    db.session.add_all(plants)
    db.session.commit()
    
    print("Done!")
