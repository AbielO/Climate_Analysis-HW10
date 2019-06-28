import numpy as np

#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#prcp_engine = create_engine("")

#Base = automap_base()

#Measurement = Base.classes.measurement
#Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

#@app.route("//api/v1.0/precipitation")
#def prcp():
     #return jsonify(prcp_engine)


if __name__ == "__main__":
    app.run(debug=True)
