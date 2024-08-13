import configparser
import os
from database import database_connection, document_schema, extract


file_path: str = os.path.abspath("database")

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

config.read(file_path + '/configuration/db-configuration.txt')

mongodb_test_cluster = database_connection.MongoDBTestCluster(config)
mongodb_document_schema = document_schema
mongodb_extract = extract
