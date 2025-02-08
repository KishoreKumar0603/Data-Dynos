import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import "./css/App.css";
import "./css/auth.css";
import Signup from "./pages/Signup";
import UploadIssueForm from "./components/UploadIssueForm";
import Login from "./pages/Login.jsx";
import Dashboard from "./pages/Dashboard.jsx";

function App() {
  return (
    <Router>
      <div className="container-fluid p-0">
        <nav className="navbar navbar-expand-lg px-5">
          <a className="navbar-brand" href="/">EnviroAI</a>
          <div className="navbar-nav">
            <Link className="nav-link" to="/">Upload Issue</Link>
          </div>
        </nav>

        <Routes>
          <Route path="/signup" element={<Signup/>} />
          <Route path="/login" element={<Login/>} />
          <Route path="/upload" element={<UploadIssueForm />} />
          <Route path="/" element={<Dashboard/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
