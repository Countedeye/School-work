#!/usr/bin/env node

let args = process.argv.slice(2);

if (args.length === 0) {
    console.error("Run this program with a tilde as the first argument.");
    process.exit(1);
}

console.log(args);
