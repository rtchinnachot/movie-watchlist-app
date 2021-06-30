import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Watch a movie.
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the Watchlist app!"

def cls_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

print(welcome)

def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    release_timestamp = parsed_date.timestamp()

    database.add_movie(title, release_timestamp)

def view_movies(header, movies):
    print(f"--- {header} ---")
    for count, movie in enumerate(movies, start=1):
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%d %b %Y")
        print(f"{count}. {movie[0]} ({human_date})")
    print('---\n')

def prompt_watched_movie():
    movie_title = input("Enter the movie title you've watched: ")
    database.watch_movie(movie_title)

database.create_tables()    

while (user_input := input(menu)) != "6":
    cls_terminal()
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(upcoming=True)
        view_movies("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies(upcoming=False)
        view_movies("All", movies)
    elif user_input == "4":
        # List All movies
        movies = database.get_movies(upcoming=False)
        view_movies("All", movies)
        # Set watched movie
        prompt_watched_movie()
    elif user_input == "5":
        movies = database.get_watched_movies()
        view_movies("Watched", movies)
    else:
        print("Invalid input, please try again!")
        