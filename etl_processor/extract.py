import configparser
import pandas

class CSVFileExtract:

    def __init__(self, configparser: configparser.ConfigParser):
        self.configparser_object = configparser
        
    def retrieve_data_for_annual_fuel_mix_for_electricity_generation_by_energy_products(self) -> pandas.DataFrame:
        file_name = self.configparser_object["CSV_FILES"]["AnnualFuelMixforElectricityGenerationbyEnergyProducts2005toJun2021"]
        
        dataframe = pandas.read_csv(file_name, skiprows=1, delimiter=",")

        return dataframe

    def retrieve_data_for_annual_motor_vehicle_population_by_type_of_fuel_used(self) -> pandas.DataFrame:
        file_name = self.configparser_object["CSV_FILES"]["AnnualMotorVehiclePopulationbyTypeofFuelUsed"]
        
        dataframe = pandas.read_csv(file_name, skiprows=1, delimiter=",")

        return dataframe
    
    def retrieve_data_for_average_annual_kilometres_travelled_per_vehicle(self) -> pandas.DataFrame:
        file_name = self.configparser_object["CSV_FILES"]["AverageAnnualKilometresTravelledPerVehicle"]
        
        dataframe = pandas.read_csv(file_name, skiprows=1, delimiter=",")

        return dataframe
    
    def retrieve_data_for_electricity_generation_and_consumption(self) -> pandas.DataFrame:
        file_name = self.configparser_object["CSV_FILES"]["AverageAnnualKilometresTravelledPerVehicle"]
        
        dataframe = pandas.read_excel(file_name, skiprows=1, delimiter=",")

        return dataframe
    