from object_helpers import *
from data_objects import *
from create_extra_objects import *


import json


def create_competitions() -> [Competition]:
    file = open("./open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/competitions.json", encoding="utf-8")
    data = json.load(file)
    competitions = []
    for item in data:
        comp = Competition(item["competition_name"], item["season_name"], item["competition_id"], item["season_id"],
                           item["competition_gender"], item["competition_youth"], item["competition_international"],
                            item["match_updated"], item["match_updated_360"], item["match_available_360"],
                            item["match_available"], [])
        if comp.competition_name == "La Liga":
            if comp.season_name in ["2020/2021", "2019/2020", "2018/2019"]:
                competitions.append(comp)
        if comp.competition_name == "Premier League" and comp.season_name == "2003/2004":
            competitions.append(comp)
    create_matches(competitions)
    return competitions


def create_managers(item):
    if item is None:
        return []
    arr = []
    for val in item:
        arr.append(Manager(
            val.get("id"), val.get("name"), val.get("nickname"), val.get("dob"),
            get_nested_value(val, "country", "id"),
        get_nested_value(val, "country", "name")
        ))
    return arr


def create_lineup_players(data):
    arr = []
    for item in data:
        arr.append(Player(item.get("player_id"),
                           item.get("player_name"),
                           item.get("player_nickname"),
                           item.get("jersey_number"),
                           get_nested_value(item, "country", "id"),
                           get_nested_value(item, "country", "name")))
    return arr


def create_lineup(match: Match):
    file = open(
        f"./open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/lineups/{match.id}.json",
        encoding="utf-8")
    data = json.load(file)
    for item in data:
        lineup = Lineup(item.get("team_id"), item.get("team_name"), create_lineup_players(item.get("lineup")))
        print(lineup)
        match.lineups.append(lineup)

def create_matches(comps: [Competition]):
    for comp in comps:
        file = open(
            f"./open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches/{comp.competition_id}/{comp.season_id}.json",
            encoding="utf-8")
        data = json.load(file)
        for item in data:
            match = Match(item["match_id"],
                          get_nested_value(item, "competition", "competition_id"),
                          get_nested_value(item, "competition", "competition_name"),
                          get_nested_value(item, "competition", "country_name"),
                          get_nested_value(item, "season", "season_id"),
                          get_nested_value(item, "season", "season_name"),
                          item.get("match_date"), item.get("kick_off"),
                          get_nested_value(item, "stadium", "id"),
                          get_nested_value(item, "stadium", "name"),
                          get_nested_value2(item, "stadium", "country", "id"),
                          get_nested_value2(item, "stadium", "country", "name"),
                          get_nested_value(item, "referee", "id"),
                          get_nested_value(item, "referee", "name"),
                          get_nested_value2(item, "referee","country", "id"),
                          get_nested_value2(item, "referee","country", "name"),
                          Team(get_nested_value(item, "home_team", "home_team_id"),
                          get_nested_value(item, "home_team", "home_team_name"),
                          get_nested_value(item, "home_team", "home_team_gender"),
                          get_nested_value(item, "home_team", "home_team_group"),
                          get_nested_value2(item, "home_team", "country", "id"),
                          get_nested_value2(item, "home_team","country", "name")),
                          create_managers(get_nested_value(item, "home_team", "managers")),
                          Team(get_nested_value(item, "away_team", "away_team_id"),
                          get_nested_value(item, "away_team", "away_team_name"),
                          get_nested_value(item, "away_team", "away_team_gender"),
                          get_nested_value(item, "away_team", "away_team_group"),
                          get_nested_value2(item, "away_team", "country", "id"),
                          get_nested_value2(item, "away_team","country", "name")),
                          create_managers(get_nested_value(item, "away_team", "managers")),
                          item.get("home_score"), item.get("away_score"), item.get("match_status"), item.get("match_week"),
                          get_nested_value(item, "competition_stage", "id"),
                          get_nested_value(item, "competition_stage", "name"),
                          item.get("last_updated"), json.dumps(item.get("metadata")),
                          [], []
                          )
            comp.matches.append(match)
            create_lineup(match)


def create_tactics(event):
    x = event.get("tactics")
    if x is not None:
        lineup = []
        for teammate in x["lineup"]:
            lineup.append((get_nested_value(teammate, "player", "id"),
                           get_nested_value(teammate, "position", "id"), teammate["jersey_number"]))
        return Tactics(event["id"], 0, x["formation"], lineup)
    else:
        return None


def create_event(event, match):
    location_x, location_y = event.get("location") or (None, None)
    player_id, player_name = get_pair(event, "player") or (None, None)
    position_id, position_name = get_pair(event, "position") or (None, None)
    type_id = event["type"]["id"]
    type_name = event["type"]["name"]
    possession_team_id = event["possession_team"]["id"]
    possession_team_name = event["possession_team"]["name"]
    play_pattern_id = event["play_pattern"]["id"]
    play_pattern_name = event["play_pattern"]["name"]
    team_id = event["team"]["id"]
    team_name = event["team"]["name"]

    return Event(match.id, event["id"], event["index"], event["period"], event["timestamp"],
                 event["minute"], event["second"], type_id, type_name, event["possession"], possession_team_id,
                 possession_team_name, play_pattern_id, play_pattern_name, team_id, team_name,
                 player_id, player_name, position_id, position_name, location_x, location_y,
                 event.get("duration"), event.get("under_pressure"), event.get("off_camera"), event.get("out"),
                 event.get("related_events") or [], create_tactics(event), create_event_any(event))


def create_event_any(event):
    match event["type"]["id"]:
        case 2:
            return create_ball_recovery(event)
        case 4:
            return create_duel(event)
        case 6:
            return create_block(event)
        case 9:
            return create_clearance(event)
        case 10:
            return create_interception(event)
        case 14:
            return create_dribble(event)
        case 16:
            return create_shot(event)
        case 17:
            return create_pressure(event)
        case 18:
            return create_half_start(event)
        case 19:
            return create_substitution(event)
        case 21:
            return create_foul_won(event)
        case 22:
            return create_foul_committed(event)
        case 23:
            return create_goal_keeper(event)
        case 24:
            return create_bad_behavior(event)
        case 27:
            return create_player_off(event)
        case 30:
            return create_pass(event)
        case 33:
            return create_fifty_fifty(event)
        case 34:
            return create_half_end(event)
        case 38:
            return create_miscontrol(event)
        case 39:
            return create_dribbled_past(event)
        case 40:
            return create_injury_stoppage(event)
        case 42:
            return create_ball_receipt(event)
        case 43:
            return create_carry(event)
