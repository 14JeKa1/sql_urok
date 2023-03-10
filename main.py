from flask import Flask, jsonify
from utils import get_one, get_all

app = Flask(__name__)

@app.get('/movie/<title>')
def get_by_title(title: str):
    query = f"""
      SELECT * FROM netflix
      WHERE title = {title}
      ORDER BY date.addet desc
    """

    query_result = get_one(query)

    if query_result is None:
        return jsonify(status=404)

    movie = {
		"title": query_result['title'],
		"country": query_result['country'],
		"release_year": query_result['release_year'],
		"genre": query_result['listed_in'],
		"description": query_result['description'],
    }

    return jsonify(movie)

@app.get('/movie/<year1>/to/<year2>')
def get_movie_date(year1: str, year2: str):
    query = f"""
          SELECT * FROM netflix
          WHERE release_year BETWEEN {year1} and {year2}
          limit 100;
        """

    result = []

    for item in get_all(query):
        result.append(
            {
                'title': item['title'],
                'release_year': item['release_year'],
            }
        )
    return jsonify(result)

@app.get('movie/rating/<value>')
def get_movie_by_rating(value: str):
    query = """
              SELECT * FROM netflix
            """

    if value == 'children':
        query += "WHERE rating = 'G'"

    elif value == 'famili':
        query += "WHERE rating = 'PG', or rating = 'PG-13'"

    elif value == 'abult':
        query += "WHERE rating = 'R' or rating = 'NC-17'"

    else:
        return jsonify(status=404)

    result = []

    for item in get_all(query):
        result.append(
            {
                'title': item['title'],
                'rating': item['rating'],
                'description': item['description'],
            }
        )
    return jsonify(result)


@app.get('/genre/<genre>')
def get_movie_by_genre(genre: str):
    query = f"""
              SELECT * FROM netflix
              WHERE listed_in LIKE '%{genre}%'
              ORDER BY date_added desc
              limit 10
            """

    result = []

    for item in get_all(query):
        result.append(
            {
                'title': item['title'],
                'description': item['description'],
            }
        )
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)



