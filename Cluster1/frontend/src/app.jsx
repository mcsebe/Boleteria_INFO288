import Home from "./pages/Home";
import Concert_page from "./pages/Concert_page";
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/concierto/:id" element={<Concert_page />} />
      </Routes>
    </Router>
  );
}

export default App;
