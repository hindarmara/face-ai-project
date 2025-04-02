from flask import Flask
from flask_cors import CORS
from routes import routes

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register blueprint
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)