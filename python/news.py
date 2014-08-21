import twitter
import random

channels = {
	"indiegamescom" : []#,
	#"indiePub" : [],
	#"game_snack" : [],
	#"polytron": [],
	#"indiegamemovie": [],
	#"iggmarathon": [],
	#"figames": [],
	#"tha_rami": []
}

def fillChannels(): # get top 20 news from each channel
	global channels
	channels = {key: twitter.getTimeLineTexts(key) for (key, value) in channels.iteritems()}

def findChannel(): # choose one of those upper channels
	nec = {}
	for c in channels:
		if len( channels[ c ] ) != 0:
			nec[ c ] = channels[ c ]

	if( len( nec.keys() ) == 0 ):
		return None
	else:
		chans = nec.keys()
		return nec[ random.choice( chans ) ]

def findText():
	channel = findChannel()
	if( channel == None ): return "Well, its nothing to discuss"
	text = random.choice( channel )
	channel.remove( text )

	return text
	