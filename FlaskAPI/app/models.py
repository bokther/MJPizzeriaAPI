from .extensions import db, ma

# __all__ = ['Category', 'CategorySchema', 'category_schema', 'categories_schema',
#            'Size', 'SizeSchema', 'size_schema', 'sizes_schema',
#            'Item', 'ItemSchema', 'item_schema', 'items_schema']

# Category
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.String(256))

    def __init__(self, name, description):
        self.name = name
        self.description = description

class CategorySchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description')

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

#Size
class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.String(256))

    def __init__(self, name, description):
        self.name = name
        self.description = description

class SizeSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description')

size_schema = CategorySchema()
sizes_schema = CategorySchema(many=True)

#Item
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.String(256))
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'), nullable='True')
    price = db.Column(db.Integer)

    category = db.relationship('Category', backref='items')
    size = db.relationship('Size', backref='items')

    def __init__(self, category_id, name, description, price, size_id=None):
      self.category_id = category_id
      self.name = name
      self.description = description
      self.size_id = size_id
      self.price = price


class ItemSchema(ma.Schema):
  class Meta:
    fields = ('id', 'category_id', 'name', 'description', 'size_id', 'price')

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

# Extra
class Extra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.String(256))
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'), nullable='True')
    price = db.Column(db.Integer)

    category = db.relationship('Category', backref='extras')
    size = db.relationship('Size', backref='extras')

    def __init__(self, category_id, name, description, price, size_id=None):
      self.category_id = category_id
      self.name = name
      self.description = description
      self.size_id = size_id
      self.price = price


class ExtraSchema(ma.Schema):
  class Meta:
    fields = ('id', 'category_id', 'name', 'description', 'size_id', 'price')

extra_schema = ExtraSchema()
extras_schema = ExtraSchema(many=True)