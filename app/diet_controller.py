from flask import request, jsonify
from models import Diet
from flask_login import current_user
from app import db
from datetime import datetime

class DietController:
  def register_diet(self):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    date_hour = data.get('date_hour')
    is_it_on_the_diet = data.get('is_it_on_the_diet')

    try:
      if not name:
        raise ValueError
      
      converted_date = datetime.strptime(date_hour, "%d/%m/%Y %H:%M")

      new_diet = Diet(name=name, description=description, date_hour=converted_date, is_it_on_the_diet=is_it_on_the_diet, user_id=current_user.id)
      db.session.add(new_diet)
      db.session.commit()

      return jsonify({"message": "Dieta criada com sucesso!"}), 201

    except (KeyError, ValueError):
      return jsonify({"erro": "Dados inválidos ou formato de data incorreto"}), 400