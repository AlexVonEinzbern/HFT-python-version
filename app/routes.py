from flask import request
from flask import current_app as app
from .models import db, Peer, PeerSchema

peer_schema = PeerSchema()
peers_schema = PeerSchema(many=True)

@app.route('/createPeer', methods=['POST'])
def createPeer():
    host = request.json['host']
    file = request.json['file']

    new_peer = Peer(host=host, file=file)
    db.session.add(new_peer)
    db.session.commit()
    return peer_schema.jsonify(new_peer)

@app.route('/getPeers', methods=['GET'])
def getPeers():
    peers = Peer.query.all()
    return peers_schema.jsonify(peers)

@app.route('/getPeer/<file_name>', methods=['GET'])
def getPeer(file_name):
    peer = Peer.query.filter_by(file=file_name)
    return peers_schema.jsonify(peer)
