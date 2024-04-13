from dataclasses import dataclass


@dataclass
class BallRecovery:
    offensive: bool
    recovery_failure: bool


@dataclass
class Duel:
    counterpress: bool
    type: int
    outcome: int


@dataclass
class Block:
    counterpress: bool
    deflection: bool
    offensive: bool
    save_block: bool


@dataclass
class Clearance:
    aerial_won: bool
    body_part: int


@dataclass
class Interception:
    outcome: int


@dataclass
class Dribble:
    overrun: bool
    nutmeg: bool
    outcome: int
    no_touch: bool


@dataclass
class FreezeFrame:
    x: int
    y: int
    player: int
    position: int
    teammate: bool


@dataclass
class Shot:
    key_pass_id: str
    end_location_x: float
    end_location_y: float
    end_location_z: float
    aerial_won: bool
    follows_dribble: bool
    first_time: bool
    open_goal: bool
    statsbomb_xg: float
    deflected: bool
    technique: int
    body_part: int
    type: int
    outcome: int
    freeze_frame: [FreezeFrame]


@dataclass
class Pressure:
    counterpress: bool


@dataclass
class HalfStart:
    late_video_start: bool


@dataclass
class HalfEnd:
    early_video_end: bool
    match_suspended: bool


@dataclass
class Substitution:
    replacement: int
    outcome: int


@dataclass
class FoulWon:
    defensive: bool
    advantage: bool
    penalty: bool


@dataclass
class FoulCommitted:
    counterpress: bool
    offensive: bool
    advantage: bool
    penalty: bool
    type: int
    card: int


@dataclass
class GoalKeeper:
    position: int
    technique: int
    body_part: int
    type: int
    outcome: int


@dataclass
class Pass:
    length: float
    angle: float
    assisted_shot_id: str
    backheel: bool
    deflected: bool
    miscommunication: bool
    cross: bool
    cut_back: bool
    switch: bool
    shot_assist: bool
    goal_assist: bool
    recipient: int
    height: int
    body_part: id
    type: id
    outcome: id
    technique: id
    end_location_x: int
    end_location_y: int


@dataclass
class BadBehavior:
    card: int


@dataclass
class PlayerOff:
    permanent: bool


@dataclass
class FiftyFifty:
    counterpress: bool
    outcome: int


@dataclass
class Miscontrol:
    aerial_won: bool


@dataclass
class DribbledPast:
    counterpress: bool


@dataclass
class InjuryStoppage:
    in_chain: bool


@dataclass
class BallReceipt:
    outcome: int


@dataclass
class Carry:
    carry_x: float
    carry_y: float
