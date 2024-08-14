import pandas
import database.database_connection
import database.document_schema
from mongoengine import NotUniqueError, Document

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
                try:
                    
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
                    self.electricity_generation_and_consumption_by_month_data_document.save(force_insert=False)
                except (NotUniqueError) as e:
                    print(e)

class ElectricityGenerationByMonth(MasterDataLoading):

    def __init__(self, dataframe: pandas.DataFrame):
        super().__init__()
        self.dataframe_to_load: pandas.DataFrame = dataframe
        self.__processDataFrame()
        
    def __processDataFrame(self) -> None:
        
            for index, row in self.dataframe_to_load.iterrows():
                self.electricity_generation_month_data_document = database.document_schema.ElectricityGenerationMonthlyData()
                try:
                    
                    self.electricity_generation_month_data_document.month = index
                    self.electricity_generation_month_data_document.electricity_generation = float(row["Electricity Generation"])
                    self.electricity_generation_month_data_document.save(force_insert=False)
                except (NotUniqueError) as e:
                    print(e)


class LicensedLocalFoodFarm(MasterDataLoading):

    def __init__(self, dataframe: pandas.DataFrame):
        super().__init__()
        self.dataframe_to_load: pandas.DataFrame = dataframe
        self.__processDataFrame()
        
    def __processDataFrame(self) -> None:
        
            for index, row in self.dataframe_to_load.iterrows():
                self.licensed_local_food_farm_document = database.document_schema.LicensedLocalFoodFarm()
                try:
                    
                    self.licensed_local_food_farm_document.year = index
                    self.licensed_local_food_farm_document.number_of_licensed_local_food_farms = int(row["Number Of Licensed Local Food Farms"])
                    self.licensed_local_food_farm_document.sea_based_seafood  = int(row["Sea-Based Seafood"])
                    self.licensed_local_food_farm_document.land_based_seafood = int(row["Land-Based Seafood"])
                    self.licensed_local_food_farm_document.vegetables = int(row["Vegetables"])
                    self.licensed_local_food_farm_document.hen_shell_eggs = int(row["Hen Shell Eggs"])
                    self.licensed_local_food_farm_document.others = int(row["Others"])
                    self.licensed_local_food_farm_document.save(force_insert=False)
                except (NotUniqueError) as e:
                    print(e)


class LocalFoodProduction(MasterDataLoading):

    def __init__(self, dataframe: pandas.DataFrame):
        super().__init__()
        self.dataframe_to_load: pandas.DataFrame = dataframe
        self.__processDataFrame()
        
    def __processDataFrame(self) -> None:
    
            for index, row in self.dataframe_to_load.iterrows():
                self.local_food_production_document = database.document_schema.LocalFoodProduction()
                try:
                    
                    self.local_food_production_document.year = str(row["index"])
                    self.local_food_production_document.total_value_of_local_production_million_dollars = int(row["Total Value Of Local Production (Million Dollars)"])
                    self.local_food_production_document.seafood_million_dollars  = int(row["Seafood (Million Dollars)"])
                    self.local_food_production_document.vegetable_million_dollars = int(row["Vegetables (Million Dollars)"])
                    self.local_food_production_document.hen_shell_eggs_million_dollars = int(row["Hen Shell Eggs (Million Dollars)"])
                    self.local_food_production_document.local_production_of_seafood_tonnes = int(row["Local Production Of Seafood (Tonnes)"])
                    self.local_food_production_document.local_production_of_vegetables_tonnes = int(row["Local Production Of Vegetables (Tonnes)"])
                    self.local_food_production_document.local_production_of_hen_shell_eggs_million_tonnes = int(row["Local Production Of Hen Shell Eggs (Million Pieces)"])
                    self.local_food_production_document.local_production_of_aquarium_fish_million_pieces = int(row["Local Production Of Aquarium Fish (Million Pieces)"])
                    self.local_food_production_document.local_production_of_aquatic_plants_and_tissue_culture_plantlets_million_plants = int(row["Local Production Of Aquatic Plants And Tissue Culture Plantlets (Million Plants)"])
                    self.local_food_production_document.local_production_of_orchids_million_stalks = int(row["Local Production Of Orchids (Million Stalks)"])
                    self.local_food_production_document.local_production_of_ornamental_plants_million_plants = int(row["Local Production Of Ornamental Plants (Million Plants)"])

                    self.local_food_production_document.save(force_insert=False)
                except (NotUniqueError) as e:
                    print(e)

class SolarPVInstallationsByURAPlanningRegion(MasterDataLoading):

    def __init__(self, dataframe: pandas.DataFrame):
        super().__init__()
        self.dataframe_to_load: pandas.DataFrame = dataframe
        self.__processDataFrame()
        
    def __processDataFrame(self) -> None:
    
            for index, row in self.dataframe_to_load.iterrows():
                self.solar_pv_installations_by_ura_planning_region = database.document_schema.SolarPVInstallationsByURAPlanningRegion()
                try:
                    self.solar_pv_installations_by_ura_planning_region.year = int(row["year"])
                    self.solar_pv_installations_by_ura_planning_region.ura_planning_region = str(row["ura_planning_region"])
                    self.solar_pv_installations_by_ura_planning_region.residential_status  = str(row["residential_status"])
                    self.solar_pv_installations_by_ura_planning_region.num_solar_pv_inst = int(row["num_solar_pv_inst"])
                    self.solar_pv_installations_by_ura_planning_region.inst_cap_kwac = float(row["inst_cap_kwac"])
                    self.solar_pv_installations_by_ura_planning_region.total_inst_cap_percent = float(row["total_inst_cap_percent"])

                    self.solar_pv_installations_by_ura_planning_region.save(force_insert=False)
                except (NotUniqueError) as e:
                    print(e)

