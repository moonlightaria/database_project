import csv
def create_known_tables(cursor):
    create_event_plays(cursor)
    create_event_positions(cursor)
    create_event_outcomes(cursor)
    create_event_type(cursor)
    create_event_extra_type(cursor)
    create_event_body_part(cursor)
    create_event_technique(cursor)
    create_event_card(cursor)
    create_event_extra_position(cursor)
    create_event_height(cursor)

    create_competition_name(cursor)
    create_season_name(cursor)


def load_known_tables(cursor):
    load_event_plays(cursor)
    load_event_positions(cursor)
    load_event_outcomes(cursor)
    load_event_type(cursor)
    load_event_extra_type(cursor)
    load_event_body_part(cursor)
    load_event_technique(cursor)
    load_event_card(cursor)
    load_event_extra_position(cursor)
    load_event_height(cursor)

    load_competition_name(cursor)
    load_season_name(cursor)


def create_event_plays(cursor):
    cursor.execute(
        "create table event_plays (play_pattern_id smallint, play_pattern_name varchar(14), primary key (play_pattern_id));")


def load_event_plays(cursor):
    play_pairs = [(1, "Regular Play"), (2, "From Corner"), (3, "From Free Kick"), (4, "From Throw In"),
                  (5, "Other"), (6, "From Counter"), (7, "From Goal Kick"), (8, "From Keeper"), (9, "From Kick Off")]
    for pair in play_pairs:
        cursor.execute("""
                INSERT INTO event_plays (play_pattern_id, play_pattern_name)
                VALUES (%s, %s)
                """, pair)


def create_event_positions(cursor):
    cursor.execute(
        "create table event_position (position_id smallint, position_name varchar(25), primary key (position_id))")


def load_event_positions(cursor):
    position_pairs = [(0, "Substitute"), (1, "GoalKeeper"), (2, "Right Back"), (3, "Right Center Back"),
                      (4, "Center Back"), (5, "Left Center Back"), (6, "Left Back"), (7, "Right Wing Back"),
                      (8, "Left Wing Back"), (9, "Right Defensive Midfield"), (10, "Center Defense Midfield"),
                      (11, "Left Defensive Midfield"), (12, "Right Midfield"), (13, "Right Center Midfield"),
                      (14, "Center Midfield"), (15, "Left Center Midfield"), (16, "Left Midfield"), (17, "Right Wing"),
                      (18, "Right Attacking Midfield"), (19, "Center Attacking Midfield"),
                      (20, "Left Attacking Midfield"), (21, "Left Wing"), (22, "Right Center Forward"), (23, "Striker"),
                      (24, "Left Center Forward"), (25, "Secondary Striker")]

    for pair in position_pairs:
        cursor.execute("""
                INSERT INTO event_position (position_id, position_name)
                VALUES (%s, %s)
                """, pair)


def create_event_outcomes(cursor):
    cursor.execute(
        "create table event_outcome (outcome_id smallint, outcome_name varchar(21), primary key (outcome_id))")


def load_event_outcomes(cursor):
    outcome_pairs = [(1, "Lost"), (2, "Success To Opposition"), (3, "Success To Team"), (4, "Won"), (8, "Complete"),
                     (9, "Incomplete"), (13, "Lost In Play"), (14, "Lost Out"), (15, "Success"), (16, "Success In Play"),
                     (17, "Success Out"), (47, "Claim"), (48, "Clear"), (49, "Collected Twice"), (50, "Fail"),
                     (51, "In Play"), (52, "In Play Danger"), (53, "In Play Safe"), (55, "No Touch"),
                     (56, "Saved Twice"), (58, "Touched In"), (59, "Touched Out"), (74, "Injury Clearance"),
                     (75, "Out"), (76, "Pass Offside"), (77, "Unknown"), (96, "Blocked"), (97, "Goal"), (98, "Off T"),
                     (99, "Post"), (100, "Saved"), (101, "Wayward"), (102, "Injury"), (103, "Tactical"), (108, "Won"),
                     (109, "Lost"), (115, "Saved Off T"), (116, "Saved To Post"), (117, "Punched Out"),
                     (147, "Success To Team"), (148, "Success to Opposition")]

    for pair in outcome_pairs:
        cursor.execute("""
                INSERT INTO event_outcome (outcome_id, outcome_name)
                VALUES (%s, %s)
                """, pair)


def create_event_type(cursor):
    cursor.execute("create table event_type (type_id smallint, type_name varchar(17), primary key (type_id))")


def load_event_type(cursor):
    type_pairs = [(2, "Ball Recovery"), (3, "Dispossessed"), (4, "Duel"), (5, "Camera On*"), (6, "Block"),
                  (8, "Offside"), (9, "Clearance"), (10, "Interception"), (14, "Dribble"), (16, "Shot"),
                  (17, "Pressure"), (18, "Half Start"), (19, "Substitution"), (20, "Own Goal Against"),
                  (21, "Foul Won"), (22, "Foul Committed"), (23, "Goal Keeper"), (24, "Bad Behaviour"),
                  (25, "Own Goal For"), (26, "Player On"), (27, "Player Off"), (28, "Shield"), (30, "Pass"),
                  (33, "50/50"), (34, "Half End"), (35, "Starting XI"), (36, "Tactical Shift"), (37, "Error"),
                  (38, "Miscontrol"), (39, "Dribbled Past"), (40, "Injury Stoppage"), (41, "Referee Ball-Drop"),
                  (42, "Ball Receipt*"), (43, "Carry")]
    for pair in type_pairs:
        cursor.execute("""
                        INSERT INTO event_type (type_id, type_name) 
                        VALUES (%s, %s)
                        """, pair)


def create_event_extra_type(cursor):
    cursor.execute(
        "create table event_extra_type (extra_type_id smallint, extra_type_name varchar(21), primary key (extra_type_id))")


def load_event_extra_type(cursor):
    type_pairs = [(10, "Aerial Lost"), (11, "Tackle"), (19, "6 Seconds"), (20, "Backpass Pick"), (21, "Dangerous Play"),
                  (22, "Dive"), (23, "Foul Out"), (24, "Handball"), (25, "Collected"),(26, "Goal Conceded"),
                  (27, "Keeper Sweeper"), (28, "Penalty Conceded"), (29, "Penalty Saved"), (30, "Punch"), (31, "Save"),
                  (32, "Shot Faced"), (33, "Shot Saved"), (34, "Smother"), (61, "Corner"), (62, "Free Kick"),
                  (63, "Goal Kick"), (64, "Interception"), (65, "Kick Off"), (66, "Recovery"), (67, "Throw-in"),
                  (87, "Open Play"), (88, "Penalty"), (109, "Penalty Saved To Post"), (110, "Saved To Post"),
                  (113, "Shot Saved Off T"), (114, "Shot Saved To Post")]
    for pair in type_pairs:
        cursor.execute("""
                        INSERT INTO event_extra_type (extra_type_id, extra_type_name) 
                        VALUES (%s, %s)
                        """, pair)


def create_event_body_part(cursor):
    cursor.execute(
        "create table event_body_part (body_part_id smallint, body_part_name varchar(10), primary key (body_part_id))")


def load_event_body_part(cursor):
    part_pairs = [(35, "Both Hands"), (36, "Chest"), (37, "Head"), (38, "Left Foot"),(39, "Left Hand"),
                  (40, "Right Foot"), (41, "Right Hand"), (68, "Drop Kick"), (69, "Keeper Arm"), (70, "Other"),
                  (106, "No Touch")]
    for pair in part_pairs:
        cursor.execute("""
                        INSERT INTO event_body_part (body_part_id, body_part_name) 
                        VALUES (%s, %s)
                        """, pair)


def create_event_technique(cursor):
    cursor.execute(
        "create table event_technique (technique_id smallint, technique_name varchar(13), primary key (technique_id))")


def load_event_technique(cursor):
    technique_pairs = [(45, "Diving"), (46, "Standing"), (89, "Backheel"), (90, "Diving Header"), (91, "Half Volley"),
                       (92, "Lob"), (93, "Normal"), (94, "Overhead Kick"), (95, "Volley"), (104, "Inswinging"),
                       (105, "Outswinging"), (107, "Straight"), (108, "Through Ball")]
    for pair in technique_pairs:
        cursor.execute("""
                        INSERT INTO event_technique (technique_id, technique_name) 
                        VALUES (%s, %s)
                        """, pair)


def create_event_card(cursor):
    cursor.execute(
        "create table event_card (card_id smallint, card_name varchar(13), primary key (card_id))")


def load_event_card(cursor):
    card_pairs = [(5, "Yellow Card"), (6, "Second Yellow"), (7, "Red Card"), (65, "Yellow Card"), (66, "Second Yellow"),
                  (67, "Red Card")]
    for pair in card_pairs:
        cursor.execute("""
                        INSERT INTO event_card (card_id, card_name) 
                        VALUES (%s, %s)
                        """, pair)


def create_event_extra_position(cursor):
    cursor.execute(
        "create table event_extra_position (extra_position_id smallint, extra_position_name varchar(6), primary key (extra_position_id))")


def load_event_extra_position(cursor):
    position_pairs = [(42, "Moving"), (43, "Prone"), (44, "Set")]
    for pair in position_pairs:
        cursor.execute("""
                        INSERT INTO event_extra_position (extra_position_id, extra_position_name) 
                        VALUES (%s, %s)
                        """, pair)


def create_event_height(cursor):
    cursor.execute(
        "create table event_height (height_id smallint, height_name varchar(11), primary key (height_id))")


def load_event_height(cursor):
    position_pairs = [(1, "Ground Pass"), (2, "Low Pass"), (3, "High Pass")]
    for pair in position_pairs:
        cursor.execute("""
                        INSERT INTO event_height (height_id, height_name) 
                        VALUES (%s, %s)
                        """, pair)


#def load_event_player(cursor):
#    with open('event_player.csv', encoding="utf-8") as csv_file:
#        csv_reader = csv.reader(csv_file, delimiter=',')
#        first_line = True
#        for row in csv_reader:
#            if first_line:
#                first_line = False
#            else:
#                add_event_player(cursor, row[0], row[1])

#def load_event_team(cursor):
#    with open('event_team.csv', encoding="utf-8") as csv_file:
#        csv_reader = csv.reader(csv_file, delimiter=',')
#        first_line = True
#        for row in csv_reader:
#            if first_line:
#                first_line = False
#            else:
#                add_event_team(cursor, row[0], row[1])


def create_competition_name(cursor):
    cursor.execute(
        "create table competition_name (competition_id smallint, competition_name varchar(15), primary key (competition_id))")


def load_competition_name(cursor):
    position_pairs = [(11, "La Liga"), (2, "Premier League")]
    for pair in position_pairs:
        cursor.execute("""
                        INSERT INTO competition_name (competition_id, competition_name) 
                        VALUES (%s, %s)
                        """, pair)


def create_season_name(cursor):
    cursor.execute(
        "create table season_name (season_id smallint, season_name varchar(9), primary key (season_id))")


def load_season_name(cursor):
    position_pairs = [(44, "2003/2004"), (4, "2018/2019"), (42, "2019/2020"), (90, "2020/2021")]
    for pair in position_pairs:
        cursor.execute("""
                        INSERT INTO season_name (season_id, season_name) 
                        VALUES (%s, %s)
                        """, pair)
