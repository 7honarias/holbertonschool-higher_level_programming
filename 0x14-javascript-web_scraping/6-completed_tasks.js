#!/usr/bin/node
const request = require('request');

const mUrl = process.argv[2];
let userId;
const dictUserTaskComplete = {};
request.get(mUrl, function (err, response, body) {
  if (err) {
    console.log(err.message);
  }
  const todos = JSON.parse(body);
  for (const task in todos) {
    userId = todos[task].userId;
    if (todos[task].completed === true) {
      if (dictUserTaskComplete[userId] !== undefined) {
        let count = dictUserTaskComplete[userId];
        count += 1;
        dictUserTaskComplete[userId] = count;
      } else {
        dictUserTaskComplete[userId] = 1;
      }
    }
  }
  console.log(dictUserTaskComplete);
});
