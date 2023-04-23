from flask_restful import Resource

hoteis = [
    {
    'hotel_id': 'alpha',
    'nome': 'alpha Hotel',
    'estrelas': 4.3,
    'diaria': 420.20,
    'cidade': 'Rio de janeiro'
    },

    {
    'hotel_id': 'Bravo',
    'nome': 'Bravo Hotel',
    'estrelas': 5.5,
    'diaria': 420.20,
    'cidade': 'Rio de janeiro'
    },

    {
    'hotel_id': 'Charlie',
    'nome': 'Charlie Hotel',
    'estrelas': 4.3,
    'diaria': 420.20,
    'cidade': 'Rio de janeiro'
    },

    {
    'hotel_id': 'alpha',
    'nome': 'alpha hotel',
    'estrelas': 4.3,
    'diaria': 420.20,
    'cidade': 'Rio de janeiro'
    },
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}