from flask import request, jsonify
from models import Meal
from flask_login import current_user
from app import db
from datetime import datetime

class MealController:
  def _get_meal_data(self):
    """Função privada para extrair e validar dados do request."""
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    date_hour = data.get('date_hour')
    is_it_on_the_diet = data.get('is_it_on_the_diet')

    if not name:
      return None, None, None, None, "O nome da refeição não pode ser vazio."

    try:
      converted_date = datetime.strptime(date_hour, "%d/%m/%Y %H:%M")
    except (ValueError, TypeError):
      return None, None, None, None, "Formato de data e hora inválido. Use 'dd/mm/yyyy HH:MM'."

    return name, description, converted_date, is_it_on_the_diet, None

  def register_meal(self):
    name, description, converted_date, is_it_on_the_diet, error = self._get_meal_data()
      
    if error:
      return jsonify({"message": error}), 400

    try:
      new_meal = Meal(
        name=name,
        description=description,
        date_hour=converted_date,
        is_it_on_the_diet=is_it_on_the_diet,
        user_id=current_user.id
      )
      db.session.add(new_meal)
      db.session.commit()
      return jsonify({"message": "Refeição adicionada com sucesso!"}), 201
    except Exception:
      return jsonify({"erro": "Ocorreu um erro ao salvar a refeição."}), 500

  def list_meals(self):
    meals = [meal.to_dict() for meal in current_user.meals]
    return jsonify({"meals": meals})

  def update_meal(self, meal_id):
    meal = next((m for m in current_user.meals if m.id == int(meal_id)), None)

    if not meal:
      return jsonify({"message": "Refeição não encontrada"}), 404
    
    name, description, converted_date, is_it_on_the_diet, error = self._get_meal_data()
    
    if error:
      return jsonify({"message": error}), 400

    try:
      meal.name = name
      meal.description = description
      meal.date_hour = converted_date
      meal.is_it_on_the_diet = is_it_on_the_diet
      db.session.commit()
      return jsonify({"message": "Refeição atualizada com sucesso!"}), 200
    except Exception:
      return jsonify({"erro": "Ocorreu um erro ao atualizar a refeição."}), 500
    
  def delete_meal(self, meal_id):
    meal = next((m for m in current_user.meals if m.id == int(meal_id)), None)

    if not meal:
      return jsonify({"message": "Refeição não encontrada"}), 404
    
    try:
      db.session.delete(meal)
      db.session.commit()
      return jsonify({"message": "Refeição deletada com sucesso!"}), 200
    except Exception:
      return jsonify({"erro": "Ocorreu um erro ao deletar a refeição."}), 500