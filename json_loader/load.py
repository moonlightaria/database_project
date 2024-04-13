import time

import psycopg
from tables import *
from data_objects import *
from create_objects import *
from extra_tables import add_extra_event_data

root_database_name = "project_database"
dbname = "query_database"
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
conn = psycopg.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conn.cursor()


def load_competition(comps, cursor):
    for comp in comps:
        add_competition(cursor, comp)


def load_events(comps: [Competition], cursor):
    for comp in comps:
        for match in comp.matches:
            file = open(f"./open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/events/{match.id}.json",
                        encoding="utf-8")
            data = json.load(file)
            for event_data in data:
                event = create_event(event_data, match)
                #add_event_team(cursor, event.team_id, event.team_name)
                #add_event_team(cursor, event.possession_team_id, event.possession_team_name)
                #add_event_player(cursor, event.player_id, event.player_name)
                add_event(cursor, event, match)
                add_event_time(cursor, event)
                add_event_tactic(cursor, event.tactics)


def load_events_extra(comps: [Competition], cursor):
    for comp in comps:
        for match in comp.matches:
            file = open(f"./open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/events/{match.id}.json",
                        encoding="utf-8")
            data = json.load(file)
            for event_data in data:
                event = create_event(event_data, match)
                add_extra_event_data(cursor, event.event_id, event.extra_data)


def load_matches(comps, cursor):
    for comp in comps:
        for match in comp.matches:
            add_match_stage(cursor, match.competition_stage_id, match.competition_stage_name)
            add_match_country(cursor, match.referee_country_id, match.referee_country_name)
            add_match_country(cursor, match.stadium_country_id, match.stadium_country_name)
            add_match_country(cursor, match.home_team.team_country_id, match.home_team.team_country_id)
            add_match_country(cursor, match.away_team.team_country_id, match.away_team.team_country_id)
            add_match_team(cursor, match.home_team)
            add_match_team(cursor, match.away_team)
            add_match_referee(cursor, match)
            add_match_stadium(cursor, match)
            add_match(cursor, match)
            for manager in match.home_team_managers:
                add_match_country(cursor, manager.country_id, manager.country_name)
                add_manager(cursor, manager)
                add_match_manager(cursor, match.id, match.home_team.team_id, manager.id)
            for manager in match.away_team_managers:
                add_match_country(cursor, manager.country_id, manager.country_name)
                add_manager(cursor, manager)
                add_match_manager(cursor, match.id, match.home_team.team_id, manager.id)


def load_lineup(comps, cursor):
    for comp in comps:
        for match in comp.matches:
            id = match.id
            for lineup in match.lineups:
                team = lineup.team_id
                for player in lineup.players:
                    add_match_country(cursor, player.country_id, player.country_name)
                    add_event_player(cursor, player)
                    add_match_lineup(cursor, player, id, team)

if __name__ == "__main__":
    conn.autocommit = True
    comps = create_competitions()

    load_competition(comps, cursor)
    load_matches(comps, cursor)
    load_lineup(comps, cursor)
    load_events(comps, cursor)
    load_events_extra(comps, cursor)
