let values = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "t", "j", "q", "k"];
// array for characters
let suits = ["s", "h", "c", "d"];
//array for suits
let deck=[];

let fancySuits = {              //object for suits in deck
    s: "Spades",
    h: "Hearts",
    c: "Clubs",
    d: "Diamonds",
};
let suitCharacter = {           //object for characters in deck
    a: "Ace",
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    t: 10,
    j: "Jack",
    q: "Queen",
    k: "King",
};
for (let i=0; i<suits.length; i++){         //for loop that creates organized deck
    for (let x=0; x<values.length; x++)     //nest for loop for creating deck with characters
        deck.push(suits[i] + values[x]);    // inserting suits and characters to array.
}
let randomcard = deck[Math.ceil(Math.random() * 52)];       //picks a random card
let randomcardsplit = randomcard.split('');                 // splits the card into two strings
console.log(suitCharacter[randomcardsplit[1]] + " of " + fancySuits[randomcardsplit[0]]);
// prints the Character with the suit.
