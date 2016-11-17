import os.path
instance_path = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db.sqlite' % instance_path