import React, { useState } from 'react';

function Form() {
    const [result, setResult] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const json = {};
        for (const [key, value] of formData.entries()) {
            json[key] = value;
        }

        fetch('http://localhost:5000/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(json)
        })
            .then(response => response.json())
            .then(data => {
                setResult(data.prediction);
            })
            .catch(error => console.error(error));
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="input" placeholder="Enter input here" />
            <button type="submit">Predict</button>
            <div id="result">{result}</div>
        </form>
    );
}

export default Form;