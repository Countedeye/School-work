#!/usr/bin/env node

const ascii = require("./ascii.js");

function decToBase(num, base=16) {

    let translate = ascii.createBase64Translator();

    let output = "";

    while (num > 0) {
        let r = num % base;
        num = Math.floor(num / base);
        output = translate[r] + output;
    }

    if (output.length === 0) {
        output = "0";
    }

    return output;
}

let max = 64**2;
for (let i=0; i<max; i++) {
    console.log(decToBase(i, 64));
}
