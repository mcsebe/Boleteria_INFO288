import React from "react";
import { useParams } from "react-router-dom";
import Form from "../components/Form";
import axios from "axios";
import Loading from "../components/Loading";
import { useState, useEffect } from "react";
import Config from "../config/config.json";

function Concert_page() {
  const [data, setData] = useState("NO");
  const [concert, setConciert] = useState(null);
  const { id } = useParams();


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
          .put(Config.routes.token, {
            Token: token,
          })
          .then((response) => {
            console.log(response.data);
            if (response.data === "SI") {
              const fetchPosts = () => {
                return axios
                  .put(Config.routes.information, { Id: id })
                  .then((res) => res.data);
              };
              fetchPosts().then((a) => {
                setConciert(a);
                setData(response.data); // Colocar setData dentro del then de fetchPosts
              });

              // Establecer el tiempo de expiración de la cookie a 5 minutos
              document.cookie = `token=${token}; max-age=300`;
            }

          })
          .catch((error) => {
            console.log(error);
          });
      }
      if (data === "SI") {
        const cookies = document.cookie.split(";");
        const tokenCookie = cookies.find((cookie) =>
          cookie.trim().startsWith("token=")
        );
        if (!tokenCookie) {
          setData("NO");
        }
      }
    }, 5000);

    return () => {
      clearInterval(intervalId);
    };
  }, [data]);

  return (
    <div className="mt-5 p-5">
      {data === "SI" ? <Form concert={concert} /> : <Loading />}
    </div>
  );
}

export default Concert_page;
