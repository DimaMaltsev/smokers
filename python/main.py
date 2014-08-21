import talks
from flask import Flask
app = Flask(__name__)
talks.createConversation()

@app.route("/")
def hello():
    return talks.history()

@app.route("/nextSpeech")
def nextSpeech():
	print "NEXT SPEECH REQUEST:::::::"
	return talks.nextSpeech()

@app.route("/newTopic")
def newTopic():
    return talks.newTopic()
 
@app.route("/history")
def history():
    return talks.history()


if __name__ == "__main__":
    app.run( "0.0.0.0" , 5000 )
