import React from "react";
import { useParams } from "react-router-dom";
import Formulario from "../components/Formulario";
import { data } from "autoprefixer";
import Loading from "./Loading";
import axios from "axios";
import { useState, useEffect } from "react";

function Concierto() {
  const [data, setData] = useState("NO");

  useEffect(() => {
    const cookies = document.cookie.split(";");
    // Busca la cookie con el nombre "token"
    const tokenCookie = cookies.find((cookie) =>
      cookie.trim().startsWith("token=")
    );
    // Si se encuentra la cookie, extrae el valor del token
    let token = null;
    if (tokenCookie) {
      token = tokenCookie.split("=")[1];
    }

    const intervalId = setInterval(() => {
      axios
        .put("http://127.0.0.1:4000/token", {
          Token: token,
        })
        .then((response) => {
          setData(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    }, 5000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return (
    <div className="mt-5 p-5">
      {data === "SI" ? <Formulario /> : <Loading />}
    </div>
  );
}

export default Concierto;
