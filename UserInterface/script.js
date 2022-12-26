const button = document.getElementById('enter-button');
button.addEventListener('click', displayNumber);
function displayNumber() {
  const input = document.getElementById('number-input');
  const number = input.value;

    const options = {
      hostname: 'url_adrress_answer',
      path: 'application/json',
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      }
    };

    const req = http.request(options, (res) => {
      console.log(`STATUS: ${res.statusCode}`);
    });
    req.write(number);
    req.end();

    var Get_Requst = new XMLHttpRequest();
    Get_Requst.open("GET", "url_adrress_answer", true);
    Get_Requst.onload = function (){
    alert( Get_Requst.responseText);
}
Get_Requst.send(null);
}

