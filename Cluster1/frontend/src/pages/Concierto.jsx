import React from "react";
import { useParams } from "react-router-dom";
import Formulario from "../components/Formulario";
import { data } from "autoprefixer";
import axios from "axios";
import Loading from "../components/Loading";
import { useState, useEffect } from 'react';


function Concierto() {
  const [data, setData] = useState("NO");
  const [concierto, setConcierto] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    const fetchPosts = () => {
      return axios.put("http://127.0.0.1:5001/informacion", {Id: id})
        .then(res => res.data);
    };
    fetchPosts()
      .then(a => setConcierto(a));
  },[]);

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
      if (data === "NO") {
        axios
          .put("http://127.0.0.1:8088/token", {
            Token: token,
          })
          .then((response) => {
            setData(response.data);
            if (response.data === "SI") {
              // Establecer el tiempo de expiración de la cookie a 5 minutos
              document.cookie = `token=${token}; max-age=300`;
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
      if(data === "SI"){
        const cookies = document.cookie.split(";");
        const tokenCookie = cookies.find((cookie) =>
          cookie.trim().startsWith("token=")
        );
        if (!tokenCookie) {
          setData("NO")
        }
      }
    }, 5000);

    return () => {
      clearInterval(intervalId);
    };
  }, [data]);

  return (
    <div className="mt-5 p-5">
      {data === "SI" ? <Formulario concierto={concierto}/> : <Loading />}
    </div>
  );
}

export default Concierto;