from peewee import *

db = SqliteDatabase('exercises.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Muscle(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'muscles'


class Exercise(BaseModel):
    name = CharField()
    info_how = CharField()
    level = CharField()
    expense_id = ForeignKeyField(Muscle)

    class Meta:
        db_table = 'exercises'
