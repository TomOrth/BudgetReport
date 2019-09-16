from app import db


class Base(db.Model):
    """
    Class that is used as a basis for the DB models, giving standard columns amongst them
    """
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

    def as_dict(self):
        """
        Converts the model into a dictionary
        :return: Database model as a dictionary
        :rtype: dict
        """
        return dict((c.name,
                     getattr(self, c.name))
                     for c in self.__table__.columns)
