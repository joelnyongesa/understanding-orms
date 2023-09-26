#!usr/bin/env python

import sqlite3

CONNECT = sqlite3.connect("cars.db")
CURSOR = CONNECT.cursor()

class Car:
    all_cars = []
    def __init__(self, model, y_o_m):
        self.model = model
        self.year_of_manufacture = y_o_m
        Car.add_to_all(self)

    @classmethod
    def add_to_all(cls, car):
        cls.all_cars.append(car)

    @classmethod
    def create_table(self):
        sql = """
                CREATE TABLE IF NOT EXISTS cars(
                    id INTEGER PRIMARY KEY,
                    model TEXT,
                    year_of_manufacture INTEGER
                )
            """
        CURSOR.execute(sql)

    def save(self):
        sql = """
                INSERT INTO cars (model, year_of_manufacture)
                VALUES (?, ?)
            """
        
        CURSOR.execute(sql, (self.model, self.year_of_manufacture))

    @classmethod
    def all(cls):
        sql = """SELECT * FROM CARS"""
        all = CURSOR.execute(sql).fetchall()
        print(all)

    @classmethod
    def get_by_id(cls, id):
        sql = """SELECT * FROM cars WHERE id = ? LIMIT 1"""
        car = CURSOR.execute(sql, (id,)).fetchone()
        print(car)


# Car.create_table()
# cx_5 = Car("Mazda CX-5", 2017)
# cx_5.save()
# Car.all()
Car.get_by_id(1)
CONNECT.commit()