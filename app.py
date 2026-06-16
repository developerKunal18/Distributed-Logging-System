from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# ---------- Config ----------
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///logs.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ---------- Model ----------
class Log(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    service_name = db.Column(
        db.String(100)
    )

    level = db.Column(
        db.String(20)
    )

    message = db.Column(
        db.String(500)
    )

    timestamp = db.Column(
        db.String(100)
    )


with app.app_context():
    db.create_all()


# ---------- Add Log ----------
@app.route(
    "/logs",
    methods=["POST"]
)
def add_log():

    data = request.get_json()

    log = Log(
        service_name=data["service_name"],
        level=data["level"],
        message=data["message"],
        timestamp=str(datetime.now())
    )

    db.session.add(log)
    db.session.commit()

    return jsonify({
        "message": "Log stored"
    })


# ---------- Get Logs ----------
@app.route("/logs")
def get_logs():

    logs = Log.query.all()

    return jsonify([
        {
            "service_name": log.service_name,
            "level": log.level,
            "message": log.message,
            "timestamp": log.timestamp
        }
        for log in logs
    ])


# ---------- Filter By Service ----------
@app.route(
    "/logs/<service_name>"
)
def service_logs(service_name):

    logs = Log.query.filter_by(
        service_name=service_name
    ).all()

    return jsonify([
        {
            "level": log.level,
            "message": log.message,
            "timestamp": log.timestamp
        }
        for log in logs
    ])


# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


# ---------- Run ----------
if __name__ == "__main__":

    app.run(
        debug=True
    )
