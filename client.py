import requests
from requests.auth import HTTPBasicAuth
import json

tests = {
    "services":[
        {
            "api":"http://skinner:14201",
            "user":"default",
            "apikey":"insecure",
            "hosts": [
                {
                    "host":"bart",
                    "tests":[
                        {
                            "type":"tcpport",
                            "description":"port 80",
                            "params":{"port":80}
                        },
                        {
                            "type":"tcpport",
                            "description":"default to port 80"
                        },
                        {
                            "type":"tcpport",
                            "description":"closed port",
                            "params":{"port":3}
                        },
                        {
                            "type":"systemping"
                        },
                        {
                            "type":"httpget",
                            "description":"all defaults"
                        },
                        {
                            "type":"httpget",
                            "description":"all defaults",
                            "params": {"path": "/Minecraft/"}
                        },
                        {
                            "type":"httpget",
                            "description":"all defaults",
                            "params": {"path": "/Minecraft/"}
                        },
                        {
                            "type":"httpget",
                            "description":"all defaults",
                            "params": {"port": 8100}
                        }
                    ]
                },
                {
                    "host":"blinky.teeks99.com",
                    "tests":[
                        {
                            "type":"tcpport",
                            "description":"Non-local",
                            "params":{"port":80}
                        },
                        {
                            "type":"systemping",
                            "description":"Non-local"
                        },
                        {
                            "type":"httpget",
                            "description":"Non-local"
                        },
                        {
                            "type":"httpget",
                            "description":"HTTPS",
                            "params": {"protocool":"https"}
                        }
                    ]
                },
                {
                    "host":"10.53.1.1",
                    "tests":[
                        {
                            "type":"tcpport",
                            "description":"IP Only",
                            "params":{"port":80}
                        },
                        {
                            "type":"systemping",
                            "description":"IP Only"
                        },
                        {
                            "type":"httpget",
                            "description":"IP Only"
                        }
                    ]
                },
                {
                    "host":"invalid",
                    "tests":[
                        {
                            "type":"tcpport",
                            "description":"Invalid Host",
                            "params":{"port": 80}
                        },
                        {
                            "type":"systemping",
                            "description":"Invalid Host"
                        },
                        {
                            "type":"httpget",
                            "description":"Invalid Host"
                        }
                    ]
                }
            ]
        },
        {
            "api":"http://jacqueline:14201",
            "user":"default",
            "apikey":"insecure",
            "hosts": [
                {
                    "host":"bart",
                    "tests":[
                        {
                            "type":"tcpport",
                            "description":"Second Service",
                            "params":{"port":80}
                        },
                    ]
                }
            ]
        },
        {
            "api":"http://skinner:14201",
            "user":"unknownuser",
            "apikey":"insecure",
            "hosts": [
                {
                    "host":"bart",
                    "tests":[
                        {
                            "type":"tcpport",
                            "description":"Bad User",
                            "params":{"port":80}
                        }
                    ]
                }
            ]
        },
        {
            "api":"http://skinner:14201",
            "user":"default",
            "apikey":"badpassword",
            "hosts": [
                {
                    "host":"bart",
                    "tests":[
                        {
                            "type":"tcpport",
                            "description":"Bad User",
                            "params":{"port":80}
                        }
                    ]
                }
            ]
        },
        {
            "api":"http://invalid:14201",
            "user":"default",
            "apikey":"insecure",
            "hosts": [
                {
                    "host":"bart",
                    "tests":[
                        {
                            "type":"tcpport",
                            "description":"Invalid Service",
                            "params":{"port":80}
                        }
                    ]
                }
            ]
        }
    ]
}

for service in tests["services"]:
    api = service["api"]
    auth = HTTPBasicAuth(service["user"], service["apikey"])

    for host in service["hosts"]:
        hostname = host["host"]
        for test in host["tests"]:
            query = {"host": hostname}
            if "params" in test:
                query.update(test["params"])
            
            query_json = json.dumps(query)

            start_str = f"{hostname}  {test['type']}"
            if "description" in test:
                start_str += f" - {test['description']}"
            
            print(start_str, end="", flush=True)

            data = json.dumps(query)
            try:
                r = requests.post(f"{api}/{test['type']}/", data=query_json, auth=auth)
                answer = r.json()

                if "error" in answer:
                    print(f"Error: {answer["error"]}")
                else:
                    output = f" - up: {answer['up']}"
                    if "response" in answer:
                        output += f" time: {answer['response']}"
                    print(output)
            except Exception as ex:
                print(f"Error: {ex}")