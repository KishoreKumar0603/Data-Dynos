import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate, Link } from "react-router-dom";
import "./css/App.css";
import "./css/auth.css";
import Signup from "./pages/Signup";
import UploadIssueForm from "./components/UploadIssueForm";
import Login from "./pages/Login.jsx";
import Dashboard from "./pages/Dashboard.jsx";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem("token"));

  useEffect(() => {
    const checkAuth = () => {
      setIsAuthenticated(!!localStorage.getItem("token"));
    };
    window.addEventListener("storage", checkAuth); // Sync across tabs
    return () => window.removeEventListener("storage", checkAuth);
  }, []);

  return (
    <Router>
      <div className="container-fluid p-0">
        {/* Show Navbar only if the user is authenticated */}
        {isAuthenticated && (
  <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-5 shadow">
    <div className="container-fluid">
      <a className="navbar-brand fw-bold text-light" href="/">🌍 EnviroAI</a>
      <button 
        className="navbar-toggler" 
        type="button" 
        data-bs-toggle="collapse" 
        data-bs-target="#navbarNav"
        aria-controls="navbarNav" 
        aria-expanded="false" 
        aria-label="Toggle navigation"
      >
        <span className="navbar-toggler-icon"></span>
      </button>
      
      <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item">
            <Link className="nav-link text-light fw-semibold" to="/upload">
              Upload Issue
            </Link>
          </li>
          <li className="nav-item">
            <button 
              className="btn btn-danger ms-3 fw-bold px-3 py-2 logout-btn" 
              onClick={() => {
                localStorage.removeItem("token");
                localStorage.removeItem("user");
                setIsAuthenticated(false);
                window.location.href = "/login"; 
              }}
            >
              Logout
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
)}


        <Routes>
          <Route path="/" element={isAuthenticated ? <Dashboard /> : <Navigate to="/login" />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login setAuth={setIsAuthenticated} />} />
          <Route path="/upload" element={isAuthenticated ? <UploadIssueForm /> : <Navigate to="/login" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
