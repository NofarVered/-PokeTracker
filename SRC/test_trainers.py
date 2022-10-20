from fastapi.testclient import TestClient
from server import app
from fastapi import status

client = TestClient(app)
