import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

prcp_engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(prcp_engine, reflect=True)

Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(prcp_engine)

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

@app.route("//api/v1.0/precipitation")
def prcp():
     prcp_results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > '2016-08-22').all()

    prcp_totals = []
    for prcps in prcp_results:
        prcp_dictionary = {}
        prcp_dictionary["date"] = Measurement.date
        prcp_dictionary["tobs"] = Measurement.tobs
        prcp_totals.append(prcp_dictionary)
    return jsonify(prcp_totals)


@app.route("/api/v1.0/stations")
def stations():
    station_results = session.query(Station.station).all()
    
    stations_total = list(np.ravel(station_results))
    
    return jsonify(stations_total)


@app.route("/api/v1.0/tobs")
def tobs():
    tobs_results = session.query(Measurement.tobs).filter(Measurement.date > '2016-08-22').all()
    
    tobs_total = list(np.ravel(tobs_results))
    
    return jsonify(tobs_total)


@app.route("/api/v1.0/<start>")
    def calc_temp1(start_date)
      start_date = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    return jsonify(calc_temp1)


@app.route("/api/v1.0/<start>/<end>")
    def calc_temp2(start_date, end_date)
      start_date = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    return jsonify(calc_temp.)

if __name__ == "__main__":
    app.run(debug=True)
