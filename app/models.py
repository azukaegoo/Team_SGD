from app import db 

class OneAppButton(db.Model):
    __tablename__ = 'one_app_button'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<OneAppButton {self.id}: {self.value}>"