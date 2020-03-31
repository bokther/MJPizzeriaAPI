from flask import Blueprint, request, jsonify

from .extensions import db
from .models import *

api = Blueprint('category', __name__)

# Category Routes
@api.route('/category', methods=['POST'])
def add_category():
    name = request.json['name']
    description = request.json['description']

    new_category = Category(name, description)

    db.session.add(new_category)
    db.session.commit()

    return category_schema.jsonify(new_category)

@api.route('/category/<id>', methods=['GET'])
def get_category(id):
    category = Category.query.get(id)
    return category_schema.jsonify(category)

@api.route('/category', methods=['GET'])
def get_categories():
    all_categories = Category.query.all()
    result = categories_schema.dump(all_categories)
    return jsonify(result)

@api.route('/category/<id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get(id)

    name = request.json['name']
    description = request.json['description']
    
    category.name = name
    category.description = description
    
    db.session.commit()
    
    return category_schema.jsonify(category)

@api.route('/category/<id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)
    db.session.delete(category)
    db.session.commit()
    
    return category_schema.jsonify(category)

# Size Routes
@api.route('/size', methods=['POST'])
def add_size():
    name = request.json['name']
    description = request.json['description']

    new_size = Size(name, description)

    db.session.add(new_size)
    db.session.commit()

    return category_schema.jsonify(new_size)

@api.route('/size/<id>', methods=['GET'])
def get_size(id):
    size = Size.query.get(id)
    return size_schema.jsonify(size)

@api.route('/size', methods=['GET'])
def get_sizes():
    all_sizes = Size.query.all()
    result = sizes_schema.dump(all_sizes)
    return jsonify(result)

@api.route('/size/<id>', methods=['PUT'])
def update_size(id):
    size = Size.query.get(id)

    name = request.json['name']
    description = request.json['description']

    size.name = name
    size.description = description

    db.session.commit()

    return size_schema.jsonify(size)

@api.route('/size/<id>', methods=['DELETE'])
def delete_size(id):
    size = Size.query.get(id)
    db.session.delete(size)
    db.session.commit()

    return size_schema.jsonify(size)

# Item Routes
@api.route('/item', methods=['POST'])
def add_item():
    category_id = request.json['category_id']
    name = request.json['name']
    description = request.json['description']
    size_id = request.json['size_id'] if "size_id" in request.json else None
    price = request.json['price']

    new_item = Item(category_id, name, description, price, size_id=size_id)

    db.session.add(new_item)
    db.session.commit()

    return item_schema.jsonify(new_item)

@api.route('/item/<id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    return item_schema.jsonify(item)

@api.route('/item', methods=['GET'])
def get_items():

    if 'category_id' in request.args:
        items = Item.query.filter_by(category_id=request.args['category_id']).all()
    else:       
        items = Item.query.all()
    result = items_schema.dump(items)
    return jsonify(result)

@api.route('/item/<id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get(id)

    category_id = request.json['category_id']
    name = request.json['name']
    description = request.json['description']
    size_id = request.json['size_id'] if "size_id" in request.json else None
    price = request.json['price']

    item.category_id = category_id
    item.name = name
    item.description = description
    item.size_id = size_id
    item.price = price

    db.session.commit()

    return item_schema.jsonify(item)

@api.route('/item/<id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()

    return item_schema.jsonify(item)

# Extra Routes
@api.route('/extra', methods=['POST'])
def add_extra():
    category_id = request.json['category_id']
    name = request.json['name']
    description = request.json['description']
    size_id = request.json['size_id'] if "size_id" in request.json else None
    price = request.json['price']

    new_extra = Extra(category_id, name, description, price, size_id=size_id)

    db.session.add(new_extra)
    db.session.commit()

    return extra_schema.jsonify(new_extra)

@api.route('/extra/<id>', methods=['GET'])
def get_extra(id):
    extra = Extra.query.get(id)
    return extra_schema.jsonify(extra)

@api.route('/extra', methods=['GET'])
def get_extras():
    all_extras = Extra.query.all()
    result = extras_schema.dump(all_extras)
    return jsonify(result)

@api.route('/extra/<id>', methods=['PUT'])
def update_extra(id):
    extra = Extra.query.get(id)

    category_id = request.json['category_id']
    name = request.json['name']
    description = request.json['description']
    size_id = request.json['size_id'] if "size_id" in request.json else None
    price = request.json['price']

    extra.category_id = category_id
    extra.name = name
    extra.description = description
    extra.size_id = size_id
    extra.price = price

    db.session.commit()

    return extra_schema.jsonify(extra)

@api.route('/extra/<id>', methods=['DELETE'])
def delete_extra(id):
    extra = Extra.query.get(id)
    db.session.delete(extra)
    db.session.commit()

    return extra_schema.jsonify(extra)