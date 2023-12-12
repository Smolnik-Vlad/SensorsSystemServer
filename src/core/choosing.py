import enum


class ReactionChoose(str, enum.Enum):
    LOGGING = 'LOGGING'
    SIGNAL = 'SIGNAL'
    CALL = "CALL"
    SIREN = "SIREN"
    FIRE_SYSTEM = "FIRE_SYSTEM"


class EmergencyTelephoneNumber(str, enum.Enum):
    T_101 = "T_101"
    T_102 = "T_102"
    T_103 = "T_103"
    T_911 = "T_911"
