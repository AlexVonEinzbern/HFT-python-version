from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:4826494629@db:5432/hft'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

class Peer(db.Model):
    id_peer = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(20), unique=True, nullable=False)
    file = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<Peer %r>' % self.host

db.create_all()

class PeerSchema(ma.Schema):
    class Meta:
        fields = ('id_peer', 'host', 'file')

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

@app.route('/getPeer/<file>', methods=['GET'])
def getPeer(file):
    peer = Peer.query.filter_by(file=file)
    return peers_schema.jsonify(peer)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')