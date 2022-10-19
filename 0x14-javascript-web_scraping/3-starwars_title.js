#!/usr/bin/node

const request = require('request');
const nbr = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

try {
  request(`${url}${nbr}`, function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
} catch (err) {
  console.log(`${err}`);
}
