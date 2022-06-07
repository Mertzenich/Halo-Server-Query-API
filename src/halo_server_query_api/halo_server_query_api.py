#!/usr/bin/env python3

from haloserverquery.haloserverquery import queryServer
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/query/{addr}")
def query_server(addr: str, port: int = 2302, attr: str = None):
    """Query a halo server at addr:port"""
    if attr:
        return queryServer(addr, port)[attr]
    return queryServer(addr, port)
