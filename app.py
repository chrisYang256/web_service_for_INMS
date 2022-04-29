import os

from flask  import Flask
from routes import *
from dotenv import load_dotenv



app = Flask(__name__)

app.register_blueprint(snmp_device_api)
app.register_blueprint(snmp_device_view)

load_dotenv(
    dotenv_path = ".env",
    override    = False,
    verbose     = True
)

if __name__=="__main__":
    app.run(
        host  = os.getenv("WEB_HOST"),
        port  = os.getenv("WEB_PORT"),
        debug = os.getenv("DEBUG"),
    )