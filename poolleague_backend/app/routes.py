from flask import Blueprint, request, jsonify
from .models     import Player
from .extensions import db

main = Blueprint('main', __name__)

@main.route('/players', methods=['POST'])
def create_player():
    data = request.get_json()
    p = Player(name=data['name'], avg=data.get('avg'))
    db.session.add(p)
    db.session.commit()
    return jsonify({'id': p.id, 'name': p.name, 'avg': p.avg}), 201

@main.route('/players', methods=['GET'])
def list_players():
    players = Player.query.all()
    return jsonify([
        {'id': p.id, 'name': p.name, 'avg': p.avg} for p in players
    ])
