from fastapi import FastAPI
from pydantic import BaseModel

import socket
import time
import subprocess
import platform
import re
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"unused": "This part of the API is unused"}


class IpQuery(BaseModel):
    host: str
    port: int | None = 80


@app.post("/tcpport/")
async def tcp_port(query: IpQuery):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            start = time.perf_counter()
            s.connect((query.host, query.port))
            end = time.perf_counter()
            return {"up": True, "response": end - start}
    except:
        return {"up": False}


class PingQuery(BaseModel):
    host: str


@app.post("/systemping/")
async def system_ping(query: PingQuery):
    os_name = platform.system()

    if os_name == "Windows":
        ping_cmd = ["ping", "-n", "1", query.host]
        latency_pattern = re.compile(r"Average = (\d+)ms")
    else:
        ping_cmd = ["ping", "-c", "1", query.host]
        latency_pattern = re.compile(r"time=(\d+\.?\d*) ms") #Handles both integers and decimal numbers

    try:
        result = subprocess.run(ping_cmd, capture_output=True, text=True, check=True)
        output = result.stdout
        match = latency_pattern.search(output)
        if not match:
            raise Exception(f"Could not find ping result in output: {output}")

        value_sec = 0
        latency_str = match.group(1)
        value_sec = float(latency_str) / 1000.0

        return {"up": True, "response":value_sec}

    except:
        return {"up": False}


class HttpQuery(BaseModel):
    host: str
    protocol: str | None = "http"
    port: int | None = None
    path: str | None = "/"


@app.post("/httpget/")
async def tcp_port(query: HttpQuery):
    try:
        port = ""
        if query.port:
            port = f":{query.port}"

        start = time.perf_counter()
        r = requests.get(f"{query.protocol}://{query.host}{port}{query.path}")
        end = time.perf_counter()

        if r.status_code != requests.codes.ok:
            raise Exception(f"Bad status code returned: {r.status_code}")

        return {"up": True, "response": end-start}
    except:
        return {"up": False}