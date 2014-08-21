var http = require( "./httpRequester.js" );

options = {
    host: 'localhost',
    port: 5000,
    path: '/',
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
};

http.getJSON(options,
    function(statusCode, result)
    {
        console.log(result.toString());
    }
);

var io = require('socket.io').listen(8080);

io.sockets.on('connection', function (socket) {
  socket.on('message', function () { });
  socket.on('disconnect', function () { });
});