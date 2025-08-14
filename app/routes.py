from .user_controller import UserController
from .meal_controller import MealController
from flask_login import login_required

def register_user_routes(app):
    user = UserController()

    @app.route('/login', methods = ["POST"])
    def login():
        return user.login()
    
    @app.route('/logout', methods = ["GET"])
    @login_required
    def logout():
        return user.logout()
    
    @app.route('/user', methods = ["POST"])
    def create_user():
        return user.create_user()
    
    @app.route('/user/<int:user_id>', methods = ["GET"])
    @login_required
    def get_user(user_id):
        return user.get_user(user_id)
    
    @app.route('/user/<int:user_id>', methods = ["PATCH"])
    @login_required
    def update_user(user_id):
        return user.update_user(user_id)
    
    @app.route('/user/<int:user_id>', methods = ["DELETE"])
    @login_required
    def delete_user(user_id):
        return user.delete_user(user_id)
    
def register_meal_routes(app):
    meal = MealController()

    @app.route('/meal/register', methods = ["POST"])
    @login_required
    def register_meal():
        return meal.register_meal()
    
    @app.route('/meal/list', methods = ["GET"])
    @login_required
    def list_meals():
        return meal.list_meals()
    
    @app.route('/meal/update/<int:meal_id>', methods = ["PUT"])
    @login_required
    def update_meal(meal_id):
        return meal.update_meal(meal_id)
    
    @app.route('/meal/<int:meal_id>', methods = ["GET"])
    @login_required
    def get_meal(meal_id):
        return meal.get_meal(meal_id)

    
    @app.route('/meal/delete/<int:meal_id>', methods = ["DELETE"])
    @login_required
    def delete_meal(meal_id):
        return meal.delete_meal(meal_id)
