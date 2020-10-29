import contextlib
import json
from csv import DictReader
import csv


@contextlib.contextmanager
def file_name(name):
    file = open(name, "r", encoding="UTF-8")
    yield file
    file.close()


with file_name("users.json") as f:
    file = json.loads(f.read())
    users_to_json = {}
    for user in file:
        i = 0
        #temp_users = dict({"name": user["name"], "gender": user["gender"], "address": user["address"], "books": []})
        user[i] = file
        i += 1
    users_to_json = user


with file_name('books.csv') as file:
    reader = csv.DictReader(file)
    header = next(reader)
    i = 0
    for row in reader:
        temp_books = dict({"title": row["Title"], "author": row["Author"], "height": row["Height"]})
    print(temp_books)

print(users_to_json)
