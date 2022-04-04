user = 'yanjun'
passwd = ''
host = 'localhost'
dbname = 'AngularFlask_login'
db_url = 'mysql://{0}:{1}@{2}'.format(user, passwd, host)
db_uri = 'mysql://{0}:{1}@{2}/{3}'.format(user, passwd, host, dbname)

class BaseConfig:
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False