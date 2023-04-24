from flask_restful import Resource, reqparse

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

class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
            hotel = Hotel.find_hotel(hotel_id)
            if hotel:
                return hotel
            return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel
    
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201


    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}