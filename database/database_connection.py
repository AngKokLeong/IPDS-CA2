import configparser
from mongoengine import connect, disconnect, register_connection


class MongoDBTestCluster:
    connection_alias: str = "test-cluster"
    
    def __init__(self, configParser: configparser.ConfigParser):
        self.configparser_object: configparser.ConfigParser = configParser
        
        #register_connection(alias=self.connection_alias, host=self.configparser_object["DATABASE"]["mongodb_connection_string"])

        
    def retrieve_connection_alias(self) -> str:
        return self.connection_alias
    
    def connect_to_mongodb_test_cluster(self) -> any:
        return connect(alias=self.connection_alias, db="SG-Green-Plan-Data-Analysis-DB",host=self.configparser_object["DATABASE"]["mongodb_connection_string"])

    
    def disconnect_from_mongodb_test_cluster(self) -> None:
        disconnect(alias=self.connection_alias)


