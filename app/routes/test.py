from flask import Blueprint, jsonify

test_bp = Blueprint(
    'test_bp',
    __name__,
    url_prefix='/test',
)


@test_bp.route('/', methods=['POST', 'GET'])
def test():
    return jsonify({"Hello": "World"})
