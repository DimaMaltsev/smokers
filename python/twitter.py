import tweepy

consumer_key="zGHg6fRu02OlhHULDduEucTLg"
consumer_secret="YPeo575zZUruXDythUTi0OFsIrHOB3lBOoOwXyNI6u7DldmRxm"

access_token="93182551-AFIFIaZR0CTytENKb6ANtLKYty3xBT96vqIWzYgD4"
access_token_secret="qxkPFaw4D3AwXfOq6x7A8dGrP9yU7ZvBuFzPCIfbCJxcP"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getTimeLineTexts( channelName ):
	timeline = api.user_timeline( channelName )
	return [timeline_instance.text for timeline_instance in timeline]
