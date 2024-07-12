document.getElementById('questionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const question = document.getElementById('question').value;
    const response = await fetch('http://127.0.0.1:5000/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question })
    });
    const data = await response.json();
    document.getElementById('answerText').textContent = data.answer;
});
