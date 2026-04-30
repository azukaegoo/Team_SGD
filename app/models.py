from . import db
from datetime import datetime, UTC

class OneAppButton(db.Model):
    __tablename__ = 'one_app_button'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           default=lambda: datetime.now(UTC),
                           nullable=False)

    def __repr__(self):
        return f"<OneAppButton {self.id}: {self.value}>"