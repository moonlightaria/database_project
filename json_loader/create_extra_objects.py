from object_helpers import *
from data_extra_objects import *


def create_ball_recovery(event) -> BallRecovery:
    return BallRecovery(get_nested_value(event, "ball_recovery", "offensive"),
                        get_nested_value(event, "ball_recovery", "recovery_failure"))


def create_duel(event) -> Duel:
    return Duel(event.get("counterpress"), get_nested_value2(event, "duel", "type", "id"),
                get_nested_value2(event, "duel", "outcome", "id"))


def create_block(event) -> Block:
    return Block(event.get("counterpress"), get_nested_value(event, "block", "deflection"),
                 get_nested_value(event, "block", "offensive"),
                 get_nested_value(event, "block", "save_block"))


def create_clearance(event) -> Clearance:
    return Clearance(get_nested_value(event, "clearance", "aerial_won"),
                     get_nested_value2(event, "clearance", "body_part", "id"))


def create_interception(event) -> Interception:
    return Interception(get_nested_value2(event, "interception", "outcome", "id"))


def create_dribble(event) -> Dribble:
    return Dribble(get_nested_value(event, "dribble", "overrun"),
                   get_nested_value(event, "dribble", "nutmeg"),
                   get_nested_value2(event, "dribble", "outcome", "id"),
                   get_nested_value(event, "dribble", "no_touch"))


def create_freeze_frame(framedata) -> FreezeFrame:
    return FreezeFrame(framedata["location"][0], framedata["location"][1], framedata["player"]["id"],
                       framedata["position"]["id"], framedata["teammate"])


def create_shot(event) -> Shot:
    end_loc = get_nested_value(event, "shot", "end_location")
    if end_loc is None:
        end_loc = [None, None, None]
    elif len(end_loc) < 3:
        end_loc.append(None)

    freeze_frame_data = get_nested_value(event, "shot", "freeze_frame")
    freeze_frame = []
    if freeze_frame_data is not None:
        for data in freeze_frame_data:
            freeze_frame.append(create_freeze_frame(data))

    return Shot(get_nested_value(event, "shot", "key_pass_id"),
                end_loc[0], end_loc[1], end_loc[2],
                get_nested_value(event, "shot", "aerial_won"),
                get_nested_value(event, "shot", "follows_dribble"),
                get_nested_value(event, "shot", "first_time"),
                get_nested_value(event, "shot", "open_goal"),
                get_nested_value(event, "shot", "statsbomb_xg"),
                get_nested_value(event, "shot", "deflected"),
                get_nested_value2(event, "shot", "technique", "id"),
                get_nested_value2(event, "shot", "body_part", "id"),
                get_nested_value2(event, "shot", "type", "id"),
                get_nested_value2(event, "shot", "outcome", "id"),
                freeze_frame
                )


def create_pressure(event) -> Pressure:
    return Pressure(event.get("counterpress"))


def create_half_start(event) -> HalfStart:
    return HalfStart(get_nested_value(event, "half_start", "late_video_start"))


def create_substitution(event) -> Substitution:
    return Substitution(get_nested_value2(event, "substitution", "replacement", "id"),
                        get_nested_value2(event, "substitution", "outcome", "id"))


def create_foul_won(event) -> FoulWon:
    return FoulWon(get_nested_value(event, "foul_won", "defensive"),
                   get_nested_value(event, "foul_won", "advantage"),
                   get_nested_value(event, "foul_won", "penalty"))


def create_foul_committed(event) -> FoulCommitted:
    return FoulCommitted(event.get("counterpress"),
                         get_nested_value(event, "foul_committed", "offensive"),
                         get_nested_value(event, "foul_committed", "advantage"),
                         get_nested_value(event, "foul_committed", "penalty"),
                         get_nested_value2(event, "foul_committed", "type", "id"),
                         get_nested_value2(event, "foul_committed", "card", "id"))


def create_goal_keeper(event) -> GoalKeeper:
    return GoalKeeper(get_nested_value2(event, "goalkeeper", "position", "id"),
                      get_nested_value2(event, "goalkeeper", "technique", "id"),
                      get_nested_value2(event, "goalkeeper", "body_part", "id"),
                      get_nested_value2(event, "goalkeeper", "type", "id"),
                      get_nested_value2(event, "goalkeeper", "outcome", "id"))


def create_bad_behavior(event) -> BadBehavior:
    return BadBehavior(get_nested_value2(event, "bad_behaviour", "card", "id"))


def create_player_off(event) -> PlayerOff:
    return PlayerOff(get_nested_value(event, "player_off", "permanent"))


def create_pass(event) -> Pass:
    location_x, location_y = get_nested_value(event, "pass", "end_location") or (None, None)
    return Pass(get_nested_value(event, "pass", "length"),
                get_nested_value(event, "pass", "angle"),
                get_nested_value(event, "pass", "assisted_shot_id"),
                get_nested_value(event, "pass", "backheel"),
                get_nested_value(event, "pass", "deflected"),
                get_nested_value(event, "pass", "miscommunication"),
                get_nested_value(event, "pass", "cross"),
                get_nested_value(event, "pass", "cut_back"),
                get_nested_value(event, "pass", "switch"),
                get_nested_value(event, "pass", "shot_assist"),
                get_nested_value(event, "pass", "goal_assist"),
                get_nested_value2(event, "pass", "recipient", "id"),
                get_nested_value2(event, "pass", "height", "id"),
                get_nested_value2(event, "pass", "body_part", "id"),
                get_nested_value2(event, "pass", "type", "id"),
                get_nested_value2(event, "pass", "outcome", "id"),
                get_nested_value2(event, "pass", "technique", "id"),
                location_x, location_y)


def create_fifty_fifty(event) -> FiftyFifty:
    return FiftyFifty(event.get("counterpress"),
                      get_nested_value2(event, "50_50", "outcome", "id"))


def create_half_end(event) -> HalfEnd:
    return HalfEnd(get_nested_value(event, "half_end", "early_video_end"),
                   get_nested_value(event, "half_end", "match_suspended"))


def create_miscontrol(event) -> Miscontrol:
    return Miscontrol(get_nested_value(event, "miscontrol", "aerial_won"))


def create_dribbled_past(event) -> DribbledPast:
    return DribbledPast(event.get("counterpress"))


def create_injury_stoppage(event) -> InjuryStoppage:
    return InjuryStoppage(get_nested_value(event, "injury_stoppage", "in_chain"))

def create_ball_receipt(event) -> BallReceipt:
    return BallReceipt(get_nested_value2(event, "ball_receipt", "outcome", "id"))


def create_carry(event) -> Carry:
    location_x, location_y = get_nested_value(event, "pass", "end_location") or (None, None)
    return Carry(location_x, location_y)
