#!/usr/bin/node

process.argv.forEach((val, index) => {
    if (index > 1){
        console.log(val);
    }
});
if (process.argv.length > 2){
    console.log("Argument found");
}else{
    console.log("No argument")
}