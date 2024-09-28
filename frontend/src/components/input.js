import React, { useState } from 'react';
import './input.css'; // Import the CSS for styling

const InputForm = () => {
    const [jobLink, setJobLink] = useState('');  // State to store the job link
    const [alertMessage, setAlertMessage] = useState('');  // State to show messages

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (jobLink.trim()) {
            // Make an API call using fetch
            try {
                const response = await fetch('http://127.0.0.1:8000/api/submit-url/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ url: jobLink }),
                });

                if (response.ok) {
                    setAlertMessage(`Link submitted successfully: ${jobLink}`);
                    setJobLink('');  // Clear the input field after submission
                } else {
                    setAlertMessage('There was an error submitting the link.');
                }
            } catch (error) {
                setAlertMessage('Network error: Could not submit the link.');
            }
        } else {
            setAlertMessage('Please enter a valid job link.');
        }
    };

    return (
        <div className="input-form">
            <h2 className="input-title">Add Your Job Links</h2>
            <p className="input-subtitle">Please place the links in the form underneath:</p>
            <form onSubmit={handleSubmit}>
                <input
                    type="url"  // Changed to "url" type for better validation
                    placeholder="Job links go here"
                    value={jobLink}
                    onChange={(e) => setJobLink(e.target.value)}
                    className="job-input"
                    required
                />
                <p className="alert-message">{alertMessage}</p>
                <div className="button-container">
                    <button type="submit" className="submit-button">Keep Submitting More</button>
                    <button
                        type="button"
                        className="done-button"
                        onClick={() => alert('Done submitting!')}
                    >
                        Done Submitting
                    </button>
                </div>
            </form>
        </div>
    );
};

export default InputForm;
