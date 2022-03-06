function randomBirthday(){
    let randomBday= Math.ceil(Math.random() * 365);
    console.log(randomBday);
}
let bdays = [];

function birthdays(){
    let i=0;
    for ( i in randomBirthday()){
        while (i<=23){
            i= bdays++;}
    }
}
console.log(birthdays());
