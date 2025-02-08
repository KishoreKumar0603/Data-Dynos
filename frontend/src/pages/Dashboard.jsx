import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../css/dashboard.css";
import axios from "axios";

const Dashboard = () => {
    const [issues, setIssues] = useState([]);
    const navigate = useNavigate();

    // Fetch issues reported by the logged-in user
    useEffect(() => {
        const fetchIssues = async () => {
            const token = localStorage.getItem("access_token");
            if (!token) {
                navigate("/login");
                return;
            }

            try {
                const response = await axios.get("http://127.0.0.1:8000/api/my-issues/", {
                    headers: { Authorization: `Bearer ${token}` }
                });
                setIssues(response.data);
            } catch (error) {
                console.error("Error fetching issues:", error);
            }
        };

        fetchIssues();
    }, [navigate]);

    // Logout Function
    const handleLogout = () => {
        localStorage.removeItem("access_token");
        navigate("/login");
    };

    return (
        <div className="container">
            <div className="d-flex justify-content-between align-items-center mt-4">
                <h2>Dashboard</h2>
                <button className="btn btn-danger" onClick={handleLogout}>Logout</button>
            </div>

            {issues.length === 0 ? (
                <p className="mt-3">No issues reported yet.</p>
            ) : (
                <div className="row mt-4">
                    {issues.map((issue) => (
                        <div key={issue.id} className="col-md-4">
                            <div className="card mb-3">
                                <img src={issue.image} alt="Issue" className="card-img-top" />
                                <div className="card-body">
                                    <h5 className="card-title">Issue #{issue.id}</h5>
                                    <p className="card-text">{issue.description}</p>
                                    <p className="card-text">
                                        📍 <strong>{issue.address}</strong> <br />
                                        🗺️ Latitude: {issue.latitude}, Longitude: {issue.longitude}
                                    </p>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default Dashboard;
