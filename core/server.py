from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException

from core.config import get_config
from core.libs import helpers
from core.libs.database import db, migrate
from core.apis.assignments import student_assignments_resources, teacher_assignments_resources, principal_assignments_resources
from core.libs.exceptions import FyleError  # Make sure this import is correct

app = Flask(__name__)
app.config.update(get_config())

# Initialize the database and migrations with the app
db.init_app(app)
migrate.init_app(app, db)

# Register blueprints
app.register_blueprint(student_assignments_resources, url_prefix='/student')
app.register_blueprint(teacher_assignments_resources, url_prefix='/teacher')
app.register_blueprint(principal_assignments_resources, url_prefix='/principal')

@app.route('/')
def ready():
    response = jsonify({
        'status': 'ready',
        'time': helpers.get_utc_now()
    })
    return response

@app.errorhandler(Exception)
def handle_error(err):
    if isinstance(err, FyleError):
        return jsonify(
            error=err.__class__.__name__, message=err.message
        ), err.status_code
    elif isinstance(err, ValidationError):
        return jsonify(
            error=err.__class__.__name__, message=err.messages
        ), 400
    elif isinstance(err, IntegrityError):
        return jsonify(
            error=err.__class__.__name__, message=str(err.orig)
        ), 400
    elif isinstance(err, HTTPException):
        return jsonify(
            error=err.__class__.__name__, message=str(err)
        ), err.code

    raise err

if __name__ == '__main__':
    app.run()