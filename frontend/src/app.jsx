import Home from "./pages/Home";
import Reserva from "./pages/Reserva";
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const app = () => {
  return (
    <Router>
      <Home />
      <Routes>
        <Route path="/Reserva" element={<Reserva />} />
      </Routes>
    </Router>
  );
};

export default app;
