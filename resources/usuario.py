from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
#from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

import hmac

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank")


class User(Resource):
    def get(self, user_id):
            user = UserModel.find_user(user_id)
            if user:
                return user.json()
            return {'message': 'User not found.'}, 404
    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
                user.delete_user()
                return {'message': 'User deleted.'}, 500
        return {'message': 'User not found.'}, 404

class UserRegister(Resource):
      #/cadastro
      def post(self):
        dados = atributos.parse_args()
        if UserModel.find_by_login(dados['login']):
                return {"message": "The login '{}' already exists." .format(dados['login'])}

        user = UserModel(**dados)
        user.save_user()
        return {'message': 'User created successfully!'}, 200

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and hmac.compare_digest(user.senha.encode('utf-8'), dados['senha'].encode('utf-8')):
             token_de_acesso = create_access_token(identity=user.user_id)
             return {'access_token': token_de_acesso}, 200
        return {'message': 'Theusername or password is incorrect.'}, 401

class UserLogout(Resource):
     
     @jwt_required()
     def post(self):
          jwt_id = get_jwt()['jti'] #JWT Token Identifier
          BLACKLIST.add(jwt_id)
          return {'message': 'Logged out successfully!'}, 200