import requests
from requests.auth import HTTPBasicAuth
import json

service_host = "skinner"
service_port = 14201
api = f"http://{service_host}:{service_port}"

basic_auth = HTTPBasicAuth('default', 'insecure')

print("No Auth")
tcp_query = {"host": "bart", "port": 80}
print(requests.post(f"{api}/tcpport/", data=json.dumps(tcp_query)).json())

print("TCP on port 80")
tcp_query = {"host": "bart", "port": 80}
print(requests.post(f"{api}/tcpport/", data=json.dumps(tcp_query), auth=basic_auth).json())

print("TCP, defaults to port 80")
tcp_query = {"host": "bart"}
print(requests.post(f"{api}/tcpport/", data=json.dumps(tcp_query), auth=basic_auth).json())

print("TCP non-local")
tcp_query = {"host": "blinky.teeks99.com", "port": 80}
print(requests.post(f"{api}/tcpport/", data=json.dumps(tcp_query), auth=basic_auth).json())

print("TCP only IP")
tcp_query = {"host": "10.53.1.1", "port": 80}
print(requests.post(f"{api}/tcpport/", data=json.dumps(tcp_query), auth=basic_auth).json())

print("TCP invalid host")
tcp_query = {"host": "invalid", "port": 80}
print(requests.post(f"{api}/tcpport/", data=json.dumps(tcp_query), auth=basic_auth).json())

print("TCP closed port")
tcp_query = {"host": "bart", "port": 3}
print(requests.post(f"{api}/tcpport/", data=json.dumps(tcp_query), auth=basic_auth).json())



print("System Ping")
ping_query = {"host": "bart"}
print(requests.post(f"{api}/systemping/", data=json.dumps(ping_query), auth=basic_auth).json())

print("System Ping, invalid host")
ping_query = {"host": "invalid"}
print(requests.post(f"{api}/systemping/", data=json.dumps(ping_query), auth=basic_auth).json())



print("HTTP, all defaults")
http_query = {"host": "bart"}
print(requests.post(f"{api}/httpget/", data=json.dumps(http_query), auth=basic_auth).json())

print("HTTP, path")
http_query = {"host": "bart", "path": "/Minecraft/"}
print(requests.post(f"{api}/httpget/", data=json.dumps(http_query), auth=basic_auth).json())

print("HTTP, port")
http_query = {"host": "bart", "port": 8100}
print(requests.post(f"{api}/httpget/", data=json.dumps(http_query), auth=basic_auth).json())

print("HTTP, https")
http_query = {"host": "blinky.teeks99.com", "protocool":"https"}
print(requests.post(f"{api}/httpget/", data=json.dumps(http_query), auth=basic_auth).json())
