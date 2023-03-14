#!/usr/bin/node
const {argv} = require('process');
while (argv.length >= 2) {
  if (argv.length === 2) {
    console.log('No argument');
  } else if (argv.length === 3){
    console.log('Argument found');
  }
  console.log('Arguments found')
}
