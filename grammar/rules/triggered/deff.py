from pyparsing import *

from decl import *

from ...constants.punctuation.deff import COMMA
from ...constants.verbs.deff import ENTER, LEAVE, DIE, GAIN, DRAW, LOSE, ATTACK
from ...constants.connectors.deff import WHEN, WHENEVER
from ...constants.resources.deff import LIFE
from ...constants.modifiers.deff import ALONE
from ...constants.timing.deff import TURN, UPKEEP, DRAWSTEP, PRECOMBAT, COMBAT, POSCOMBAT
from ...entities.people.deff import undercontrol, peoplecontrol
from ...entities.subjects.deff import objects
from ...entities.zones.deff import zone
from ...functions.deff import delimitedListAnd
from ..oneshot.deff import oneshot
from ..continuous.deff import continuous

enterzone << ENTER + zone + Optional(undercontrol)
leavezone << LEAVE + zone
die << DIE
gainlife << GAIN + LIFE
drawcards << DRAW + objects
loselife << LOSE + LIFE
attackalone << ATTACK + ALONE
controlobjects << peoplecontrol + objects


trigger_action << (
		enterzone
		| leavezone
		| die
		| gainlife
		| drawcards
		| loselife
		| attackalone
		| controlobjects
)

when_trigger << (WHEN|WHENEVER) + objects + trigger_action

turn << TURN
upkeep << UPKEEP
drawstep << DRAWSTEP
precombat << PRECOMBAT
combat << COMBAT
poscombat << POSCOMBAT

step << (turn|upkeep|drawstep|precombat|combat|poscombat)


# Implement at triggers
at_trigger << Empty()
trigger << (when_trigger|at_trigger)

# implement intervening if clauses
intervif << Empty()

trigger_clause << trigger #+ Optional(COMMA + intervif)

triggered << trigger_clause + COMMA + delimitedListAnd(oneshot|continuous)