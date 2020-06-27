import time
from connect_to_db import ConnectToDb
from map_of_the_world import CreatingMap
from map_of_the_world import CreatingMap

if __name__ == "__main__":
    ConnectToDb().run_sql_script(scripts="db_init.sql")

    time.sleep(3)
    ConnectToDb().run_sql_script("towns.sql")
    CreatingMap().map_of_the_world()
