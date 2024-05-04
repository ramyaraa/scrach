function showForm(formType) {
    document.getElementById('login-form').style.display = formType === 'login' ? 'block' : 'none';
    document.getElementById('signup-form').style.display = formType === 'signup' ? 'block' : 'none';
    document.getElementById('message').textContent = '';
}

// Function to handle the login process
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    authenticateUser(username, password, 'login');
});

// Function to handle the signup process
document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('signup-username').value;
    const password = document.getElementById('signup-password').value;
    authenticateUser(username, password, 'signup');
});

// The authenticateUser function using the type parameter
function authenticateUser(username, password, type) {
    fetch(`http://127.0.0.1:5000/${type}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const messageElement = document.getElementById('message');
        messageElement.textContent = data.message;

        if (data.success) {
            // Clear the message after 3 seconds
            setTimeout(() => {
                messageElement.textContent = '';
            }, 3000);

            document.getElementById('auth-container').style.display = 'none';
            document.getElementById('quiz-container').style.display = 'block';
            startQuiz();  // This is where you start the quiz
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('message').textContent = 'Failed to connect or server error';
    });
}
