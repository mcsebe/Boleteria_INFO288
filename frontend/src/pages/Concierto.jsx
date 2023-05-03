import React from "react";
import { useParams } from "react-router-dom";
import Formulario from "../components/Formulario";
import { data } from "autoprefixer";
import Home from "./Home";
import axios from "axios";

function Concierto() {
  let token = "";
  axios
    .put("http://127.0.0.1:5100/token", {
      concierto: name,
      mensaje: "123",
    })
    .then((response) => {
      const data = response.data;
      token = data;
    })
    .catch((error) => {
      console.log(error);
    });
  console.log(token);
  return (
    <div className="mt-5 p-5">
      <Formulario />
    </div>
  );
}
export default Concierto;
