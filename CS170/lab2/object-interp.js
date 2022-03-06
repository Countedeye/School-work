let data = {
    firstName: "Will",                                  //camelCase
    "last-name": "Sutton",                              //kebab-case
    email_address: "wsutton@sycamores.indstate.edu",    //snake_case
};

console.log(`My name is ${data.firstName} ${data["last-name"]} and my
email address is
${data["email_address"]}\n\n${data.email_address}`);
