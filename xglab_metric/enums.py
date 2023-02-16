from enum import Enum


class EventType(str, Enum):
    Pass = 'Pass'
    Shot = 'Shot'
    Card = 'Card'
    Claim = 'Claim'
    KeeperSweeper = 'KeeperSweeper'
    KeeperPickup = 'KeeperPickup'
    Smother = 'Smother'
    GoodSkill = 'GoodSkill'
    BlockOfPass = 'BlockOfPass'
    OffsideProvoked = 'OffsideProvoked'
    ShieldBall = 'ShieldBall'
    Error = 'Error'
    Dispossessed = 'Dispossessed'
    Interception = 'Interception'
    BallRecovery = 'BallRecovery'
    Aerial = 'Aerial'
    Tackle = 'Tackle'
    OwnGoal = 'OwnGoal'
    Foul = 'Foul'
    FoulProvoked = 'FoulProvoked'
    ChanceMissed = 'ChanceMissed'
    End = 'End'
    Start = 'Start'
    KeeperThrow = 'KeeperThrow'
    CornerProvoked = 'CornerProvoked'
    LedToOppCorner = 'LedToOppCorner'
    SubstitutionOn = 'SubstitutionOn'
    SubstitutionOff = 'SubstitutionOff'
    BallTouch = 'BallTouch'
    Clearance = 'Clearance'
    Punch = 'Punch'
    TakeOn = 'TakeOn'
    Save = 'Save'
    FormationSet = 'FormationSet'
    FormationChange = 'FormationChange'
    BallCarry = 'BallCarry'
    PenaltyFaced = 'PenaltyFaced'


class PassType(str, Enum):
    OpenPlay = 'OpenPlay',
    Corner = 'Corner',
    GoalKick = 'GoalKick',
    FreeKick = 'FreeKick',
    ThrowIn = 'ThrowIn'


class PassDestination(str, Enum):
    Offside = 'Offside',
    Out = 'Out'


class Period(str, Enum):
    PreMatch = 'PreMatch',
    FirstHalf = 'FirstHalf',
    SecondHalf = 'SecondHalf',
    FirstPeriodOfExtraTime = 'FirstPeriodOfExtraTime',
    SecondPeriodOfExtraTime = 'SecondPeriodOfExtraTime',
    PenaltyShootout = 'PenaltyShootout',
    PostGame = 'PostGame'


class DetailedPositionName(str, Enum):
    GK = 'GK'
    LB = 'LB'
    LWB = 'LWB'
    RB = 'RB'
    RWB = 'RWB'
    LCB3 = 'LCB3'
    CB3 = 'CB3'
    RCB3 = 'RCB3'
    LCB2 = 'LCB2'
    RCB2 = 'RCB2'
    CDM = 'CDM'
    LCM2 = 'LCM2'
    RCM2 = 'RCM2'
    LCM3 = 'LCM3'
    CM3 = 'CM3'
    RCM3 = 'RCM3'
    LCAM = 'LCAM'
    CAM = 'CAM'
    RCAM = 'RCAM'
    LM = 'LM'
    RM = 'RM'
    LW = 'LW'
    RW = 'RW'
    FW1 = 'FW1'
    LFW2 = 'LFW2'
    RFW2 = 'RFW2'


class GeneralPositionName(str, Enum):
    GK = 'GK'
    RB = 'RB'
    LB = 'LB'
    CB = 'CB'
    CM = 'CM'
    RM = 'RM'
    LM = 'LM'
    CAM = 'CAM'
    FW = 'FW'


class BodyPart(str, Enum):
    LeftFoot = 'LeftFoot'
    RightFoot = 'RightFoot'
    Feet = 'Feet'
    Head = 'Head'
    Hands = 'Hands'
    Other = 'Other'


class SaveType(str, Enum):
    Diving = 'Diving'
    Standing = 'Standing'
    JumpRight = 'JumpRight'
    JumpLeft = 'JumpLeft'


class ShotResult(str, Enum):
    Missed = 'Missed'
    Goal = 'Goal'
    Saved = 'Saved'
    OnPost = 'OnPost'


class ErrorResult(str, Enum):
    Goal = 'Goal'
    Attempt = 'Attempt'


class CardType(str, Enum):
    Yellow = 'Yellow'
    SecondYellow = 'SecondYellow'
    Red = 'Red'


class CardReason(str, Enum):
    Foul = 'Foul'
    Other = 'Other'


class FoulType(str, Enum):
    Ground = 'Ground'
    Aerial = 'Aerial'


class ShotType(str, Enum):
    RegularPlay = 'RegularPlay'
    FromCorner = 'FromCorner'
    SetPiece = 'SetPiece'
    DirectFreekick = 'DirectFreekick'
    FastBreak = 'FastBreak'
    ThrowinSetPiece = 'ThrowinSetPiece'
    Penalty = 'Penalty'


class SaveResult(str, Enum):
    ParriedSafe = 'ParriedSafe'
    ParriedDanger = 'ParriedDanger'
    Collected = 'Collected'
    OutfielderBlock = 'OutfielderBlock'


class FormationName(str, Enum):
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
