import React from 'react';
import './card.css'; // Import CSS for styling

export default function Card({ topic, text, videos }) {
    return (
        <div className="card">
            <h2 className="card-title">{topic}</h2>
            <p className="card-text">{text}</p>
            <div className="card-videos">
                {videos.map((video, index) => (
                    <a key={index} href={video.link} target="_blank" rel="noopener noreferrer">
                        <img 
                            src={video.thumbnail} 
                            alt={`Video ${index + 1}`} 
                            className="video-thumbnail"
                        />
                    </a>
                ))}
            </div>
        </div>
    );
}
