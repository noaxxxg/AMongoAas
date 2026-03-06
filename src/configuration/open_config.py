import json


def open_config(path):
    with open(path, 'r', encoding="utf-8") as file:
        content = json.load(file)
        return content


values = open_config("C:\\Users\\Noago\\AMongoAas\\src\\configuration\\config.json")
HOST = values["host"]
PORT = values["port"]
POSTGRES_URL = values["postgres_url"]
MONGO_URL = values["mongo_url"]
