from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.client import KeeperState
from kazoo.exceptions import NodeExistsError, NoNodeError, ConnectionLossException
from json import load
import requests
import json
import config as config

# Zookeeper Service Registry
class ZookeeperHandler:
    def registerAuthService(self,port):
        zk = KazooClient(hosts= config.ZK, read_only=True)
        zk.start()
        path = '/Blue'
        host= str(requests.get('https://ip.42.pl/raw').text)
        pass_data=json.dumps({"host":host, "port":port}).encode('utf-8')
        try:
            zk.create(path,value=pass_data, ephemeral=True, sequence=True, makepath=True)
            print("Blue Service is running '"+path+"' here.")
        except NodeExistsError:
            print("Node already exists in Zookeeper")