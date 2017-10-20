//Single file voting system
//express config
const express = require("express");
const app = express();
//Path
const path = require("path");
//database
const JsonDB = require("node-json-db");
const db = new JsonDB("db", true, true);
//functions
function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}


//express routes
//For post
app.post("/vote", (req, res) => {
    var data = req.body;
    if(data.main !== "true"){
        res.send(false);
        return false;
    }
    try {
        pathm = "/votes/" + data.userid;
        try {
            if(db.getData(pathm) == 1){
                res.send("User already exist")
                return false;
            }
        } catch (error) {
            if(validateEmail(data.userid)){
                console.log("No errors");
            } else {
                res.send("Wrong email");
                return false;
            }
        }
        db.push(pathm, 1, false);
        res.send(true);
        return true;
    } catch(err){
        console.log(path, data, err);
        res.send("See console");
        return false;
    }
});
//for get
app.get("/vote", (req, res) => {
    var data = req.query;
    if(data.main !== "true"){
        res.send(false);
        return false;
    }
    try {
        pathm = "/votes/" + data.userid;
        try {
            if(db.getData(pathm) == 1){
                res.send("User already exist")
                return false;
            }
        } catch (error) {
            if(validateEmail(data.userid)){
                console.log("No errors");
            } else {
                res.send("Wrong email");
                return false;
            }
        }
        db.push(pathm, 1, false);
        res.send(true);
        return true;
    } catch(err){
        console.log(path, data, err);
        res.send("See console");
        return false;
    }
});

//Listen on port
var port = process.env.PORT || 8080;
app.listen(port)