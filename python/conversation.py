import bot

class Conversation():
	currentSpeaker = 0
	terminated = False
	def __init__( self , id , startingText ):
		self.id				= id
		self.history 		= [ startingText ]
		self.gettableHistory= [ startingText ]
		self.participants 	= [
			bot.botFactory.create( bot.ChatterBotType.JABBERWACKY ).create_session(),
			bot.botFactory.create( bot.ChatterBotType.JABBERWACKY ).create_session()
		]

	def _generateNextSpeech( self ):
		text 	= self.history[ len( self.history ) - 1 ]
		ret 	= self.participants[ self.currentSpeaker ].think( text )
		self.currentSpeaker += 1

		if self.currentSpeaker > 1:
			self.currentSpeaker = 0
		self.history.append( ret )
		self.gettableHistory.append( ret )

	def newTopic( self , text ):
		del self.history[:]
		del self.gettableHistory[:]
		self.history = [ text ]
		self.gettableHistory= [ text ]

	def _getLastSpeech( self ):
		return self.gettableHistory.pop( 0 ) if len( self.gettableHistory ) > 0 else ''

	def getHistory( self ):
		ret = ''
		for i in range( len( self.history ) ):
			ret += self.history[ i ] + "<br>"
		return ret

