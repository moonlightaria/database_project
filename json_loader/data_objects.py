from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tactics:
    event_id: str
    id: int
    formation: int
    lineup: [(int, int, int)]


@dataclass
class Event:
    match_id: int
    event_id: str
    index: int
    period: int
    timestamp: str
    minute: int
    second: int
    type_id: int
    type_name: str
    possession: int
    possession_team_id: int
    possession_team_name: str
    play_pattern_id: int
    play_pattern_name: str
    team_id: int
    team_name: str
    player_id: int
    player_name: str
    position_id: int
    position_name: str
    location_x: int
    location_y: int
    duration: float
    under_pressure: bool
    off_camera: bool
    out: bool
    related_events: [str]
    tactics: Tactics
    extra_data: any

@dataclass
class Manager:
    id: int
    name: str
    nickname: str
    dob: str
    country_id: int
    country_name: str

@dataclass
class Team:
    team_id: int
    team_name: str
    team_gender: str
    team_group: str
    team_country_id: int
    team_country_name: str

@dataclass
class Player:
    id: int
    name: str
    nickname: str
    jersey: int
    country_id: int
    country_name: str

@dataclass
class Lineup:
    team_id: int
    team_name: str
    players: [Player]

@dataclass
class Match:
    id: int
    competition_id: int
    competition_name: str
    country_name: str
    season_id: int
    season_name: str
    match_date: str
    kickoff: str
    stadium_id: int
    stadium_name: str
    stadium_country_id: int
    stadium_country_name: str
    referee_id: int
    referee_name: str
    referee_country_id: int
    referee_country_name: str
    home_team: Team
    home_team_managers: [Manager]
    away_team: [Team]
    away_team_managers: [Manager]
    home_score: int
    away_score: int
    match_status: str
    match_week: int
    competition_stage_id: int
    competition_stage_name: str
    last_updated: str
    metadata: str
    lineups: [Lineup]
    events: [Event]


@dataclass
class Competition:
    competition_name: str
    season_name: str
    competition_id: int
    season_id: int
    gender: str
    youth: bool
    international: bool
    updated: str
    updated_360: str
    available_360: str
    available: str
    matches: [Match]
