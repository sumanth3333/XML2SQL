var express = require("express");
var http = require("http");
var path = require("path");
var exphbs = require('express-handlebars');
var support =require("./model/model.js"); // Get model function
var supportdb = require("./model/dbconnection.js"); // Get model function
const expressSession = require('express-session'); // Get the session handling middleware for express
const session = require("express-session");
const { nextTick } = require("process");
const { captureRejectionSymbol } = require("events");

// Construct the actual express object 
var app= express();

// Set up handlebars
var handlebars = exphbs.create({defaultLayout: 'main'});
app.engine('.handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.use(express.static('views'));

// Set its properties
app.use(expressSession(
    {
        resave: false,
        saveUninitialized: false,
        secret: "abcd1234EFGH", // Secret key to sign session ID
        cookie: {maxAge: 600000} // Session exprires in 600,000 ms (10 minutes)

    }
));

// When home page requested initially load Stationery's first page into session
app.get("/", function(request, response)
{
    if (!request.session.awardlist) //If no productlist list in session
    { 
        
        var result;
        supportdb.getAwards(function(result)
        {
            request.session.awardlist =result;
         //  console.log(request.session.awardlist);
         //   console.log(result);
            response.render("home");

        });
        
       // request.session.pdlist = support.getpdlist();  // Load aproductlist and store now, session starts
    }
    else
    {
    response.render("home");
    }
}); 
// try
app.get("/home", function(request,response)

{ 
   
    response.render("home",{awardselect:request.session.awardlist});
    
});


//try
// When Product selection requested , diplay it with session
app.get("/awardselect", function(request,response)

{ 
    response.render("awardselect",{awardselect:request.session.awardlist});
});

app.get("/awardselectbyIns", function(request,response)

{ 
    response.render("awardselectbyIns",{awardselectbyins:request.session.awardlist});
});

app.get("/awardselectbypi", function(request,response)
{ 
    response.render("awardselectbypi",{awardselectbypi:request.session.awardlist});
});


// When Product detail requested , diplay it with session
app.get("/awarddetail", function(request,response)
{   
var awardlist = request.session.awardlist;
 var tosearch = support.getAwardByid(request.query.id, awardlist);
 {
    response.render("awarddetail",{awarddetail:tosearch});
    
 }
});

app.get("/awarddetailpi", function(request,response)
{   
var awardlist = request.session.awardlist;

 var tosearch = support.getAwardByPI(request.query.id, awardlist);
 {
    response.render("awarddetailpi",{awarddetailpi:tosearch});
    
 }
});

app.get("/awarddetailins", function(request,response)
{   
var awardlist = request.session.awardlist;

 var tosearch = support.getAwardByIns(request.query.id, awardlist);
 {
    response.render("awarddetailins",{awarddetailins:tosearch});
    
 }
});
// Have the app listen at port 3002
http.createServer(app).listen(3002);

