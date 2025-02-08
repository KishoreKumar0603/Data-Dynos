import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate, Link } from "react-router-dom";
import "./css/App.css";
import "./css/auth.css";
import Signup from "./pages/Signup";
import UploadIssueForm from "./components/UploadIssueForm";
import Login from "./pages/Login.jsx";
import Dashboard from "./pages/Dashboard.jsx";

function App() {
  const isAuthenticated = !!localStorage.getItem("token"); // Check if user is logged in

  return (
    <Router>
      <div className="container-fluid p-0">
        {/* Show Navbar only if the user is authenticated */}
        {isAuthenticated && (
          <nav className="navbar navbar-expand-lg px-5">
            <a className="navbar-brand" href="/">EnviroAI</a>
            <div className="navbar-nav">
              <Link className="nav-link" to="/upload">Upload Issue</Link>
            </div>
          </nav>
        )}

        <Routes>
          <Route path="/" element={<Dashboard/>} />
          {/* Redirect to Login if not authenticated */}
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/upload" element={isAuthenticated ? <UploadIssueForm /> : <Navigate to="/login" />} />
          {/* <Route path="/" element={isAuthenticated ? <Dashboard /> : <Navigate to="/login" />} /> */}

          
        </Routes>
      </div>
    </Router>
  );
}

export default App;
