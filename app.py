from crypt import methods
from peewee import *
from flask import Flask, request, jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('water_bottles', user='nasimakbor', password='12345',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Bottles(BaseModel):
    name = CharField()
    size = IntegerField()
    unit = CharField()
    sparkling = BooleanField()
    mineral_Count = IntegerField()

# class Companies(BaseModel):
#     name = CharField()


db.drop_tables([Bottles])
db.create_tables([Bottles])

Bottles(name="San Pelligrino", size=1, unit="L",
        sparkling=True, mineral_Count=1057).save()
Bottles(name="Fiji", size=500, unit="mL",
        sparkling=False, mineral_Count=193).save()
Bottles(name="Evian", size=330, unit="mL",
        sparkling=False, mineral_Count=485).save()
Bottles(name="VOSS", size=375, unit="mL",
        sparkling=True, mineral_Count=49).save()
Bottles(name="Ty Nant", size=330, unit="mL",
        sparkling=False, mineral_Count=75).save()
Bottles(name="Poland Springs", size=17, unit="oz",
        sparkling=False, mineral_Count=31).save()
Bottles(name="Perrier", size=17, unit="oz",
        sparkling=False, mineral_Count=36).save()
Bottles(name="Aquila", size=330, unit="mL",
        sparkling=False, mineral_Count=119).save()
Bottles(name="Calistoga", size=12, unit="oz",
        sparkling=True, mineral_Count=418).save()
Bottles(name="San Benedetto", size=17, unit="oz",
        sparkling=False, mineral_Count=404).save()
Bottles(name="Ferrarelle", size=500, unit="mL",
        sparkling=True, mineral_Count=510).save()
Bottles(name="Badoit", size=24, unit="oz",
        sparkling=True, mineral_Count=533).save()
Bottles(name="Gerolsteiner", size=750, unit="mL",
        sparkling=False, mineral_Count=665).save()

app = Flask(__name__)


@app.route('/')
def index():
    return "This is the API root, type /bottles to see the list of bottles"


@app.route('/bottles/', methods=['GET', 'POST'])
@app.route('/bottles/<name>', methods=['GET', 'PUT', 'DELETE'])
def bottles(name=None):
    if request.method == 'GET':
        if name:
            return jsonify(model_to_dict(Bottles.get(Bottles.name == name)))
        else:
            bottlesList = []
            for bottle in Bottles.select():
                bottlesList.append(model_to_dict(bottle))
            return jsonify(bottlesList)
    if request.method == 'POST':
        new_bottle = dict_to_model(Bottles, request.get_json())
        new_bottle.save()
        return jsonify({"success": f'{new_bottle.name} created'})
    if request.method == 'DELETE':
        if Bottles.name == name:
            deleted = Bottles.delete().where(Bottles.name == name)
            deleted.execute()
            return jsonify({"deleted": "Something definitely got deleted."})
        else:
            return jsonify({"deleted": "Could not find"})


app.run(port=9000, debug=True)
