# Bug-free-train

Api for projecting images (maps) and displaying them on a TUI

- Consider image storage, images are currently posted from ``http://localhost:8500/media/{url}`` . `localhost:8500` is a Django server

- ``localhost:80 See image``
- ``losthost:5000 Api Fastapi (contains endopoints) ``
- ``losthost:9001 Server MQTT ``

# Quick start

1. Clone repository
2. Run `docker compose up -d --build` and start the services

# How to use

1. Write in your browser ``localhost`` this shows the image you will display, use ``Google Chrome``

2. Send an image 
    - In local: 
        you can send a GET REQUEST ``localhost:5000/mount/{static_value}`` 
        ex: http://localhost:5000/mount/xp.jpg
    
    - With Django Server:

## Random things

Caracterisitcas importantes de la imagen:

- imagen.style.transform = `scale(${escalaX}, ${escalaY})` ROTATE IMAGE, NOT ZOOM
- keystoneContainer.style.transform = `matrix3d(-0.0767133, -1.02482, 0, -1.94e-05, 1.04147, 0.0155276, 0, 9.7e-06, 0, 0, 1, 0, 3940, 1595, 0, 1)`;
 

