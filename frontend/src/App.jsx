import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Upload from "./pages/Upload";

function App() {
  return (
    <Router>
      <div className="container">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <a className="navbar-brand" href="/">EnviroAI</a>
          <div className="navbar-nav">
            <Link className="nav-link" to="/">Upload Issue</Link>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Upload />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
