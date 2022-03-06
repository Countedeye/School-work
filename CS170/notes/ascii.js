#!/usr/bin/env node

function createBase64Translator() {

    let nums = [];

    for (let i=48; i<58; i++) {
        nums.push(i);
    }
    for (let i=97; i<123; i++) {
        nums.push(i);
    }
    for (let i=65; i<91; i++) {
        nums.push(i);
    }
    nums.push(45);
    nums.push(95);

    let translate = {};

    nums.forEach(function (v, i) {
        let c = String.fromCharCode(v);
        // console.log(i, c);
        translate[i] = c;
    });

    return translate;
}

module.exports.createBase64Translator = createBase64Translator;


// let translate = createBase64Translator();
// console.log(translate);
