import React from 'react';
import Card from './card'; // Import the Card component
import { plan } from './planData'; // Import the plan data
import './studyPlan.css'; // Import CSS for the study plan

export default function StudyPlan() {
    const renderedPlan = plan.map((item, index) => {
        return (
            <Card 
                key={index}
                topic={item.topic}
                text={item.text}
                videos={item.videos}
            />
        );
    });

    return (
        <div className="study-plan-container"> {/* Apply center alignment to the container */}
            <h1>Study Plan</h1>
            <p>When you submit your job links, a personalized study plan will appear here</p>
            {renderedPlan}
        </div>
    );
}
