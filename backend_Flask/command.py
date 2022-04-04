import click
from sqlalchemy import create_engine
from settings import db_url,dbname
from app import app,db
from models import User

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop database.')
def createdb(drop):
    click.echo('Initializing the database......')
    engine = db.create_engine(db_url,{}) # connect to server
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        engine.execute("DROP DATABASE " + dbname) #drop db
        click.echo('Drop database ' + dbname)
    engine.execute("CREATE DATABASE " + dbname) #create db
    click.echo('Create database ' + dbname)

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop tables.')
def initdb(drop):
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all() # drop tables
        click.echo('Drop tables.')
    db.create_all() # create tables
    click.echo('Create tables.')


@app.cli.command()
@click.option('--count', default=20, help='Quantity of fake data, default is 20.')
def forge(count):
    from faker import Faker

    db.drop_all() # drop tables
    db.create_all() # create tables

    fake=Faker('zh_CN')
    click.echo('working......')

    for i in range(count):
        user=User(
            userName=fake.name(),
            passwd=fake.password(),
            userCity=fake.city()
        )
        db.session.add(user)
    db.session.commit()
    click.echo('Creates %d faker messages.'%count)

