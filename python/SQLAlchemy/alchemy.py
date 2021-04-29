from sqlalchemy import create_engine
from sqlalchemy import text
import pymysql

engine = create_engine("mysql+pymysql://root:mysql@localhost:3306/TESTALCHEMY")
# engine.connect()

with engine.connect() as connection:
    result = connection.execute(text("select user,user_id,age from myTable"))
    for user,user_id,age in result:
        print("user_id is:", user_id)
        print("user is:", user)
        print("age is:", age)
    