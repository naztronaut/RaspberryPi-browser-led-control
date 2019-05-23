from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)


# {{url}}/led?status=on
@app.route('/', methods=['GET'])
def led():
    status = request.args.get('status')
    if status == "on":
        GPIO.output(18, GPIO.HIGH)
        return jsonify({"message": "Led successfully turned on"})
    elif status == "off":
        GPIO.output(18, GPIO.LOW)
        return jsonify({"message": "Led successfully turned off"})
    else:
        return jsonify({"message": "Not a valid status"})
