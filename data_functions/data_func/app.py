from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Wall-E.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Class/Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  genres = db.Column(db.String(200))
  

  def __init__(self, name, genres):
    self.name = name
    self.genres = genres
    
   

# Movies Schema
class MoviesSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'genres')

# Init schema
  


# Create 
@app.route('/movie', methods=['POST'])
def add_movie():
  name = request.json['name']
  genres = request.json['genres']
  
  

  new_movie = movie(name, genres)

  db.session.add(new_movie)
  db.session.commit()

  return movie_schema.jsonify(new_movie)

# Get All 
@app.route('/movie', methods=['GET'])
def get_movies():
  all_movies = movie.query.all()
  result = movies_schema.dump(all_movies)
  return jsonify(result.data)

# Get Single 
@app.route('/movie/<id>', methods=['GET'])
def get_movie(id):
  movie = movie.query.get(id)
  return movie_schema.jsonify(movie)

# Update 
@app.route('/movie/<id>', methods=['PUT'])
def update_product(id):
  movie = movie.query.get(id)

  name = request.json['name']
  genres = request.json['genres']
  

  movie.name = name
  movie.genres = genres
  

  db.session.commit()

  return movie_schema.jsonify(movie)

# Delete 
@app.route('/movie/<id>', methods=['DELETE'])
def delete_movie(id):
  movie = movie.query.get(id)
  db.session.delete(movie)
  db.session.commit()

  return movie_schema.jsonify(movie)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)