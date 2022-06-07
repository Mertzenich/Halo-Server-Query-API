#!/usr/bin/env python3

from halo_server_query import queryServer
from fastapi import FastAPI

app = FastAPI()

@app.get("/query/{addr}")
def query_server(addr: str, port: int = 2302):
    """Query a halo server at addr:port"""
    query = queryServer(addr, port)
    return query
