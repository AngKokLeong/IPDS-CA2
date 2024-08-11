import configparser
import etl_processor.extract

import os


file_path: str = os.path.abspath(os.path.relpath("etl_processor"))

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

config.read(file_path + '/configuration/csv_file_path_configuration.txt')

config.set("DEFAULT", "module_file_path", file_path)


csv_file_data_source = etl_processor.extract.CSVFileExtract(config)
excel_file_data_source = etl_processor.extract.ExcelFileExtract(config)

