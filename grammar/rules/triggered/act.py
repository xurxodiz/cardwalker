from ...functions.xml.deff import *

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