from flask import Flask, render_template

app = Flask(__name__)

class Media:
    def __init__(self, title, type, genre, description, director, country, releaseYear, rating, duration, seasons, dateAdded):
        self.title = title
        self.type = type
        self.genre = genre
        self.description = description
        self.director = director
        self.country = country
        self.releaseYear = releaseYear
        self.rating = rating
        self.duration = duration
        self.seasons = seasons
        self.dateAdded = dateAdded

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/insert')
def insert():  # put application's code here
    return render_template("insert.html")

@app.route('/delete')
def delete():  # put application's code here
    return render_template("delete.html")

@app.route('/modify')
def modify():  # put application's code here
    return render_template("modify.html")

@app.route('/search')
def search():  # put application's code here
    return render_template("search.html")

@app.route('/view')
def view():
    # put application's code here

    medias = [
        Media("Movie Title", "movie", "Action", "A thrilling action movie.", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie Title", "movie", "Action", "A thrilling action movie.", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie Title", "movie", "Action", "A thrilling action movie.", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie Title", "movie", "Action", "A thrilling action movie.", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie Title", "movie", "Action", "A thrilling action movie.", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title", "tvseries", "Drama", "A captivating drama series.", "Jane Smith", "UK", 2022, 9.2, 0,
              5, "2023-08-31")
    ]

    return render_template("view.html", medias=medias)


if __name__ == '__main__':
    app.run()
