import enum


class ReactionChoose(str, enum.Enum):
    LOGGING = 'LOGGING'
    SIGNAL = 'SIGNAL'
    CALL = "CALL"
    SIREN = "SIREN"
    FIRE_SYSTEM = "FIRE_SYSTEM"


class EmergencyTelephoneNumber(str, enum.Enum):
    FIRE = "101"
    POLICE = "102"
    EMERGENCY = "103"
    COMMON = "911"
