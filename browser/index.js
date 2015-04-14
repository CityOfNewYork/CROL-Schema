var express = require('express');
var app = express();

app.set('port', (process.env.PORT || 5000));
app.use(express.static(__dirname + '/docson'));

app.get('/', function(request, response) {
  // response.send('Hello World!');
  response.redirect('/index.html')
});

app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'));
});
