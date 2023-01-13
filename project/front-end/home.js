document.addEventListener("DOMContentLoaded", function (ev) {
    document.querySelector('.form').addEventListener('submit', (e) => {
    e.preventDefault();
    // get the form data
    const formData = new FormData(e.target);
    const json = {}
    for (const [key, value]  of formData.entries()) {
        json[key] = value
    }
    console.log(json)
    //const data = JSON.stringify(json)
    fetch('http://localhost:5000/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(json)
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            console.log(data.prediction)
            t = data.prediction
            result = "Waiting ..."
            color = "black"
            if(t == 1){
                result = "Fraud"
                color = "red"
            }else if(t == 0){
                result = "No Fraud"
                color = "green"
            }
            document.getElementById('result').innerHTML = result;
            document.getElementById('result').style.color = color;
        })
        .catch(error => console.error(error));
});

})
