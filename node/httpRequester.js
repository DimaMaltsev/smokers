var http = require("http");
var https = require("https");

exports.getJSON = function(options, onResult)
{
    var prot = options.port == 443 ? https : http;
    var req = prot.request(options, function(res)
    {
        var output = '';
        res.setEncoding('utf8');
        res.on('data', function (chunk) { output += chunk; });
        res.on('end', function() {
            var obj = output;
            onResult( obj );
        });
    });
    req.on('error', function(err) { });
    req.end();
};

/*var options = {
    host: 'localhost',
    port: 5000,
    path: '/',
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
};*/

/*getJSON(options,
        function(statusCode, result)
        {
            // I could work with the result html/json here.  I could also just return it
            console.log("onResult: (" + statusCode + ")" + result.toString());
            //res.statusCode = statusCode;
            //res.send(result);
        });*/