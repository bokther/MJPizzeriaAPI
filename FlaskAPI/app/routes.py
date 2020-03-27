from flask import Blueprint, request, jsonify

from .extensions import db
from .models import Category, CategorySchema, category_schema, categories_schema

category = Blueprint('category', __name__)

@category.route('/category', methods=['POST'])
def add_category():
    name = request.json['name']
    description = request.json['description']

    new_category = Category(name, description)

    db.session.add(new_category)
    db.session.commit()

    return category_schema.jsonify(new_category)

@category.route('/category/<id>', methods=['GET'])
def get_category(id):
  category = Category.query.get(id)
  return category_schema.jsonify(category)

@category.route('/category', methods=['GET'])
def get_categories():
    all_categories = Category.query.all()
    result = categories_schema.dump(all_categories)
    return jsonify(result)

@category.route('/category/<id>', methods=['PUT'])
def update_category(id):
  category = Category.query.get(id)

  name = request.json['name']
  description = request.json['description']

  category.name = name
  category.description = description

  db.session.commit()

  return category_schema.jsonify(category)

@category.route('/category/<id>', methods=['DELETE'])
def delete_category(id):
  category = Category.query.get(id)
  db.session.delete(category)
  db.session.commit()

  return category_schema.jsonify(category)