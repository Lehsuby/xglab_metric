from enum import auto
from strenum import StrEnum


class EventType(StrEnum):
    Pass = auto()
    Shot = auto()
    Card = auto()
    Claim = auto()
    KeeperSweeper = auto()
    KeeperPickup = auto()
    Smother = auto()
    GoodSkill = auto()
    BlockOfPass = auto()
    OffsideProvoked = auto()
    ShieldBall = auto()
    Error = auto()
    Dispossessed = auto()
    Interception = auto()
    BallRecovery = auto()
    Aerial = auto()
    Tackle = auto()
    OwnGoal = auto()
    Foul = auto()
    FoulProvoked = auto()
    ChanceMissed = auto()
    End = auto()
    Start = auto()
    KeeperThrow = auto()
    CornerProvoked = auto()
    LedToOppCorner = auto()
    SubstitutionOn = auto()
    SubstitutionOff = auto()
    BallTouch = auto()
    Clearance = auto()
    Punch = auto()
    TakeOn = auto()
    Save = auto()
    FormationSet = auto()
    FormationChange = auto()
    BallCarry = auto()
    PenaltyFaced = auto()


class PassType(StrEnum):
    OpenPlay = auto()
    Corner = auto()
    GoalKick = auto()
    FreeKick = auto()
    ThrowIn = auto()


class PassDestination(StrEnum):
    Offside = auto()
    Out = auto()


class Period(StrEnum):
    PreMatch = auto()
    FirstHalf = auto()
    SecondHalf = auto()
    FirstPeriodOfExtraTime = auto()
    SecondPeriodOfExtraTime = auto()
    PenaltyShootout = auto()
    PostGame = auto()


class DetailedPositionName(StrEnum):
    GK = auto()
    LB = auto()
    LWB = auto()
    RB = auto()
    RWB = auto()
    LCB3 = auto()
    CB3 = auto()
    RCB3 = auto()
    LCB2 = auto()
    RCB2 = auto()
    CDM = auto()
    LCM2 = auto()
    RCM2 = auto()
    LCM3 = auto()
    CM3 = auto()
    RCM3 = auto()
    LCAM = auto()
    CAM = auto()
    RCAM = auto()
    LM = auto()
    RM = auto()
    LW = auto()
    RW = auto()
    FW1 = auto()
    LFW2 = auto()
    RFW2 = auto()


class GeneralPositionName(StrEnum):
    GK = auto()
    RB = auto()
    LB = auto()
    CB = auto()
    CM = auto()
    RM = auto()
    LM = auto()
    CAM = auto()
    FW = auto()


class BodyPart(StrEnum):
    LeftFoot = auto()
    RightFoot = auto()
    Feet = auto()
    Head = auto()
    Hands = auto()
    Other = auto()


class SaveType(StrEnum):
    Diving = auto()
    Standing = auto()
    JumpRight = auto()
    JumpLeft = auto()


class ShotResult(StrEnum):
    Missed = auto()
    Goal = auto()
    Saved = auto()
    OnPost = auto()


class ErrorResult(StrEnum):
    Goal = auto()
    Attempt = auto()


class CardType(StrEnum):
    Yellow = auto()
    SecondYellow = auto()
    Red = auto()


class CardReason(StrEnum):
    Foul = auto()
    Other = auto()


class FoulType(StrEnum):
    Ground = auto()
    Aerial = auto()


class ShotType(StrEnum):
    RegularPlay = auto()
    FromCorner = auto()
    SetPiece = auto()
    DirectFreekick = auto()
    FastBreak = auto()
    ThrowinSetPiece = auto()
    Penalty = auto()


class SaveResult(StrEnum):
    ParriedSafe = auto()
    ParriedDanger = auto()
    Collected = auto()
    OutfielderBlock = auto()


class FormationName(StrEnum):
    _343 = '343'
    _352 = '352'
    _433 = '433'
    _442 = '442'
    _451 = '451'
    _532 = '532'
    _541 = '541'
    _3142 = '3142'
    _3241 = '3241'
    _3331 = '3331'
    _3412 = '3412'
    _3421 = '3421'
    _3511 = '3511'
    _4132 = '4132'
    _4141 = '4141'
    _4222 = '4222'
    _4231 = '4231'
    _4240 = '4240'
    _4312 = '4312'
    _4321 = '4321'
    _4411 = '4411'
    _31312 = '31312'
    _41212 = '41212'
    _343d = '343d'
