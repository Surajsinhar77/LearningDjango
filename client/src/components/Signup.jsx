import React, { useState } from 'react';

function Signup() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Call the signup API endpoint with the form data
        try {
            const response = await fetch('http://127.0.0.1:8000/userSignup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // set the csrf token in the header
                    'X-CSRFToken': document.cookie.split('=')[1],
                },
                body: JSON.stringify({ name, email, password }),
            });

            if (response.ok) {
                // Handle successful signup
                console.log('Signup successful!');
            } else {
                // Handle signup error
                console.error('Signup failed!');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Name:
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
            </label>
            <br />
            <label>
                Email:
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
            </label>
            <br />
            <label>
                Password:
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            </label>
            <br />
            <button type="submit">Sign Up</button>
        </form>
    );
}

export default Signup;