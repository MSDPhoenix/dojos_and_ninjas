let count = 0;

function edit_dojo_name() {
    let dojo_name = document.querySelector("h1");
    if (count%2==0) {
    // if (dojo_name.style="color: red;") {
        dojo_name.style="color: black;";
        count+=1;
        console.log('Turning black',count)
    } else {
        dojo_name.style="color: red;";
        count+=1;
        console.log('Turning red',count)
    }


    let newName = window.prompt('enter new name','')
    dojo_name.innerText = newName


    // NEED TO AJAX WITH DATABASE!!!
}