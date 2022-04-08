from flask import Flask, jsonify, request
import csv

allmovies = []
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]

did_not_watch = []
liked_movies = []
disliked_movies = []

app = Flask(__name__)

@app.route('/get-movies')
def getMovies():
    return jsonify({"data": allmovies[0], "status": "success"})

@app.route('/did-not-watch', method = ["POST"])
def didNotWatch():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    did_not_watch.append(movie)
    return jsonify({"status": "success"}), 201

@app.route('/liked-movies', method = ["POST"])
def likedMovies():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    liked_movies.append(movie)
    return jsonify({"status": "success"}), 201

@app.route('/disliked-movies', method = ["POST"])
def disikedMovies():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    disliked_movies.append(movie)
    return jsonify({"status": "success"}), 201