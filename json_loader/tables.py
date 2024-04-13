from known_tables import create_known_tables
from extra_tables import create_extra_tables
from extra_tables import *
from data_objects import *


def create_tables(cursor):
    create_known_tables(cursor)
    create_competition(cursor)
    create_match_stage(cursor)
    create_match_country(cursor)
    create_event_player(cursor)
    create_manager(cursor)
    create_match_team(cursor)
    create_match_referee(cursor)
    create_match_stadium(cursor)
    create_match(cursor)
    create_match_manager(cursor)
    create_match_lineup(cursor)
    create_event(cursor)
    create_event_tactic(cursor)
    create_event_time(cursor)
    create_tactics_lineup(cursor)
    create_extra_tables(cursor)


def create_event_tactic(cursor):
    cursor.execute("""
                    create table event_tactic 
                    (tactics_id serial, event_id uuid, formation int,
                    primary key (tactics_id), foreign key (event_id) references event);""")


def add_event_tactic(cursor, tactics):
    if tactics is not None:
        cursor.execute("""
                        insert into event_tactic
                        (event_id, formation)
                        values (%s, %s) returning tactics_id;""",
                       [tactics.event_id, tactics.formation])
        tactics.id = cursor.fetchone()[0]
        add_tactics_lineup(cursor, tactics)


def create_tactics_lineup(cursor):
    cursor.execute("""
                    create table tactics_lineup
                    (lineup_id serial, tactics_id int, player_id int, position_id smallint, jersey smallint,
                    primary key (lineup_id), foreign key (tactics_id) references event_tactic,
                    foreign key (player_id) references event_player, foreign key (position_id) references event_position);""")


def add_tactics_lineup(cursor, tactics):
    for teammate in tactics.lineup:
        cursor.execute("""
                        insert into tactics_lineup
                        (tactics_id, player_id, position_id, jersey)
                        values (%s, %s, %s, %s);""",
                       [tactics.id, teammate[0], teammate[1], teammate[2]])


def create_event(cursor):
    cursor.execute("""
                    create table event 
                    (match_id int, event_id uuid, type_id smallint, possession smallint, possession_team_id smallint,
                    play_pattern_id smallint, team_id smallint, player_id int, position_id smallint, location_x smallint,
                    location_y smallint, under_pressure bool, off_camera bool, out bool, related_events uuid[],
                    primary key (event_id), foreign key (possession_team_id) references match_team,
                    foreign key (team_id) references match_team, foreign key (play_pattern_id) references event_plays,
                    foreign key (player_id) references event_player, foreign key (type_id) references event_type,
                    foreign key (position_id) references event_position, foreign key (match_id) references match);""")


def add_event(cursor, event, match):
    cursor.execute("""
                    insert into event 
                    (match_id, event_id, type_id, possession,possession_team_id, play_pattern_id, team_id,
                    player_id, position_id, location_x, location_y, under_pressure, off_camera, out,
                    related_events)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """,
                   [match.id, event.event_id, event.type_id, event.possession, event.possession_team_id,
                    event.play_pattern_id, event.team_id, event.player_id, event.position_id, event.location_x,
                    event.location_y, event.under_pressure, event.off_camera, event.out, event.related_events])


def create_event_time(cursor):
    cursor.execute("""
                    create table event_time
                    (event_id uuid, index int, period int, timestamp time,
                    minute int, second int, duration float8,
                    primary key (event_id), foreign key (event_id) references event)
                    """)


def add_event_time(cursor, event):
    cursor.execute("""
                    INSERT INTO event_time (event_id, index, period, timestamp, minute, second, duration) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, [event.event_id, event.index, event.period, event.timestamp, event.minute, event.second,
                          event.duration])


def create_competition(cursor):
    cursor.execute("""
        create table competition (comp_id integer, season_id integer,
        gender varchar(10), youth bool, international bool, updated timestamp, updated_360 timestamp, available timestamp,
        available_360 timestamp, primary key (comp_id, season_id), foreign key (comp_id) references competition_name,
        foreign key (season_id) references season_name);""")


def add_competition(cursor, comp: Competition):
    cursor.execute("""
                    INSERT INTO competition (comp_id, season_id, gender, youth, international, 
                    updated, updated_360, available, available_360) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                    """, [comp.competition_id, comp.season_id, comp.gender,
                          comp.youth, comp.international, comp.updated, comp.updated_360, comp.available, comp.available_360])


def create_match(cursor):
    cursor.execute("""
            create table match (match_id integer, competition_id smallint, season_id smallint, match_date date, kickoff time, 
            stadium_id int, referee_id int, home_team_id smallint, away_team_id smallint, home_score smallint, away_score smallint,
            match_status varchar(20), match_week smallint, competition_stage_id smallint, last_updated timestamp, metadata json,
            primary key (match_id), foreign key (competition_id, season_id) references competition,
            foreign key (competition_id) references competition_name, foreign key (season_id) references season_name,
            foreign key (stadium_id) references match_stadium, 
            foreign key (referee_id) references match_referee, foreign key (home_team_id) references match_team,
            foreign key (away_team_id) references match_team, foreign key (competition_stage_id) references match_stage);""")


def add_match(cursor, match: Match):
    cursor.execute("""
            INSERT INTO match (match_id, competition_id, season_id, match_date, kickoff, 
            stadium_id, referee_id, home_team_id, away_team_id, home_score, away_score,
            match_status, match_week, competition_stage_id, last_updated, metadata) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, [match.id, match.competition_id, match.season_id, match.match_date, match.kickoff,
                      match.stadium_id, match.referee_id, match.home_team.team_id, match.away_team.team_id, match.home_score,
                      match.away_score, match.match_status, match.match_week, match.competition_stage_id, match.last_updated,
                      match.metadata])


def create_match_stadium(cursor):
    cursor.execute("""
            create table match_stadium (stadium_id int, stadium_name varchar(50), stadium_country_id smallint,
            primary key (stadium_id), foreign key (stadium_country_id) references match_country);""")


def add_match_stadium(cursor, match: Match):
    try:
        cursor.execute("""
                INSERT INTO match_stadium (stadium_id, stadium_name, stadium_country_id) 
                    VALUES (%s, %s, %s);
                    """, [match.stadium_id, match.stadium_name, match.stadium_country_id])
    except Exception:
        pass


def create_match_referee(cursor):
    cursor.execute("""
            create table match_referee (referee_id int, referee_name varchar(50), referee_country_id smallint,
            primary key (referee_id), foreign key (referee_country_id) references match_country);""")


def add_match_referee(cursor, match: Match):
    if match.referee_id is not None:
        try:
            cursor.execute("""
                    INSERT INTO match_referee (referee_id, referee_name, referee_country_id) 
                        VALUES (%s, %s, %s);
                        """, [match.referee_id, match.referee_name, match.referee_country_id])
        except Exception:
            pass


def create_match_team(cursor):
    cursor.execute("""create table match_team (team_id smallint, team_name varchar(23), team_gender varchar(10),
                   team_group varchar(20), team_country_id smallint, primary key (team_id),
                   foreign key (team_country_id) references match_country)""")


def add_match_team(cursor, team: Team):
    try:
        cursor.execute("""
                        INSERT INTO match_team (team_id, team_name, team_gender, team_group, team_country_id) 
                        VALUES (%s, %s, %s, %s, %s)
                        """, [team.team_id, team.team_name, team.team_gender, team.team_group, team.team_country_id])
    except Exception:
        pass


def create_manager(cursor):
    cursor.execute("""create table manager (manager_id smallint, manager_name varchar(50),
                      manager_nickname varchar(20), manager_dob date, manager_country_id smallint, primary key (manager_id),
                      foreign key (manager_country_id) references match_country)""")


def add_manager(cursor, manager: Manager):
    try:
        cursor.execute("""
                        INSERT INTO manager (manager_id, manager_name,
                          manager_nickname, manager_dob , manager_country_id) 
                        VALUES (%s, %s, %s, %s, %s)
                        """, [manager.id, manager.name, manager.nickname, manager.dob, manager.country_id])
    except Exception:
        pass


def create_match_manager(cursor):
    cursor.execute("""create table match_manager (manager_id smallint, match_id int, team_id smallint, 
                      primary key (manager_id, match_id, team_id), foreign key (manager_id) references manager, 
                      foreign key (match_id) references match, foreign key (team_id) references match_team)""")


def add_match_manager(cursor, id, team, manager):
    cursor.execute("""
                    INSERT INTO match_manager (manager_id, match_id, team_id) 
                    VALUES (%s, %s, %s)
                    """, [manager, id, team])


def create_match_country(cursor):
    cursor.execute("""create table match_country (country_id smallint, country_name varchar(50),
                       primary key (country_id))""")


def add_match_country(cursor, id, name):
    if id is not None:
        try:
            cursor.execute("""
                            INSERT INTO match_country (country_id, country_name) 
                            VALUES (%s, %s)
                            """, [id, name])
        except Exception:
            pass


def create_match_stage(cursor):
    cursor.execute("""create table match_stage (stage_id smallint, stage_name varchar(20),
                       primary key (stage_id))""")


def add_match_stage(cursor, id, name):
    try:
        cursor.execute("""
                        INSERT INTO match_stage (stage_id, stage_name) 
                        VALUES (%s, %s)
                        """, [id, name])
    except Exception:
        pass


def create_event_player(cursor):
    cursor.execute("""create table event_player (player_id int, player_name varchar(48), player_nickname varchar(48),
                   player_country_id smallint, primary key (player_id), foreign key (player_country_id) references match_country)""")


def add_event_player(cursor, player: Player):
    try:
        cursor.execute("""
                    INSERT INTO event_player (player_id, player_name, player_nickname, player_country_id) 
                    VALUES (%s, %s, %s, %s)
                    """, [player.id, player.name, player.nickname, player.country_id])
    except Exception as e:
        print(e)


def create_match_lineup(cursor):
    cursor.execute("""create table match_lineup (match_id int, team_id smallint, player_id int, jersey smallint,
                       primary key (match_id, player_id), foreign key (match_id) references match, 
                       foreign key (team_id) references match_team, foreign key (player_id) references event_player)""")


def add_match_lineup(cursor, player: Player, id, team):
    cursor.execute("""
                    INSERT INTO match_lineup (match_id, team_id, player_id, jersey) 
                    VALUES (%s, %s, %s, %s)
                    """, [id, team, player.id, player.jersey])