from flask import request, jsonify
from models import Diet
from flask_login import current_user
from app import db
from datetime import datetime

class DietController:
  def _get_diet_data(self):
    """Função privada para extrair e validar dados do request."""
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    date_hour = data.get('date_hour')
    is_it_on_the_diet = data.get('is_it_on_the_diet')

    if not name:
      return None, None, None, None, "O nome da dieta não pode ser vazio."

    try:
      converted_date = datetime.strptime(date_hour, "%d/%m/%Y %H:%M")
    except (ValueError, TypeError):
      return None, None, None, None, "Formato de data e hora inválido. Use 'dd/mm/yyyy HH:MM'."

    return name, description, converted_date, is_it_on_the_diet, None

  def register_diet(self):
    name, description, converted_date, is_it_on_the_diet, error = self._get_diet_data()
      
    if error:
      return jsonify({"message": error}), 400

    try:
      new_diet = Diet(
        name=name,
        description=description,
        date_hour=converted_date,
        is_it_on_the_diet=is_it_on_the_diet,
        user_id=current_user.id
      )
      db.session.add(new_diet)
      db.session.commit()
      return jsonify({"message": "Dieta criada com sucesso!"}), 201
    except Exception:
      return jsonify({"erro": "Ocorreu um erro ao salvar a dieta."}), 500

  def list_diets(self):
    diets = [diet.to_dict() for diet in current_user.diets]
    return jsonify({"diets": diets})

  def update_diet(self, diet_id):
    diet = next((d for d in current_user.diets if d.id == int(diet_id)), None)

    if not diet:
      return jsonify({"message": "Dieta não encontrada"}), 404
    
    name, description, converted_date, is_it_on_the_diet, error = self._get_diet_data()
    
    if error:
      return jsonify({"message": error}), 400

    try:
      diet.name = name
      diet.description = description
      diet.date_hour = converted_date
      diet.is_it_on_the_diet = is_it_on_the_diet
      db.session.commit()
      return jsonify({"message": "Dieta atualizada com sucesso!"}), 200
    except Exception:
      return jsonify({"erro": "Ocorreu um erro ao atualizar a dieta."}), 500