
from mongoengine import Document, StringField, IntField, DecimalField


class ElectricityGenerationMonthlyData(Document):

    year: IntField = IntField(required=True, unique=True)
    electricity_generation = DecimalField(min_value=0)
    electricity_consumption = DecimalField(min_value=0)
    industrial_related = = DecimalField(min_value=0)
    manufacturing = DecimalField(min_value=0)
    construction = DecimalField(min_value=0)
    utilities = DecimalField(min_value=0)
    other_industrial_related = DecimalField(min_value=0)
    commerce_and_service_related = DecimalField(min_value=0)
    wholesale_and_retail_trade = DecimalField(min_value=0)
    accommodation_and_food_services = DecimalField(min_value=0)
    information_and_communications = DecimalField(min_value=0)
    financial_and_insurance_activities = DecimalField(min_value=0)
    real_estate_activities = DecimalField(min_value=0)
    professional = DecimalField(min_value=0)
    scientific_and_technical = DecimalField(min_value=0)
    administration_and_support_activities = DecimalField(min_value=0)
    other_commerce_and_service_related = DecimalField(min_value=0)
    transport_related = DecimalField(min_value=0)
    households = DecimalField(min_value=0)
    others = DecimalField(min_value=0)

