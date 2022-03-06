// problematic flow
// conditional statements (if/else if / else)

console.log("Starting Program...");

let score = Math.random() * 100;

console.log("Score:", score);

// Only one code block will execute in if/else if/else, and
// One will definitely execute.
if(score < 60){
    console.log("You got better than an F.");
}
else if(score < 70){
    console.log("You received a D.");
}
else if(score < 80){
    console.log("You received a C.");
}
else if(score < 90){
    console.log("You received a B.");
}
else if(score < 100){
    console.log("You received an A.");
}
else{
    console.log("A+!");
}

console.log("Program complete.");
