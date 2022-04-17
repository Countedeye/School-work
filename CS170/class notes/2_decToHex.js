#!/usr/bin/env node



function decToHex(num) {

    let translate = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    };

    let output = "";
    let base = 16;

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


for (let i=0; i<256; i++) {
    console.log(decToHex(i));
}
