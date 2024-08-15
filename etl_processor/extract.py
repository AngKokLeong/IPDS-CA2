import configparser
import pandas

class CSVFileExtract:

    def __init__(self, configparser: configparser.ConfigParser):
        self.configparser_object = configparser
        
    def retrieve_data_for_annual_fuel_mix_for_electricity_generation_by_energy_products(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["AnnualFuelMixforElectricityGenerationbyEnergyProducts2005toJun2021"]
        
        dataframe = pandas.read_csv(file_name, skiprows=1, delimiter=",")

        return dataframe

    def retrieve_data_for_annual_motor_vehicle_population_by_type_of_fuel_used(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["AnnualMotorVehiclePopulationbyTypeofFuelUsed"]
        
        dataframe = pandas.read_csv(file_name, skiprows=1, delimiter=",")

        return dataframe
    
    def retrieve_data_for_average_annual_kilometres_travelled_per_vehicle(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["AverageAnnualKilometresTravelledPerVehicle"]
        
        dataframe = pandas.read_csv(file_name, skiprows=1, delimiter=",")

        return dataframe

    def retrieve_data_for_peak_system_demand_2005_to_jul_2021(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["PeakSystemDemand2005toJul2021"]
        
        dataframe = pandas.read_csv(file_name, skiprows=0, delimiter=",")

        return dataframe

    def retrieve_data_for_solar_pv_installations_by_ura_planning_region(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["SolarPVInstallationsbyURAPlanningRegion"]
        
        dataframe = pandas.read_csv(file_name, skiprows=0, delimiter=",")

        return dataframe

    def retrieve_data_for_total_final_energy_consumption_2009_to_2019(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["TotalFinalEnergyConsumption2009to2019"]
        
        dataframe = pandas.read_csv(file_name, skiprows=0, delimiter=",")

        return dataframe


    def retrieve_data_for_value_of_local_food_production_in_singapore(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["ValueOfLocalFoodProductionInSingapore"]
        
        dataframe = pandas.read_csv(file_name, skiprows=1, delimiter=",")

        return dataframe

class ExcelFileExtract:

    def __init__(self, configparser: configparser.ConfigParser):
        self.configparser_object = configparser

    def retrieve_data_for_local_production_annual(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["LocalProductionAnnual"]
        
        dataframe = pandas.read_excel(file_name, header=30, nrows=12)

        return dataframe

    def retrieve_data_for_total_final_energy_consumption_by_energy_type_and_sector_for_total(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["TotalFinalEnergyConsumptionByEnergyTypeAndSector"]
        
        dataframe = pandas.read_excel(file_name, header=26, nrows=7)

        return dataframe


    def retrieve_data_for_total_final_energy_consumption_by_energy_type_and_sector_for_petroleum_products(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["TotalFinalEnergyConsumptionByEnergyTypeAndSector"]
        
        dataframe = pandas.read_excel(file_name, header=91, nrows=7)

        return dataframe
    
    def retrieve_data_for_total_final_energy_consumption_by_energy_type_and_sector_total_for_coal_and_peat(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["TotalFinalEnergyConsumptionByEnergyTypeAndSector"]
        
        dataframe = pandas.read_excel(file_name, header=100, nrows=7)

        return dataframe

    def retrieve_data_for_total_final_energy_consumption_by_energy_type_and_sector_total_for_crude_oil(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["TotalFinalEnergyConsumptionByEnergyTypeAndSector"]
        
        dataframe = pandas.read_excel(file_name, header=78, nrows=7)

        return dataframe    

    
    def retrieve_data_for_total_final_energy_consumption_by_energy_type_and_sector_total_for_electricity(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["TotalFinalEnergyConsumptionByEnergyTypeAndSector"]
        
        dataframe = pandas.read_excel(file_name, header=114, nrows=7)

        return dataframe

    def retrieve_data_for_total_final_energy_consumption_by_energy_type_and_sector_total_for_natural_gas(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["TotalFinalEnergyConsumptionByEnergyTypeAndSector"]
        
        dataframe = pandas.read_excel(file_name, header=124, nrows=7)

        return dataframe


    def retrieve_data_for_licensed_local_food_farm(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["LicensedLocalFoodFarm"]
        
        dataframe = pandas.read_excel(file_name, header=37, nrows=7)

        return dataframe

    def retrieve_data_for_electricity_generation_and_consumption(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["ElectricityGenerationAndConsumption"]
        
        dataframe = pandas.read_excel(file_name, header=33, nrows=19)

        return dataframe
    
    def retrieve_data_for_electricity_generation_monthly_data(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["ElectricityGenerationMonthlyData"]
        
        dataframe = pandas.read_excel(file_name, header=28, nrows=2)

        return dataframe
    
    def retrieve_data_for_household_electricity_consumption_by_dwelling_type(self) -> pandas.DataFrame:
        file_name = self.configparser_object["DATA_SOURCE"]["SingaporeEnergyStatistics"]

        dataframe = pandas.read_excel(file_name, sheet_name="T3.4", header=0, nrows=2411)

        return dataframe