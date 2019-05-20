# Raspberry Pi - Control an LED from a browser

This project contains the tutorial files for EasyProgramming.net

## Contents

1. Front end - index.html, script.js, and style.css make up a very simple frontend UI for our app
2. led - this directory contains the Flask app that will act as our back end app

### Installation 

Follow the tutorial here to learn how to run a Flask app behind Apache: https://www.easyprogramming.net/raspberrypi/pi_flask_apache.php

Since we are running `RPi.GPIO` from a virtual environment, we need to take one extra step after activating venv and install the package:

```bash
pip3 install RPi.GPIO
```

We need to do this because our virtual environment can't access the globally installed RPi.GPIO package

### Configurations

The `script.js` has jQuery that calls the Flask app using simple AJAX calls. They assume that the path for the flask app is `/led` - 
if you use another path, change this in the JavaScript to avoid getting 404s on your AJAX calls. 

If everything is set up correctly, the AJAX call will happen with the following url: `http://{{ip_addr}}/led?status=on`

Only a status of `on` or `off` are accepted. Anything else will return a simple error message. Open up the JavaScript console for more info.  