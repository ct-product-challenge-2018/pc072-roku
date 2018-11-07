var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);
io.on('connection', function(socket){ 
    console.log('connected') 
    setInterval(function(){
        socket.emit('blah', [1,2,3]);
    }, 1000)
    socket.on('time', function(data) {
        console.log('time', data)
    })
});
server.listen(3000);
app.use(express.static('./'));