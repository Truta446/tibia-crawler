from dataclasses import dataclass

@dataclass
class Tibia:
    name: str
    title: str
    sex: str
    vocation: str
    level: str
    achivement: str
    world: str
    residence: str
    guild_membership: str
    last_login: str
    account_status: str
    deaths: dict