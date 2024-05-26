import os
from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from graphql_schema import schema

from keycloak import KeycloakOpenID

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)

app.config.from_envfile('.env')

keycloak_openid = KeycloakOpenID(server_url="KEYCLOAK_SERVER_URL",
                                 client_id="CLIENT_ID",
                                 realm_name="REALM_NAME")
                    
engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
db = Session()

app.add_url_rule('/graphql',view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, context=lambda: {'keycloak': keycloak}))

@app.route('/login')

def login():
    return keycloak_openid.render_login_url()

@app.route('/callback')

def callback():
    code = request.args.get('code')
    token = keycloak_openid.token(code)
    userinfo = keycloak_openid.userinfo(token['access_token'])
    return f'Welcome, {userinfo["preferred_username"]}!'  


if __name__ == '__main__':
    app.run(debug=True, port=8080)           