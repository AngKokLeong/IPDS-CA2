import pandas
import database.database_connection
import database.document_schema

class MasterDataLoading:
    
    def __init__(self):
        database.mongodb_test_cluster.connect_to_mongodb_test_cluster()

    def __del__(self):
        database.mongodb_test_cluster.disconnect_from_mongodb_test_cluster()

class ElectricityGenerationAndConsumptionByMonth(MasterDataLoading):

    def __init__(self, dataframe: pandas.DataFrame):
        super().__init__()
        self.dataframe_to_load: pandas.DataFrame = dataframe
        self.__processDataFrame()
        
    
    def __processDataFrame(self):

        for index, row in self.dataframe_to_load.iterrows():
            self.electricity_generation_and_consumption_by_month_data_document = database.document_schema.ElectricityGenerationAndConsumptionByMonth()
            self.electricity_generation_and_consumption_by_month_data_document.year = index
            self.electricity_generation_and_consumption_by_month_data_document.electricity_generation = float(row["Electricity Generation"])
            self.electricity_generation_and_consumption_by_month_data_document.industrial_related = float(row["Industrial-Related"])
            self.electricity_generation_and_consumption_by_month_data_document.manufacturing = float(row["Manufacturing"])
            self.electricity_generation_and_consumption_by_month_data_document.construction = float(row["Construction"])
            self.electricity_generation_and_consumption_by_month_data_document.utilities = float(row["Utilities"])
            self.electricity_generation_and_consumption_by_month_data_document.other_industrial_related = float(row["Other Industrial-Related"])
            self.electricity_generation_and_consumption_by_month_data_document.commerce_and_service_related = float(row["Commerce And Service-Related"])
            self.electricity_generation_and_consumption_by_month_data_document.wholesale_and_retail_trade = float(row["Wholesale And Retail Trade"])
            self.electricity_generation_and_consumption_by_month_data_document.accommodation_and_food_services = float(row["Accommodation And Food Services"])
            self.electricity_generation_and_consumption_by_month_data_document.information_and_communications = float(row["Information And Communications"])
            self.electricity_generation_and_consumption_by_month_data_document.financial_and_insurance_activities = float(row["Financial And Insurance Activities"])
            self.electricity_generation_and_consumption_by_month_data_document.real_estate_activities = float(row["Real Estate Activities"])
            self.electricity_generation_and_consumption_by_month_data_document.professional_scientific_and_technical_administration_and_support_activities = float(row["Professional, Scientific & Technical, Administration & Support Activities"])
            self.electricity_generation_and_consumption_by_month_data_document.other_commerce_and_service_related = float(row["Other Commerce And Service-Related"])
            self.electricity_generation_and_consumption_by_month_data_document.transport_related = float(row["Transport-Related"])
            self.electricity_generation_and_consumption_by_month_data_document.households = float(row["Households"])
            self.electricity_generation_and_consumption_by_month_data_document.others = float(row["Others"])
            self.electricity_generation_and_consumption_by_month_data_document.cascade_save()

class ElectricityGenerationByMonth(MasterDataLoading):

    def __init__(self, dataframe: pandas.DataFrame):
        super().__init__()
        self.dataframe_to_load: pandas.DataFrame = dataframe
        self.__processDataFrame()
        
    def __processDataFrame(self) -> None:

        for index, row in self.dataframe_to_load.iterrows():
            self.electricity_generation_month_data_document = database.document_schema.ElectricityGenerationMonthlyData()
            self.electricity_generation_month_data_document.month = index
            self.electricity_generation_month_data_document.electricity_generation = float(row["Electricity Generation"])
            self.electricity_generation_month_data_document.cascade_save()


class LicensedLocalFoodFarm(MasterDataLoading):

    def __init__(self, dataframe: pandas.DataFrame):
        super().__init__()
        self.dataframe_to_load: pandas.DataFrame = dataframe
        self.__processDataFrame()
        
    def __processDataFrame(self) -> None:

        for index, row in self.dataframe_to_load.iterrows():
            self.licensed_local_food_farm_document = database.document_schema.LicensedLocalFoodFarm()
            self.licensed_local_food_farm_document.month = index
            self.licensed_local_food_farm_document.number_of_licensed_local_food_farms = int(row["Number Of Licensed Local Food Farms"])
            self.licensed_local_food_farm_document.sea_based_seafood  = int(row["Sea-Based Seafood"])
            self.licensed_local_food_farm_document.land_based_seafood = int(row["Land-Based Seafood"])
            self.licensed_local_food_farm_document.vegetables = int(row["Vegetables"])
            self.licensed_local_food_farm_document.hen_shell_eggs = int(row["Hen Shell Eggs"])
            self.licensed_local_food_farm_document.others = int(row["Others"])
            self.licensed_local_food_farm_document.cascade_save()




'''

Total Value Of Local Production (Million Dollars)',
       'Seafood (Million Dollars)', 'Vegetables (Million Dollars)',
       'Hen Shell Eggs (Million Dollars)',
       'Local Production Of Seafood (Tonnes)',
       'Local Production Of Vegetables (Tonnes)',
       'Local Production Of Hen Shell Eggs (Million Pieces)',
       'Local Production Of Aquarium Fish (Million Pieces)',
       'Local Production Of Aquatic Plants And Tissue Culture Plantlets (Million Plants)',
       'Local Production Of Orchids (Million Stalks)',
       'Local Production Of Ornamental Plants (Million Plants)'

'''