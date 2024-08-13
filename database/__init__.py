import configparser
import os
import db_manager.database_connection

file_path: str = os.path.abspath("db_manager")

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

config.read(file_path + '/configuration/db-configuration.txt')

mongodb_test_cluster = db_manager.database_connection.MongoDBTestCluster(config)
