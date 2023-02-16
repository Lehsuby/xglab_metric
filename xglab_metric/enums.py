from enum import Enum


class EventType(str, Enum):
    pass_ = 'Pass'
    end = 'End'
    start = 'Start'
    foul = 'Foul'
    corner_awarded =  'CornerAwarded'
    penalty_faced = 'PenaltyFaced'
    goal = 'Goal'
    offside_pass = 'OffsidePass'
    offside_provoked = 'OffsideProvoked'
    offside_given = 'OffsideGiven'
    keeper_pickup = 'KeeperPickup'
    ball_recovery = 'BallRecovery'
    Card = 'Card'
    claim = 'Claim'
    keeper_sweeper = 'KeeperSweeper'
    smother = 'Smother'
    good_skill = 'GoodSkill'
    blocked_pass = 'BlockedPass'
    cross_not_claimed = 'CrossNotClaimed'
    shield_ball_opp = 'ShieldBallOpp'
    error = 'Error'
    dispossessed = 'Dispossessed'
    interception = 'Interception'
    aerial = 'Aerial'
    tackle = 'Tackle'
    challenge = 'Challenge'
    missed_shots = 'MissedShots'
    saved_shot = 'SavedShot'
    shot_on_post = 'ShotOnPost'
    chance_missed = 'ChanceMissed'
    substitution_on = 'SubstitutionOn'
    substitution_off = 'SubstitutionOff'
    ball_touch = 'BallTouch'
    clearance = 'Clearance'
    punch = 'Punch'
    take_on = 'TakeOn'
    save = 'Save'
    formation_set = 'FormationSet'
    formation_change = 'FormationChange'


class PassType(str, Enum):
    open_play = 'OpenPlay',
    corner = 'Corner',
    goal_kick = 'GoalKick',
    free_kick = 'FreeKick',
    throw_in = 'ThrowIn'


class PassDestination(str, Enum):
    pass


class Period(str, Enum):
    pass


class DetailedPositionName(str, Enum):
    pass


class GeneralPositionName(str, Enum):
    pass


class BodyPart(str, Enum):
    pass


class SaveType(str, Enum):
    pass


class ShotResult(str, Enum):
    pass


class ErrorResult(str, Enum):
    pass


class CardType(str, Enum):
    pass


class CardReason(str, Enum):
    pass


class FoulType(str, Enum):
    pass


class ShotType(str, Enum):
    pass


class SaveResult(str, Enum):
    pass


class FormationName(str, Enum):
    pass
