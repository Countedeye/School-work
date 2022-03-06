#!/usr/bin/env node

// Do not pollute the global namespace!
// setTimeout = "My Variable a";

console.dir(global);

// console.log(a);

global.setTimeout(function () {
    console.log("Go 1!");
}, 2000);

setTimeout(function () {
    console.log("Go 2!");
}, 2000);
