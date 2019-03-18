from ThinkBoard import db

class Engine(db.Model):
    """
        Create an Engine table
    """

    __tablename__ = 'engines'

    # Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    thrust = db.Column(db.Integer, default=0)

    def __init__(self, title, thrust):
        self.title = title
        self.thrust = thrust

    def __repr__(self):
        return '<Engine %r>' % self.title
        #return '<Engine: {}>'.format(self.title)
