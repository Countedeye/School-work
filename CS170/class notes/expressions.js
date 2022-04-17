#!/usr/bin/env node



// Single line comments

/* Multiline
comments */

// Basic types

// Number

console.log(5, typeof 5);
console.log(-4, typeof -4);
console.log(0.1, typeof 0.1);
console.log(-3.2, typeof -3.2);

// Be careful of rounding errors

console.log(0.1 + 0.2);

// Arithmetic ops
// _ + * / ** %



console.log("-----------------------");
console.log("Boolean values:");

console.log(true, typeof true);
console.log(false, typeof false);

console.log("Boolean Operators");

console.log("AND: &&");

console.log(false && false);
console.log(false && true);
console.log(true && false);
console.log(true && true);

console.log("OR: ||");

console.log(false || false);
console.log(false || true);
console.log(true || false);
console.log(true || true);

console.log("Expressions always evaluate down to a single value.");

console.log( (!(true && true) || !(true && false)) );
console.log( true );

console.log("---------------------------");
console.log("Strings: surround text with double or single quotes.");
console.log("Template strings use backticks. ` ");


console.log("", typeof "");
console.log("a", typeof "a");
console.log("cat", typeof "cat");

let firstName = "Bob";
let lastName = "Roberts";
let age = 19;

console.log(firstName + " " + lastName + " " + age);
console.log(`${firstName} ${lastName} ${age}`);
