import React, { useState, useEffect } from "react";
import Concert from "../imports/Concert";
import { Link } from "react-router-dom";
import axios from "axios";

const Concerts = () => {
  function sendInformation(name) {
    // Se genera un token, se deja en el navegador del usuario como una cookie y se envía el mismo al backend publisher
    let result =
      Math.random().toString(36).substr(2) +
      Math.random().toString(36).substr(2);
    document.cookie = `token=${result}`;
    axios.put(`http://127.0.0.1:5100/publisher`, {
      concierto: name,
      mensaje: result,
    });
  }

  return (
    <div className="md:mt-5 md:mx-[10%] grid grid-rows-1 md:grid-cols-2 justify-items-center">
      {Concert.map((e) => (
        <button
          onClick={() => sendInformation(e.name)}
          className="rounded-md mx-10 my-5 w-[20rem] h-[10rem] md:w-[18rem] md:h-[11rem] xl:w-[30rem] xl:h-[15rem] 3xl:w-[40rem] 3xl:h-[18rem] shadow-md transition-all duration-500 ease-in-out md:hover:scale-110"
        >
          <Link to={`/concierto/${e.id}`} key={e.id}>
            <div className="h-full w-full relative inline-block">
              <img
                className="h-full w-full  rounded-t-md "
                src={e.image}
                alt={e.name}
              />
              <div className="border-gray-500 font-mono absolute bottom-0 ">
                <p className="text-white mx-2 flex justify-start ">{e.name}</p>
                <p className="text-gray-200 text-sm mx-2">{e.date}</p>
              </div>
            </div>
          </Link>
        </button>
      ))}
    </div>
  );
};

export default Concerts;
