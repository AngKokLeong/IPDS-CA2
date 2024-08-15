import pandas


class TransformExcelFileData:

    def transform_local_food_production_annual_data(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:

        if "Data Series" in dataframe.columns:
            for column in dataframe.columns[1:]:
                dataframe.loc[dataframe[column] == 'na', column] = 0
            dataframe = dataframe.set_index("Data Series").transpose().rename(columns=lambda x: x.strip()).reset_index()


        return dataframe


    def transform_electricity_generation_monthly_data(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        if "Data Series" in dataframe.columns:
            return dataframe.rename(columns=lambda x: x.strip()).set_index("Data Series").transpose()
        
        return dataframe
    

    def transform_licensed_local_food_farm_data(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:

        if "Data Series" in dataframe.columns:
            return dataframe.rename(columns=lambda x: x.strip()).set_index("Data Series").transpose().rename(columns=lambda x: x.strip())

        return dataframe

    def transform_electricity_generation_and_consumption_monthly_data(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        if "Data Series" in dataframe.columns:

            dataframe = dataframe.rename(columns=lambda x: x.strip()).set_index("Data Series").transpose()
            # to clear the white space in another columns in dataframe after transpose
            dataframe = dataframe.rename(columns=lambda x: x.strip())

            dataframe = dataframe.replace('na', value=0).astype(int)
            return dataframe.rename(columns={"Data Series": "Year"})

        return dataframe
    
    def transform_electricity_generation_by_month(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        if "Data Series" in dataframe.columns:
            dataframe = dataframe.rename(columns={"Data Series": "Month"})
            dataframe = dataframe.set_index("Month").transpose()
    
            return dataframe
        
        return dataframe
    
    def transform_total_energy_consumption_by_energy_type_and_sector_for_all_products(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        # total_final_energy_consumption_by_energy_type_and_sector_for_total_dataframe
        
        return dataframe.rename(columns=lambda x: x.strip())[["Data Series", "2021", "2020"]].replace('-', value=0)[1:]

 
    def transform_total_energy_consumption_by_energy_type_and_sector_total_for_coal_and_peat(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
       
        
        return dataframe.rename(columns=lambda x: x.strip())[["Data Series", "2021", "2020"]].replace('-', value=0)[1:]


    def transform_total_final_energy_consumption_by_energy_type_and_sector_total_for_electricity(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:

        return dataframe.rename(columns=lambda x: x.strip())[["Data Series", "2021", "2020"]][1:]

    def transform_total_final_energy_consumption_by_energy_type_and_sector_total_for_natural_gas(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
                
        return dataframe.rename(columns=lambda x: x.strip())[["Data Series", "2021", "2020"]][1:]

    def transform_total_final_energy_consumption_by_energy_type_and_sector_for_petroleum_products(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
                
        return dataframe.rename(columns=lambda x: x.strip())[["Data Series", "2021", "2020"]].replace('-', value=0)[1:] 

    def transform_total_final_energy_consumption_by_energy_type_and_sector_for_crude_oil(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
                
        
        return dataframe.rename(columns=lambda x: x.strip())[["Data Series", "2021", "2020"]].replace('-', value=0)[1:] 


class TransformCSVFileData:


    def merge_all_data_of_total_final_energy_consumption_by_energy_type(self, dataframe_list: list[pandas.DataFrame], resulting_dataframe_column: list,dataframe_information: list[str], resulting_dataframe: pandas.DataFrame) -> pandas.DataFrame:
        
        for index in range(len(dataframe_list)):
            energy_product: str = dataframe_information[index]
            for index_inner, row in dataframe_list[index].iterrows():
                for column_index in range(1, len(dataframe_list[index].columns)) :
                    current_year = dataframe_list[index].columns[column_index]
                    sector = row["Data Series"]
                    consumption_ktoe_value = row[current_year]

                    resulting_dataframe.loc[resulting_dataframe.index[-1] + 1] = [current_year, sector, energy_product, consumption_ktoe_value]


        return resulting_dataframe


    