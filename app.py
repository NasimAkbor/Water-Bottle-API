from peewee import *

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
