import React from 'react';
import './hero.css'; // Create a CSS file for styling

const Hero = () => {
  return (
    <section className="hero">
      <h1 className="hero-title">Welcome to the Study Plan Maker</h1>
      <p className="hero-subtitle">Your personalized learning journey starts here!</p>
      <div className="scroll-prompt">
        <span className="arrow">⬇️</span>
        <p>Scroll down to get started</p>
      </div>
    </section>
  );
};

export default Hero;
