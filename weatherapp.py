from flask import Flask, render_template
from sense_hat import SenseHat

app =Flask(__name__)

@app.route("/")

def index():
	sense = SenseHat()
	cTemp = round(sense.get_temperature(), 1)
	fTemp = round(sense.get_temperature() * 1.8 + 32, 1)
	humidity = round(sense.get_humidity(), 1)
	pressure = round(sense.get_pressure())
	inpressure = round(pressure/33.864, 2)

	return render_template("weathersite.html", cTemp=cTemp, fTemp=fTemp, humidity=humidity, pressure=pressure, inpressure=inpressure)

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")

