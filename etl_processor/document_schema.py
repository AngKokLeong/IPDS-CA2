
from mongoengine import *

class AnnualMotorVehiclePopulationByTypeOfFuelUsedDocument(Document):

    year = StringField(max_length=4, required=True)
    type = StringField(max_length=30, required=True)
    engine = StringField(max_length=30, required=True)
    number_of_vehicle = IntField(min_value=0)


    