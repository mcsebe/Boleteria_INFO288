import Home from "./pages/Home";
import Concierto from "./pages/Concierto";
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/concierto/:id" element={<Concierto />} />
      </Routes>
    </Router>
  );
}

export default App;
