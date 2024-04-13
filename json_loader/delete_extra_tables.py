import psycopg
from extra_tables import create_extra_tables

dbname = "query_database"
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
conn = psycopg.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

cursor.execute("drop table event_ball_recovery, event_duel, event_block, event_clearance, event_interception,"
               "event_dribble, event_shot, event_freeze_frame, event_pressure, event_half_start, event_half_end,"
               "event_substitution, event_foul_won, event_foul_committed, event_goal_keeper, event_pass,"
               "event_bad_behavior, event_player_off, event_fifty_fifty, event_miscontrol, event_injury_stoppage,"
               "event_ball_receipt, event_carry")

create_extra_tables(cursor)
conn.commit()