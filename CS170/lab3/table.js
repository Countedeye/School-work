let students = ["Gabrielle", "Will", "Bryson"];
let scores = [100.5, 0.0, 89.9];


console.log("|==============|==============|");
console.log("| Student      | Score        |");
console.log("|==============|==============|");

let paddedStudents = [];
for (let i=0; i<students.length; i++) {
    let padded = students[i].padEnd(12, " ");
    paddedStudents.push(padded);
}

let paddedScores = [];
for(let i=0; i<scores.length; i++) {
    let roundedString = scores[i].toFixed(2);
    let padded = roundedString.padStart(10, " ");
    paddedScores.push(padded);
}

for (let i=0; i<paddedStudents.length; i++){
    console.log(`| ${paddedStudents[i]} | ${paddedScores[i]} % |`);
    console.log("|--------------|--------------|");
}
