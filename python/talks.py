import conversation as c
import news
import thread

#news.fillChannels()
currid = 0
conversationLimit = 4
convesations = []
requests = []
canRequest = True

def createConversation():
	global currid
	currid += 1

	conv = c.Conversation( currid , news.findText() )
	convesations.append( conv )
	thread.start_new_thread( checkRequests , () )

def nextSpeech():
	global canRequest
	text = convesations[ 0 ]._getLastSpeech()
	if text is '':
		if canRequest is True:
			requests.append( "nextSpeech" )
			
			canRequest = False

		return '*thinking*'
	else:
		canRequest = True
		return text

def checkRequestsIterator():
	if len( requests ) is 0: return True
	r = requests.pop( 0 )
	print r
	if r is "nextSpeech":
		convesations[ 0 ]._generateNextSpeech()

		return True
	if r is "newTopic":
		#news.findText()
		convesations[ 0 ].newTopic( news.findText() )
		return True
	return False

def newTopic():
	requests.append( "newTopic" )
	return ""

def history():
	return convesations[ 0 ].getHistory()

def checkRequests():
	while checkRequestsIterator():
		pass

news.fillChannels()
			




