import React from "react";
import "../css/dashboard.css";

const Dashboard = () => {
    return (
        <div className="dashboard-container">
            <h2>Welcome to EnviroAI Dashboard</h2>
            <div className="dashboard-cards">
                <div className="card">
                    <h3>Total Issues Reported</h3>
                    <p>120</p>
                </div>
                <div className="card">
                    <h3>Issues Resolved</h3>
                    <p>85</p>
                </div>
                <div className="card">
                    <h3>Pending Issues</h3>
                    <p>35</p>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
