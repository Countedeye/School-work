
//	Takes each of command-line arguments provided
// and converts them to the data type number by making use of the function parsefloat()
//	Needs to sum the array of numbers and then divide
// by the number of arguments provided. (args.length)
//	The program should then output that one value without any other output.

let avg = process.argv.slice(2);    //splices off extra arguments.

function average(avg) {             //function to find average
    let sum = 0,                    // holds array data
        average = 0;
    for (let i of avg) {            //for if loop that adds sum of array.
        sum += i;
    }


    average = (sum/avg.length);     //averages sum of array data by the length.

    return (average);     //returns average of array data in parseFloat
}
console.log(average);
