from app import create_app
import os

if __name__ == "__main__":
    config_name = os.getenv('FLASK_ENV')
    app = create_app(config_name)
    app.run(debug=True)
