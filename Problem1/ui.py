#!/usr/bin/env/python3

import db
from objects import Movie


def display_title():
    print("The Movie List program")
    print()
    display_menu()


def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("min  - View movies by minutes")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()


def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()


def display_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        print(line_format.format(str(movie.id), movie.name,
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()


def display_movies_by_category():
    category_id = int(input("Category ID: "))
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())


def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))


def display_movies_by_minutes():
    max_minutes = get_int("Maximum number of minutes: ")
    print()
    movies = db.get_movies_by_minutes(max_minutes)
    display_movies(movies, "LESS THAN " + str(max_minutes) + " MINUTES")


def get_int(prompt):
    while True:
        try:
            return int(float(input(prompt)))
        except ValueError:
            print("Please enter an integer")


def add_movie():
    name = input("Name: ")
    year = int(input("Year: "))
    minutes = int(input("Minutes: "))
    category_id = int(input("Category ID: "))

    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        result = db.add_movie(movie)
        if result:
            print(name + " was added to database.\n")
        else:
            print("This movie already exists in the database.\n")


def delete_movie():
    try:
        movie_id = int(input("Movie ID: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    movie = db.get_movie(movie_id)
    if not movie:
        print(f"Movie ID {movie_id} not found.\n")
        return

    confirm = input(f"Are you sure you want to delete '{movie.name}'? (y/n): ").lower()
    if confirm == 'y':
        db.delete_movie(movie_id)
        print(f"'{movie.name}' was deleted from database.\n")
    else:
        print("Delete canceled.\n")


def main():
    db.connect()
    display_title()
    display_categories()
    commands = {
        "cat": display_movies_by_category,
        "year": display_movies_by_year,
        "min": display_movies_by_minutes,
        "add": add_movie,
        "del": delete_movie
    }

    while True:
        command = input("Command: ").lower()
        if command == "exit":
            break
        elif command in commands:
            commands[command]()
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()

    db.close()
    print("Bye!")


if __name__ == "__main__":
    main()
