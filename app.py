from deeppavlov import configs
from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
from whatsapp_api_client_python import API


from flask import Flask
import kagglehub

# Download latest version


app = Flask("public-health")
greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/v1/health")
def health():
    
    return {"status": "ok"}


