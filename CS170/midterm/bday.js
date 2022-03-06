function randomBirthday(){
    let randomBday= Math.ceil(Math.random() * 365);
    return randomBday;
}
function runTrial(){
    let bdays = [];
    let i=0;
    for ( i=0; i<23; i++){
        let temp = randomBirthday();
        if (bdays.includes(temp)){
            return true;
        }
        else{
            bdays.push(temp);
        }
    }
    return false;
}
runTrial();
let result = {
    success: 0,
    failure: 0,
};

for (let x=0; x<1000000; x++){
    if (runTrial() === true){
        result.success += 1;
    }
    else{
        result.failure +=1;
    }
}
console.log("Successful Trials: " + result.success.toString().padEnd(8, " ") +
(result.success/1000000*100).toFixed(2)+ "%");


console.log("Failed Trials:".padEnd(19, " ") + result.failure.toString().padEnd(8, " ") +
(result.failure/1000000*100).toFixed(2)+ "%");


console.log("Total Trials:".padEnd(19, " ") + 1000000 +
"100%".padStart(7, " "));
