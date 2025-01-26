# status-service
This is a simple python service, to be run on nearly any computer, that can query the network (or internet) for the
status of an exposed host/serivce.

Currently supported are:
*   TCP Port
*   System Ping
*   HTTP Get Request

This uses the python [FastAPI](https://fastapi.tiangolo.com/) library to provide the web framework. It includes the
API documentation for the supported requests in every instance of the service, found in the `/docs` path.


## Authentication Required
Because exposing this on the internet could lead to Denial-of-service attacks against un-related 3rd parties, it is 
required that authentication is enabled to access the service. 

**However**, by default the username is "default" and the api key is "insecure". If this is sufficient for your
environment (i.e. you are *not* connected to the internet), feel free to leave as-is.

If this is ever deployed into an internet connected environment, generate a strong API key (they can be any string you 
link, but it is recommended to generate a long random one) for each user and save it in the `auth_list.json` file. Each 
user may have several API keys registered, such as:

```json
{
    "users":{
        "userwiththreekeys": [
            "Q5xD5uUMXzLhtubcGOTLggFop18LIiia2FKJsybJIVT6XLw4hzyl6njO9DOaeAI",
            "hCCJZIlfjwK3Y2kyUzqkeH7DFloX8GpBY8loh95Dvmt5Kpd20R6D0mboQpXF54y",
            "SkHeqO6DBLYKwnatdIkPaJMRS2mRPTtEB3wSCPz42PbMCAZmOB93XeBYfEZ88w7"
        ],
        "userwithonekey": [
            "rxjwn00W5dAGoXLxPipOH1KjuH6hIzDo0lak64cP5RHry07mWhy4YiuS3IRqeeD"
        ]
    }
}
```
