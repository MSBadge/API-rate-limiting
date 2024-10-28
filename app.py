from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,  # Limit based on the IP address
    app=app,
    default_limits=["10 per minute"]
)

@app.route("/api/resource")
@limiter.limit("3 per minute")  # set limit for this endpoint
def get_data():
    return jsonify({"message": "This is an API rate limiting using Flask limiting extension."})

# error handler for rate limit exceeded
@app.errorhandler(429)
def ratelimit_exceeded(e):
    return jsonify({
        "error": "Too Many Requests",
        "message": " Please check your connectivity or your requests are many.",
        "status_code": 429
    }), 429

if __name__ == "__main__":
    app.run(debug=True)
