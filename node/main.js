var httpSender = require( "./httpRequester.js" );
var http = require("http");


history = ""
i = 0
function sendRequestToPyhon( method , callback ){
    var options = {
        host: 'localhost',
        port: 5000,
        path: '/' + method,
        method: 'GET'
    };

    httpSender.getJSON( options , callback );
}

function askNextSpeech(){
    sendRequestToPyhon( "nextSpeech" , function( res ){ 
        if( res != "*thinking*" ){
            i++;
            history += res + "<br>"; 

            if( i == 5 ){
                sendRequestToPyhon( "newTopic" , function(){} );
                i = 0;
            }

        }
    } )
    setTimeout( askNextSpeech , 1000 )
}




/*var io = require('socket.io').listen(8080);

io.sockets.on('connection', function (socket) {
  socket.on('message', function () { });
  socket.on('disconnect', function () { });
});*/

http.createServer(function(request, response) {
  response.writeHead(200, {"Content-Type": "text/html"});
  response.write(history);
  response.end();
}).listen(5001);

askNextSpeech();