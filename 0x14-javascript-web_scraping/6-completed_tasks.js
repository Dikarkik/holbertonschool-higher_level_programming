#!/usr/bin/node
// Script that computes the number of tasks completed by user id.
// ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const tasksCompleted = {};

    for (const task of JSON.parse(body)) {
      if (task.completed) {
        if (!tasksCompleted[task.userId]) {
          tasksCompleted[task.userId] = 1;
        } else {
          tasksCompleted[task.userId]++;
        }
      }
    }
    console.log(tasksCompleted);
  }
});
