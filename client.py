import requests
import json

service_host = "skinner"
service_port = 14201

tcp_query = {"host": "bart", "port": 80}
print(requests.post(f"http://{service_host}:{service_port}/tcpport/", data=json.dumps(tcp_query)).json())

ping_query = {"host": "bart"}
print(requests.post(f"http://{service_host}:{service_port}/systemping/", data=json.dumps(ping_query)).json())