from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Media:
    def __init__(self, title, type, genre, description, cast, director, country, releaseYear, rating, duration, seasons,
                 dateAdded):
        self.title = title
        self.type = type
        self.genre = genre
        self.description = description
        self.director = director
        self.country = country
        self.releaseYear = releaseYear
        self.rating = rating
        self.duration = duration
        self.cast = cast
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


@app.route('/show-edit', methods=['GET', 'POST'])
def show_edit():  # put application's code here
    media_data = {
        'title': request.form.get('title', 'ciao'),
        'type': request.form.get('type', ''),
        'genre': request.form.get('genre', ''),
        'description': request.form.get('description', ''),
        'director': request.form.get('director', ''),
        'country': request.form.get('country', ''),
        'releaseYear': request.form.get('releaseYear', ''),
        'rating': request.form.get('rating', ''),
        'duration': request.form.get('duration', ''),
        'dateAdded': request.form.get('dateAdded', '')
    }

    page = request.form.get('page', 0)

    print(request.form)
    return render_template('edit.html', media_data=media_data, page=page)


@app.route('/editMovie', methods=['GET', 'POST'])
def edit():  # put application's code here

    medias = [
        Media("Movie 1", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 2", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 3", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 4", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 5", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 6", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 7", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 8", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 9", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 10", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 2", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 11", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 12", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 13", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 14", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 15", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 3", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 16", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 17", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 18", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 19", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 20", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 4", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 21", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 22", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 23", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 24", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 25", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 5", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31")
    ]
    page = request.form.get('page', 0)
    req = {'page': page}
    return view(medias, req)


@app.route('/search')
def search():  # put application's code here
    return render_template("search.html")


@app.route('/search-title')
def search_title():  # put application's code here
    medias = [
        Media("Movie 1", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 2", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 3", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 4", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 5", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 6", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 7", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 8", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 9", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 10", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 2", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 11", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 12", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 13", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 14", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 15", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 3", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 16", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 17", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 18", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 19", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 20", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 4", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 21", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 22", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 23", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 24", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 25", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 5", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31")
    ]

    req = {'page': 1}
    return view(medias=medias, req=req)


@app.route('/search-type-genre')
def search_type_genre():  # put application's code here
    return render_template("search.html")


@app.route('/search-type-release-year')
def search_type_release():  # put application's code here
    return render_template("search.html")


@app.route('/view')
def view(medias=None, req=None):
    # put application's code here

    medias = [
        Media("Movie 1", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 2", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 3", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 4", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 5", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 6", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 7", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 8", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 9", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 10", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 2", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 11", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 12", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 13", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 14", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 15", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 3", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 16", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 17", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 18", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 19", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 20", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 4", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31"),
        Media("Movie 21", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 22", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 23", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 24", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("Movie 25", "movie", "Action", "A thrilling action movie.", "Cast", "John Doe", "USA", 2023, 8.5, 120, 0,
              "2023-08-31"),
        Media("TV Series Title 5", "tvseries", "Drama", "A captivating drama series.", "Cast", "Jane Smith", "UK", 2022,
              9.2, 0,
              5, "2023-08-31")
    ]

    # Get the current page number from the request's query parameters
    print(request)
    if req is None:
        page = request.args.get('page', type=int, default=1)
    else:
        page = int(req['page'])

    # Number of items per page
    per_page = 3  # Adjust this as needed

    # Calculate the index range for the current page
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    # Slice the data to display only items for the current page
    medias_on_page = medias[start_idx:end_idx]

    # Calculate the total number of pages
    total_pages = len(medias) // per_page + (len(medias) % per_page > 0)

    return render_template('view.html', medias=medias_on_page, page=page, total_pages=total_pages)


if __name__ == '__main__':
    app.run()
