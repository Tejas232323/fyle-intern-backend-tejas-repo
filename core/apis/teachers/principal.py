from flask import Blueprint, jsonify
from core.models.teachers import Teacher
from core.apis.decorators import requires_principal_auth
from .schema import TeacherSchema

teachers_api = Blueprint('teachers_api', __name__)

@teachers_api.route('/principal/teachers', methods=['GET'])
@requires_principal_auth
def get_principal_teachers():
    try:
        teachers = Teacher.query.all()
        teachers_dump = TeacherSchema().dump(teachers, many=True)
        return jsonify({"data": teachers_dump}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
