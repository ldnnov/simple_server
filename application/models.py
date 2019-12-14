from . import db


class Counter(db.Model):
    __tablename__ = 'counter'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return str(self.value)
