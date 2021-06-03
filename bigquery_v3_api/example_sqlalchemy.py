# example based off of https://github.com/googleapis/python-bigquery-sqlalchemy#sqlalchemy
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
# query a copy of bigquery-public-data.austin_311.311_service_requests
engine = create_engine('bigquery://clever-hangar-289701/austin_311')
table = Table('311_service_requests', MetaData(bind=engine), autoload=True)
print(select([func.count('*')], from_obj=table).scalar())
