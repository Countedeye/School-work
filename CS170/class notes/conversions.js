#!/usr/bin/env node

// Convert decimal to binary


let decimal = 11;
let binary = "";
let base = 2;

while (decimal > 0) {
    let r = decimal % base;
    decimal = Math.floor(decimal / base);
    binary = r + binary;
}

console.log(binary);
