import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Upload from "./pages/Upload";
import "./css/App.css"
import Signup from "./pages/Signup";
// import Login from "./pages/Login";
// import Dashboard from "./pages/Dashboard";

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
          {/* <Route path="/login" element={<Login/>} />
          <Route path="/dashboard" element={<Dashboard/>} /> */}
          <Route path="/" element={<Upload />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
