#!/usr/bin/env node

console.log( (10).toString(2) );

console.log( (256).toString(16) );
console.log( (255).toString(16) );

console.log( (255).toString(16) );


console.log("-------------------------------");

for (let i=0; i<16; i++) {
    let s = i.toString(2);
    while (s.length < 4) {
        s = "0" + s;
    }
    console.log( s );
}
