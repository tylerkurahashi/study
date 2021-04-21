from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("mysql+pymysql://root:mysql@mysql:3306")

with engine.connect() as connection:
    result = connection.execute(text("select username from users"))
    for row in result:
        print("username:", row["username"])