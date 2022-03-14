import sentry_sdk, os, sys, shutil
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration
from dotenv import load_dotenv
load_dotenv()

sentry_sdk.init(
    dsn=os.environ["SENTRY_DSN"],
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/debug-sentry')
def trigger_error():
    print("hello there")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)