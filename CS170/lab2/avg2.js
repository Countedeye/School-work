
//	Takes each of command-line arguments provided
// and converts them to the data type number by making use of the function parsefloat()
//	Needs to sum the array of numbers and then divide
// by the number of arguments provided. (args.length)
//	The program should then output that one value without any other output.

let avg = process.argv.slice(2);    //splices off extra arguments.

function average(avg) {         //function to hold array data
    let total = 0;
    let count = 0;

    parseFloat(avg.forEach(function(item, index){
        total += item;
        count++;
    }));

    return total / count;       //divides total array by number of arguments.
}

console.log(average(avg));
