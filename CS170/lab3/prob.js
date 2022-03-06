let totalsArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];          //holds total rolls
for (let i=0; i<100000; i++) {                                  //100000 loop for rolls
    let total = Math.ceil(Math.random() * 6) + Math.ceil(Math.random() * 6);  //rolls total dice
    totalsArray[total] += 1;            //iterates to the totalArray
}
for (let x=2; x<totalsArray.length; x++) {
    console.log(x + ":".padEnd(2, " ") + (totalsArray[x]/100000*100).toFixed(2) + "%");
    //prints out padded output.
}
