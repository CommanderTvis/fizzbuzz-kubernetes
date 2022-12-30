const button = document.getElementById('enter-button');
button.addEventListener('click', displayNumber);
function displayNumber() {
  const input = document.getElementById('number-input');
  const number = input.value;
  const postData = async (url = '', data = {}) => {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    return response.json();
  }

  postData('127.0.0.1:5003/fizzbuzz/', { fizzbuzz: number })
    .then((data) => {
      console.log(data);
    });

}


