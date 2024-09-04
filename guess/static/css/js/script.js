// script.js

document.getElementById('guessForm').addEventListener('submit', function(event) {
    const userGuess = document.getElementById('userGuess').value;

    if (userGuess < 1 || userGuess > 10) {
        event.preventDefault();
        document.getElementById('feedback').innerText = 'Please enter a number between 1 and 10.';
    }
});
