# Bug-free-train

Api for projecting images (maps) and displaying them on a TUI

- Consider image storage, images are currently posted from ``http://localhost:8500/media/{url}`` . `localhost:8500` is a Django server

- ``localhost:80 See image``
- ``losthost:5000 Api Fastapi (contains endopoints) ``

# Quick start

1. Clone repository
2. Run `docker compose up -d --build` and start the services

# How to use

1. Write in your browser ``localhost`` this shows the image you will display, use ``Google Chrome``

2. To send an image 
    - In local: 
        you can send a GET REQUEST ``localhost:5000/mount/{static_value}`` 
        ex: http://localhost:5000/mount/xp.jpg
    
    - With Django Server:
