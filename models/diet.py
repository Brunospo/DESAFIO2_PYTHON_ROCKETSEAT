from app import db

class Diet(db.Model):
  __tablename__ = 'diets'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.Text)
  date_hour = db.Column(db.DateTime)
  is_it_on_the_diet = db.Column(db.Boolean, default=False)

  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def to_dict(self):
    return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "date_hour": self.date_hour.strftime("%d/%m/%Y %H:%M") if self.date_hour else None,
        "is_it_on_the_diet": self.is_it_on_the_diet,
        "user_id": self.user_id
    }