from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import os
import shutil
import paho.mqtt.publish as publish

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name = "static")

mqtt_broker = os.getenv('MQTT_BROKER', 'localhost')
mqtt_port = int(os.getenv('MQTT_PORT', 1883))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o especifica los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/post-image')
async def post_image(request_data: dict):
    print(request_data)
    url = request_data.get('url')
    address = 'localhost'
    url = f'http://{address}:8500/media/{url}'
    print(url)
    publish.single("proyectores", url, hostname=mqtt_broker, port=mqtt_port)
    return {"message": f"Image URL sent to MQTT broker. \nurl = {url}"}

@app.get('/hola2/{nombregif}')
async def hola2(nombregif: str):
    address = 'localhost'
    url = f'http://{address}:5000/static/{nombregif}.gif'
    print(url)
    publish.single("proyectores", url, hostname=mqtt_broker, port=mqtt_port)
    return {"message": f"Image URL sent to MQTT broker. \nurl = {url}"}

@app.get('/mount/{static_value}')
async def hola2(static_value: str):
    address = 'localhost'
    url = f'http://{address}:5000/static/{static_value}'
    print(url)
    publish.single("proyectores", url, hostname=mqtt_broker, port=mqtt_port)
    return {"message": f"Image URL sent to MQTT broker. \nurl = {url}"}


@app.get('/send_cap/{static_value}')
async def send_cap(static_value: str):
    address = 'localhost'
    url = f'http://{address}:5000/static/{static_value}'
    publish.single("capa", url, hostname=mqtt_broker, port=mqtt_port)

    return {"message": f"Cap send"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
