//Experimenting
run = true;
while(run){
    var m = Math.random() + Math.random() + Math.random()
    m = m * m
    console.log(Math.floor(m));
    if(m > 5){
        console.log("Wow");
        console.log(m);
        break;
    }
}