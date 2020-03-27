from .extensions import db, ma

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.String(256))

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Category Schema
class CategorySchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description')

# Init schema
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)