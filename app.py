from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
import json

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

client = MongoClient("mongodb://localhost:27017/")
db = client['AmazonDB']
amazon_collection = db['medias']


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

    page = request.form.get('page', 0)
    req = {'page': page}
    return view(medias, req)


@app.route('/search')
def search():  # put application's code here
    return render_template("search.html")


@app.route('/execute-search', methods=['GET', 'POST'])
def execute_search():
    page = request.args.get('page', 0, type=int)
    num_query = request.args.get('query', 0, type=int)

    if page == 0:
        num_query = request.form.get("query", type=int)

        if num_query == 1:
            title = request.form.get("title")
        elif num_query == 2:
            type = request.form.get("type")
            genre = request.form.get("genre")
        elif num_query == 3:
            type1 = request.form.get("type1")
            release_year_1 = request.form.get("releaseYear1", type=int)
            type2 = request.form.get("type2")
            release_year_2 = request.form.get("releaseYear2", type=int)
    else:
        if num_query == 1:
            title = request.args.get("title")
        elif num_query == 2:
            type = request.args.get("type")
            genre = request.args.get("genre")
        elif num_query == 3:
            type1 = request.args.get("type1")
            release_year_1 = request.args.get("releaseYear1", type=int)
            type2 = request.args.get("type2")
            release_year_2 = request.args.get("releaseYear2", type=int)
        else:
            num_query = 0

    if num_query == 1:
        return search_title(page, title)
    elif num_query == 2:
        return search_type_genre(page, type, genre)
    elif num_query == 3:
        return search_type_release(page, type1, release_year_1, type2, release_year_2)
    else:
        num_query = 0

    return None


@app.route('/search-title', methods=['GET', 'POST'])
def search_title(page, title):  # put application's code here

    query = {'title': title}
    medias = list(amazon_collection.find(query))

    parameters = {
        'title': title
    }

    return view(medias, page, parameters, query=1)


@app.route('/search-type-genre', methods=['GET', 'POST'])
def search_type_genre(page, type, genre):  # put application's code here

    query = {
        '$and': [
            {'type': type},
            {'genre': {'$regex': genre, '$options': 'i'}}
        ]
    }

    parameters = {
        'type': type,
        'genre': genre,
    }

    medias = list(amazon_collection.find(query))

    return view(medias, page, parameters, query=2)


@app.route('/search-type-release-year', methods=['GET', 'POST'])
def search_type_release(page, type1, release_year_1, type2, release_year_2):  # put application's code here

    query = {
        '$or':
            [
                {'$and':
                    [
                        {'type': type1}, {'release_year': release_year_1}
                    ]
                },
                {'$and':
                    [
                        {'type': type2}, {'release_year': release_year_2}
                    ]
                },
            ]
    }

    medias = list(amazon_collection.find(query))

    parameters = {
        'type1': type1,
        'releaseYear1': release_year_1,
        'type2': type2,
        'releaseYear2': release_year_2
    }

    return view(medias, page, parameters, query=3)


@app.route('/view')
def view(medias=None, page=1, parameters=None, query=0):
    if page == 0:
        page = 1

    # Number of items per page
    per_page = 3  # Adjust this as needed

    # Calculate the index range for the current page
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    # Slice the data to display only items for the current page
    medias_on_page = medias[start_idx:end_idx]

    # Calculate the total number of pages
    total_pages = len(medias) // per_page + (len(medias) % per_page > 0)

    return render_template('search-view.html', medias=medias_on_page, page=page, total_pages=total_pages,
                           parameters=parameters, query=query)


if __name__ == '__main__':
    app.run()
