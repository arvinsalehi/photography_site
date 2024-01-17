function sum() {
    var num1 = document.getElementById('num1').value;
    var num2 = document.getElementById('num2').value;
    var title = document.getElementById('title')
    title.innerHTML = parseInt(num1) + parseInt(num2);
}

function changeTitle(value) {
    document.getElementById('title').innerHTML = value; //fix bug
}

var time = new Date().getHours();
if (time < 12) {
    document.getElementById('title').innerHTML = "Good Morning";
}else if ( time <= 18){
    document.getElementById('title').innerHTML = "Good Afternoon";
}else{
    document.getElementById('title').innerHTML = "Good Night";
}

var caseTest = 'Fucker';

switch (caseTest){
    case "Fucker":{
        document.write('Fucker');
        break;
    }
    case "Sucker": {
        document.write('Sucker');
        break;
    }
    default:{
        document.write("Fuck you");
        break;
    }
}