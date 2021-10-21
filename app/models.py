"""Data models"""

from . import db, ma

class Peer(db.Model):
    id_peer = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(20), unique=True, nullable=False)
    file = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<Peer {}>'.format(self.host)

    
class PeerSchema(ma.Schema):
    class Meta:
        fields = ('id_peer', 'host', 'file')