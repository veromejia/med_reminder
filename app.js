var express = require("express");
var app = express();
var path = require('path');
var mongoose = require('mongoose');
var mongoDB = 'mongodb://localhost/my_database';
mongoose.connect(mongoDB, { useUnifiedTopology: true });
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
/* MongoClient.connect("mongodb://localhost/med_reminder_app");
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json())*/
var Schema = mongoose.Schema;
var recipientSchema = new Schema({
        firstName: "",
        lastName: "",
        birthDate: Number,
        phoneNumber: Number,
});

var Recipient = mongoose.model("Recipient", recipientSchema);

// When you go to "/" => it's the home page


app.use(express.static(path.join(__dirname)));
//set up the restful route
app.get('/', function(req, res) {
        res.redirect("/welcome");
        //res.sendFile(path.join(__dirname + '/welcome.html'));
});
// index route
app.get("/welcome"), function(req, res){
        res.render("welcome.html");
}
// create Route
app.post('/recipient', function(req, res) {
        res.sendFile(path.join(__dirname + 'recipient.html'));
});


/*app.get("/", function(req, res) {
        res.sendFile("/welcome.html");
});

app.get("/welcome", function(req, res) {
        res.render("/recipient");
});
*/
// when go to /recipient => it's for recipient info
// when got to /Reminder get to selection info
app.listen(3000, function() {
        console.log("server has started!!");
});