#!/usr/bin/node
const request = require('request');

const mUrl = process.argv[2];
let userId;
let dictUserTaskComplete
request.get(mUrl, function(err, response, body){
    if (err){
        console.log(err.message);
    }
    todos = JSON.parse(body);
    for (task in todos) {
        userId = todos[task]['userId'];
        if( dictUserTaskComplete.hasOwnProperty(userId) ) {
            let count = dictUserTaskComplete[userId];
            count += 1;
        }
        console.log(todos[task]['id'])
    }
});