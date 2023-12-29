from flask import request, jsonify, views
from datetime import datetime
from . import app
from .recomendations.recomendations_engine_3 import get_recomendations


class RecommendMovieView(views.MethodView):
    """
    APIs Methods
    -----------
    GET: Return recommended movies as per given description.
    """
    def get(self):
        try:
            """
            @param: description > "Avatar"
            """
            if not request.args.get('description',  type=str):
                return jsonify({"error": "Param 'description' is required!"}), 400

            data = get_recomendations(request.args.get('description'))
            response = jsonify({"message": ("Success"), "data": data})
            response.status_code = 200

        except Exception as error:
            response = jsonify({"error": "Something Went Wrong!"}), 400
        return response