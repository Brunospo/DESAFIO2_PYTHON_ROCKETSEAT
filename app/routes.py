from .user_controller import UserController
from .diet_controller import DietController
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
    
def register_diet_routes(app):
    diet = DietController()

    @app.route('/register_diet', methods = ["POST"])
    @login_required
    def register_diet():
        return diet.register_diet()
    
    # @app.route('/logout', methods = ["GET"])
    # @login_required
    # def logout():
    #     return user.logout()
    
    # @app.route('/user', methods = ["POST"])
    # def create_user():
    #     return user.create_user()
    
    # @app.route('/user/<int:user_id>', methods = ["GET"])
    # @login_required
    # def get_user(user_id):
    #     return user.get_user(user_id)
    
    # @app.route('/user/<int:user_id>', methods = ["PATCH"])
    # @login_required
    # def update_user(user_id):
    #     return user.update_user(user_id)
    
    # @app.route('/user/<int:user_id>', methods = ["DELETE"])
    # @login_required
    # def delete_user(user_id):
    #     return user.delete_user(user_id)
