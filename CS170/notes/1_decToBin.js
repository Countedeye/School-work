#!/usr/bin/env node

// Convert decimal to binary


function decToBin (decimal) {

    let binary = "";
    let base = 2;

    while (decimal > 0) {
        let r = decimal % base;
        decimal = Math.floor(decimal / base);
        binary = r + binary;
    }

    if (binary.length === 0) {
        return "0";
    }

    return binary;
}

// Reusability is powerful


for (let i=0; i<16; i++) {
    console.log(decToBin(i));
}
