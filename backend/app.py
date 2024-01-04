from fastapi import FastAPI, HTTPException, Body

import os
import paho.mqtt.publish as publish

app = FastAPI()
mqtt_broker = os.getenv('MQTT_BROKER', 'localhost')
mqtt_port = int(os.getenv('MQTT_PORT', 1883))

@app.post('/post-image')
async def post_image(url: str = Body(...)):
    publish.single("proyectores", url, hostname=mqtt_broker, port=mqtt_port)
    return {"message": "Image URL sent to MQTT broker."}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
