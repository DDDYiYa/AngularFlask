import click
from flask import Flask, jsonify 
from sqlalchemy import create_engine

from settings import BaseConfig,db_url,dbname
from extensions import db
from blueprints.hello import hello_bp
from models import user

app = Flask(__name__)

app.config.from_object(BaseConfig)

db.init_app(app)

app.register_blueprint(hello_bp, url_prefix='/hello')

@app.route("/",methods=['GET'])
def index():
    return "Index!"

@app.cli.command()
def createdb():
    click.echo('Initializing database......')
    engine = db.create_engine(db_url,{}) # connect to server

    # engine.execute("DROP DATABASE " + dbname) #drop db
    # click.echo('Drop database ' + dbname)

    engine.execute("CREATE DATABASE " + dbname) #create db
    click.echo('Create database ' + dbname)

@app.cli.command()
def initdb():
    db.create_all() # create tables
    click.echo('Create tables.')
    
