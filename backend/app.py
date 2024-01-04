from flask import Flask, request
import os
import paho.mqtt.publish as publish

app = Flask(__name__)
mqtt_broker = os.getenv('MQTT_BROKER', 'localhost')
mqtt_port = int(os.getenv('MQTT_PORT', 1883))

@app.route('/post-image', methods=['POST'])
def post_image():
    image_url = request.json.get('url')
    publish.single("proyectores", image_url, hostname=mqtt_broker, port=mqtt_port)
    return {"message": "Image URL sent to MQTT broker."}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
