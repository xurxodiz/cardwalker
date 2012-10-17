from pyparsing import *

from decl import *

from ...constants.punctuation.deff import COMMA
from ...constants.verbs.deff import ENTER, LEAVE, DIE, GAIN, DRAW, LOSE, ATTACK
from ...constants.connectors.deff import WHEN, WHENEVER
from ...constants.resources.deff import LIFE
from ...constants.modifiers.deff import ALONE
from ...entities.people.deff import undercontrol, peoplecontrol
from ...entities.objects.deff import objects
from ...entities.subjects.deff import subject
from ...entities.zones.deff import zone
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

trigger << (
		enterzone
		| leavezone
		| die
		| gainlife
		| drawcards
		| loselife
		| attackalone
		| controlobjects
)

when_trigger << (WHEN|WHENEVER) + subject + trigger
at_trigger << Empty()
trigger << (when_trigger|at_trigger)

intervif << Literal("FILLER")

trigger_clause << trigger + Optional(COMMA + intervif)

triggered << trigger_clause + COMMA + (oneshot|continuous)