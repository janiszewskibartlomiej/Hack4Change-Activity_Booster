from flask import Flask
from sqlalchemy import event, create_engine
from sqlalchemy.orm import sessionmaker
from models import *


app = Flask(__name__)
app.secret_key = 'ZeroAbsolutneTylkoWOdwrotnaStrone'


def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')


def get_session(echo=False):
    engine = create_engine('sqlite:///database.db', echo=echo)
    DBSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    event.listen(engine, 'connect', _fk_pragma_on_connect)

    return DBSession()

session = get_session()


import routes

if __name__ == '__main__':
    app.run(debug=True)
