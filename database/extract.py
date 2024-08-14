import pandas
import database.database_connection
import database.document_schema
from mongoengine import *

class MasterDataRetrieval:
    
    def __init__(self):
        database.mongodb_test_cluster.connect_to_mongodb_test_cluster()

    def disconnect_from_mongodb_test_cluster(self):
        database.mongodb_test_cluster.disconnect_from_mongodb_test_cluster()

    def display_record_count(self):
        pass

    def retrieve_data(self):
        pass

    def retrieve_data_with_filter(self):
        pass

class ElectricityGenerationAndConsumptionByMonth(MasterDataRetrieval):

    def __init__(self):
        super().__init__()
        self.mongoengine_document_queryset = database.document_schema.ElectricityGenerationAndConsumptionByMonth.objects      

    def display_record_count(self) -> int:
        return len(self.mongoengine_document_queryset)

    def retrieve_data(self) -> str:
        return self.mongoengine_document_queryset.exclude('id')


class ElectricityGenerationMonthlyData(MasterDataRetrieval):

    def __init__(self):
        super().__init__()
        self.mongoengine_document_queryset = database.document_schema.ElectricityGenerationMonthlyData.objects      

    def display_record_count(self) -> int:
        return len(self.mongoengine_document_queryset)

    def retrieve_data(self) -> str:
        return self.mongoengine_document_queryset.exclude('id')


class LicensedLocalFoodFarm(MasterDataRetrieval):

    def __init__(self):
        super().__init__()
        self.mongoengine_document_queryset = database.document_schema.LicensedLocalFoodFarm.objects      

    def display_record_count(self) -> int:
        return len(self.mongoengine_document_queryset)

    def retrieve_data(self) -> str:
        return self.mongoengine_document_queryset.exclude('id')



class LocalFoodProduction(MasterDataRetrieval):

    def __init__(self):
        super().__init__()
        self.mongoengine_document_queryset = database.document_schema.LocalFoodProduction.objects      

    def display_record_count(self) -> int:
        return len(self.mongoengine_document_queryset)

    def retrieve_data(self) -> str:
        return self.mongoengine_document_queryset.exclude('id')



class SolarPVInstallationsByURAPlanningRegion(MasterDataRetrieval):

    def __init__(self):
        super().__init__()
        self.mongoengine_document_queryset = database.document_schema.SolarPVInstallationsByURAPlanningRegion.objects      

    def display_record_count(self) -> int:
        return len(self.mongoengine_document_queryset)

    def retrieve_data(self) -> str:
        return self.mongoengine_document_queryset.exclude('id')



class PeakSystemDemand(MasterDataRetrieval):

    def __init__(self):
        super().__init__()
        self.mongoengine_document_queryset = database.document_schema.PeakSystemDemand.objects      

    def display_record_count(self) -> int:
        return len(self.mongoengine_document_queryset)

    def retrieve_data(self) -> str:
        return self.mongoengine_document_queryset.exclude('id')