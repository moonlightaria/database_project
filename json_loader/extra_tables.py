from data_extra_objects import *

def create_extra_tables(cursor):
    create_ball_recovery(cursor)
    create_duel(cursor)
    create_block(cursor)
    create_clearance(cursor)
    create_interception(cursor)
    create_dribble(cursor)
    create_shot(cursor)
    create_freeze_frame(cursor)
    create_pressure(cursor)
    create_half_start(cursor)
    create_half_end(cursor)
    create_substitution(cursor)
    create_foul_won(cursor)
    create_foul_committed(cursor)
    create_goal_keeper(cursor)
    create_pass(cursor)
    create_bad_behavior(cursor)
    create_player_off(cursor)
    create_fifty_fifty(cursor)
    create_miscontrol(cursor)
    create_injury_stoppage(cursor)
    create_ball_receipt(cursor)
    create_carry(cursor)


def add_extra_event_data(cursor, event_id, event_extra_data):
    if isinstance(event_extra_data, BallRecovery):
        add_ball_recovery(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Duel):
        add_duel(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Block):
        add_block(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Clearance):
        add_clearance(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Interception):
        add_interception(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Dribble):
        add_dribble(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Shot):
        add_shot(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Pressure):
        add_pressure(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, HalfStart):
        add_half_start(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, HalfEnd):
        add_half_end(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Substitution):
        add_substitution(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, FoulWon):
        add_foul_won(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, FoulCommitted):
        add_foul_committed(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, GoalKeeper):
        add_goal_keeper(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Pass):
        add_pass(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, BadBehavior):
        add_bad_behavior(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, PlayerOff):
        add_player_off(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, FiftyFifty):
        add_fifty_fifty(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Miscontrol):
        add_miscontrol(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, InjuryStoppage):
        add_injury_stoppage(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, BallReceipt):
        add_ball_receipt(cursor, event_id, event_extra_data)
    elif isinstance(event_extra_data, Carry):
        add_carry(cursor, event_id, event_extra_data)

def create_carry(cursor):
    cursor.execute("""
        create table event_carry (event_id uuid, carry_x float, carry_y float,
		primary key (event_id), foreign key (event_id) references event);""")


def add_carry(cursor, event_id: str, carry: Carry):
    cursor.execute("""
                    INSERT INTO event_carry (event_id, carry_x, carry_y) 
                    VALUES (%s, %s, %s);
                    """, [event_id, carry.carry_x, carry.carry_y])

def create_ball_receipt(cursor):
    cursor.execute("""
        create table event_ball_receipt (event_id uuid, outcome_id smallint,
		primary key (event_id), foreign key (event_id) references event, foreign key (outcome_id) references event_outcome);""")


def add_ball_receipt(cursor, event_id: str, ball_receipt: BallReceipt):
    cursor.execute("""
                    INSERT INTO event_ball_receipt (event_id, outcome_id) 
                    VALUES (%s, %s);
                    """, [event_id, ball_receipt.outcome])

def create_injury_stoppage(cursor):
    cursor.execute("""
        create table event_injury_stoppage (event_id uuid, in_chain bool,
		primary key (event_id), foreign key (event_id) references event);""")


def add_injury_stoppage(cursor, event_id: str, injury_stoppage: InjuryStoppage):
    cursor.execute("""
                    INSERT INTO event_injury_stoppage (event_id, in_chain) 
                    VALUES (%s, %s);
                    """, [event_id, injury_stoppage.in_chain])


def create_dribbled_past(cursor):
    cursor.execute("""
        create table event_dribbled_past (event_id uuid, counterpress bool,
		primary key (event_id), foreign key (event_id) references event);""")


def add_dribbled_past(cursor, event_id: str, dribbled_past: DribbledPast):
    cursor.execute("""
                    INSERT INTO event_dribbled_past (event_id, counterpress) 
                    VALUES (%s, %s);
                    """, [event_id, dribbled_past.counterpress])


def create_miscontrol(cursor):
    cursor.execute("""
        create table event_miscontrol (event_id uuid, aerial_won bool,
		primary key (event_id), foreign key (event_id) references event);""")


def add_miscontrol(cursor, event_id: str, miscontrol: Miscontrol):
    cursor.execute("""
                    INSERT INTO event_miscontrol (event_id, aerial_won) 
                    VALUES (%s, %s);
                    """, [event_id, miscontrol.aerial_won])

def create_fifty_fifty(cursor):
    cursor.execute("""
         create table event_fifty_fifty (event_id uuid, counterpress bool, outcome_id smallint,
 		primary key (event_id), foreign key (event_id) references event, foreign key (outcome_id) references event_outcome);""")


def add_fifty_fifty(cursor, event_id: str, fifty_fifty: FiftyFifty):
    cursor.execute("""
                     INSERT INTO event_fifty_fifty (event_id, counterpress, outcome_id) 
                     VALUES (%s, %s, %s);
                     """, [event_id, fifty_fifty.counterpress, fifty_fifty.outcome])

def create_player_off(cursor):
    cursor.execute("""
        create table event_player_off (event_id uuid, permanent bool,
		primary key (event_id), foreign key (event_id) references event);""")


def add_player_off(cursor, event_id: str, player_off: PlayerOff):
    cursor.execute("""
                    INSERT INTO event_player_off (event_id, permanent) 
                    VALUES (%s, %s);
                    """, [event_id, player_off.permanent])
def create_bad_behavior(cursor):
    cursor.execute("""
        create table event_bad_behavior (event_id uuid, card_id smallint,
		primary key (event_id), foreign key (event_id) references event, foreign key (card_id) references event_card);""")


def add_bad_behavior(cursor, event_id: str, bad_behavior: BadBehavior):
    cursor.execute("""
                    INSERT INTO event_bad_behavior (event_id, card_id) 
                    VALUES (%s, %s);
                    """, [event_id, bad_behavior.card])


def create_pass(cursor):
    cursor.execute("""
        create table event_pass (event_id uuid, length float, angle float, assisted_shot_id uuid, 
        backheel bool, deflected bool, miscommunication bool, cross_pass bool, cut_back bool, switch bool, shot_assist bool, 
        goal_assist bool, recipient_id int, height_id smallint, body_part_id smallint, type_id smallint, 
        outcome_id smallint, technique_id smallint, end_location_x smallint, end_location_y smallint,
		primary key (event_id), foreign key (event_id) references event, foreign key (assisted_shot_id) references event,
		foreign key (recipient_id) references event_player, foreign key (height_id) references event_height,
		foreign key (body_part_id) references event_body_part, foreign key (type_id) references event_extra_type,
		foreign key (outcome_id) references event_outcome, foreign key (technique_id) references event_technique);""")


def add_pass(cursor, event_id: str, pass_obj: Pass):
    cursor.execute("""
                    INSERT INTO event_pass (event_id, length, angle, assisted_shot_id, backheel, deflected, 
                    miscommunication, cross_pass, cut_back, switch, shot_assist, goal_assist, recipient_id, height_id, 
                    body_part_id, type_id, outcome_id, technique_id, end_location_x, end_location_y) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                    """, [event_id, pass_obj.length, pass_obj.angle, pass_obj.assisted_shot_id, pass_obj.backheel,
                          pass_obj.deflected, pass_obj.miscommunication, pass_obj.cross, pass_obj.cross,
                          pass_obj.switch, pass_obj.shot_assist, pass_obj.goal_assist, pass_obj.recipient,
                          pass_obj.height, pass_obj.body_part, pass_obj.type, pass_obj.outcome, pass_obj.technique,
                          pass_obj.end_location_x, pass_obj.end_location_y])


def create_goal_keeper(cursor):
    cursor.execute("""
        create table event_goal_keeper (event_id uuid, position_id smallint, technique_id smallint, 
        body_part_id smallint, type_id smallint, outcome_id smallint,
		primary key (event_id), foreign key (event_id) references event, foreign key (position_id) references event_extra_position,
		foreign key (technique_id) references event_technique, foreign key (body_part_id) references event_body_part,
		foreign key (type_id) references event_extra_type, foreign key (outcome_id) references event_outcome);""")


def add_goal_keeper(cursor, event_id: str, goal_keeper: GoalKeeper):
    cursor.execute("""
                    INSERT INTO event_goal_keeper (event_id, position_id, technique_id, body_part_id, type_id, outcome_id) 
                    VALUES (%s, %s, %s, %s, %s, %s);
                    """, [event_id, goal_keeper.position, goal_keeper.technique, goal_keeper.body_part, goal_keeper.type,
                          goal_keeper.outcome])
def create_foul_committed(cursor):
    cursor.execute("""
        create table event_foul_committed (event_id uuid, counterpress bool, offensive bool, advantage bool, 
        penalty bool, type_id smallint, card_id smallint,
		primary key (event_id), foreign key (event_id) references event, foreign key (type_id) references event_extra_type,
		foreign key (card_id) references event_card);""")


def add_foul_committed(cursor, event_id: str, foul_committed: FoulCommitted):
    cursor.execute("""
                    INSERT INTO event_foul_committed (event_id, counterpress, offensive, advantage, penalty, type_id, card_id) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """, [event_id, foul_committed.counterpress, foul_committed.offensive, foul_committed.advantage,
                          foul_committed.penalty, foul_committed.type, foul_committed.card])
def create_foul_won(cursor):
    cursor.execute("""
        create table event_foul_won (event_id uuid, defensive bool, advantage bool, penalty bool,
		primary key (event_id), foreign key (event_id) references event);""")


def add_foul_won(cursor, event_id: str, foul_won: FoulWon):
    cursor.execute("""
                    INSERT INTO event_foul_won (event_id, defensive, advantage, penalty) 
                    VALUES (%s, %s, %s, %s);
                    """, [event_id, foul_won.defensive, foul_won.advantage, foul_won.penalty])


def create_substitution(cursor):
    cursor.execute("""
        create table event_substitution (event_id uuid, replacement_id int, outcome_id smallint,
		primary key (event_id), foreign key (event_id) references event, foreign key (replacement_id) references event_player,
		foreign key (outcome_id) references event_outcome);""")


def add_substitution(cursor, event_id: str, substitution: Substitution):
    cursor.execute("""
                    INSERT INTO event_substitution (event_id, replacement_id, outcome_id) 
                    VALUES (%s, %s, %s);
                    """, [event_id, substitution.replacement, substitution.outcome])

def create_half_end(cursor):
    cursor.execute("""
        create table event_half_end (event_id uuid, early_video_end bool, match_suspended bool,
		primary key (event_id), foreign key (event_id) references event);""")


def add_half_end(cursor, event_id: str, half_end: HalfEnd):
    cursor.execute("""
                    INSERT INTO event_half_end (event_id, early_video_end, match_suspended) 
                    VALUES (%s, %s, %s);
                    """, [event_id, half_end.early_video_end, half_end.match_suspended])

def create_half_start(cursor):
    cursor.execute("""
        create table event_half_start (event_id uuid, late_video_start bool,
		primary key (event_id), foreign key (event_id) references event);""")


def add_half_start(cursor, event_id: str, half_start: HalfStart):
    cursor.execute("""
                    INSERT INTO event_half_start (event_id, late_video_start) 
                    VALUES (%s, %s);
                    """, [event_id, half_start.late_video_start])
def create_pressure(cursor):
    cursor.execute("""
        create table event_pressure (event_id uuid, counterpress bool,
		primary key (event_id), foreign key (event_id) references event);""")


def add_pressure(cursor, event_id: str, pressure: Pressure):
    cursor.execute("""
                    INSERT INTO event_pressure(event_id, counterpress) 
                    VALUES (%s, %s);
                    """, [event_id, pressure.counterpress])
def create_freeze_frame(cursor):
    cursor.execute("""
        create table event_freeze_frame (id serial, shot_id uuid, loc_x smallint, loc_y smallint, player_id int, position_id smallint, teammate bool,
		primary key (id), foreign key (shot_id) references event, foreign key (player_id) references event_player,
		foreign key (position_id) references event_position);""")


def add_freeze_frame(cursor, id: int, frame: FreezeFrame):
    cursor.execute("""
                    INSERT INTO event_freeze_frame (shot_id, loc_x, loc_y, player_id, position_id, teammate) 
                    VALUES (%s, %s, %s, %s, %s, %s);
                    """, [id, frame.x, frame.y, frame.player, frame.position, frame.teammate])

def create_shot(cursor):
    cursor.execute("""
        create table event_shot (event_id uuid, key_pass_id uuid, end_location_x float, end_location_y float,
        end_location_z float, aerial_won bool, follows_dribble bool, first_time bool, open_goal bool, statsbomb_xg float,
        deflected bool, technique_id smallint, body_part_id smallint, type_id smallint, outcome_id smallint,
		primary key (event_id), foreign key (event_id) references event, foreign key (key_pass_id) references event,
		foreign key (technique_id) references event_technique, foreign key (body_part_id) references event_body_part,
		foreign key (type_id) references event_extra_type, foreign key (outcome_id) references event_outcome);""")


def add_shot(cursor, event_id: str, shot: Shot):
    cursor.execute("""
                    INSERT INTO event_shot (event_id, key_pass_id, end_location_x , end_location_y, end_location_z, 
                    aerial_won, follows_dribble, first_time, open_goal, statsbomb_xg, deflected, technique_id, 
                    body_part_id, type_id, outcome_id) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) returning event_id;
                    """, [event_id, shot.key_pass_id, shot.end_location_x, shot.end_location_y, shot.end_location_z,
                          shot.aerial_won, shot.follows_dribble, shot.first_time, shot.open_goal, shot.statsbomb_xg,
                          shot.deflected, shot.technique, shot.body_part, shot.type, shot.outcome])
    id = cursor.fetchone()[0]
    for frame in shot.freeze_frame:
        add_freeze_frame(cursor, id, frame)

def create_dribble(cursor):
    cursor.execute("""
        create table event_dribble (event_id uuid, overrun bool, nutmeg bool, outcome_id smallint, no_touch bool,
		primary key (event_id), foreign key (event_id) references event, foreign key (outcome_id) references event_outcome);""")


def add_dribble(cursor, event_id: str, dribble: Dribble):
    cursor.execute("""
                    INSERT INTO event_dribble (event_id, overrun, nutmeg, outcome_id, no_touch) 
                    VALUES (%s, %s, %s, %s, %s);
                    """, [event_id, dribble.overrun, dribble.nutmeg, dribble.outcome, dribble.no_touch])


def create_interception(cursor):
    cursor.execute("""
        create table event_interception (event_id uuid, outcome_id smallint,
		primary key (event_id), foreign key (event_id) references event, foreign key (outcome_id) references event_outcome);""")


def add_interception(cursor, event_id: str, interception: Interception):
    cursor.execute("""
                    INSERT INTO event_interception (event_id, outcome_id) 
                    VALUES (%s, %s);
                    """, [event_id, interception.outcome])


def create_clearance(cursor):
    cursor.execute("""
        create table event_clearance (event_id uuid, aerial_won bool, body_part_id smallint,
		primary key (event_id), foreign key (event_id) references event, foreign key (body_part_id) references event_body_part);""")


def add_clearance(cursor, event_id: str, clearance: Clearance):
    cursor.execute("""
                    INSERT INTO event_clearance (event_id, aerial_won, body_part_id) 
                    VALUES (%s, %s, %s);
                    """, [event_id, clearance.aerial_won, clearance.body_part])


def create_block(cursor):
    cursor.execute("""
        create table event_block (event_id uuid, counterpress bool, deflection bool, offensive bool,
        save_block bool, primary key (event_id), foreign key (event_id) references event);""")


def add_block(cursor, event_id: str, block: Block):
    cursor.execute("""
                    INSERT INTO event_block (event_id, counterpress, deflection, offensive, save_block) 
                    VALUES (%s, %s, %s, %s, %s);
                    """, [event_id, block.counterpress, block.deflection, block.offensive, block.save_block])


def create_ball_recovery(cursor):
    cursor.execute("""
        create table event_ball_recovery (event_id uuid, offensive bool, recovery_failure bool,
        primary key (event_id), foreign key (event_id) references event);""")


def add_ball_recovery(cursor, event_id: str, ball_recovery: BallRecovery):
    cursor.execute("""
                    INSERT INTO event_ball_recovery (event_id, offensive, recovery_failure) 
                    VALUES (%s, %s, %s);
                    """, [event_id, ball_recovery.offensive, ball_recovery.recovery_failure])


def create_duel(cursor):
    cursor.execute("""
        create table event_duel (event_id uuid, counterpress bool, type_id smallint, outcome_id smallint,
        primary key (event_id), foreign key (event_id) references event, foreign key (type_id) references event_extra_type,
        foreign key (outcome_id) references event_outcome);""")


def add_duel(cursor, event_id: str, duel: Duel):
    cursor.execute("""
                    INSERT INTO event_duel (event_id, counterpress, type_id, outcome_id) 
                    VALUES (%s, %s, %s, %s);
                    """, [event_id, duel.counterpress, duel.type, duel.outcome])
