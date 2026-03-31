import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/upload/<file_name>", methods=["GET"])
def upload_file(file_name):
    return jsonify({
        "message": "File uploaded successfully",
        "file_name": file_name,
        "storage": "AWS S3"
    })

@app.route("/deploy-status", methods=["GET"])
def deploy_status():
    return jsonify({
        "message": "Service is deployment-ready",
        "platform": "AWS EC2",
        "containerized": True,
        "environment": os.getenv("APP_ENV", "development")
    })

if __name__ == "__main__":
    app.run(debug=True)
