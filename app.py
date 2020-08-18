from flask import Flask, jsonify

# Dictionary of date and prcp
prcp = [
    {}
]

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(precipitation)


@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Precipitation API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
    )


if __name__ == "__main__":
    app.run(debug=True)