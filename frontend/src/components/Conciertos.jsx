import React from "react";
import Concert from "../imports/Concert";
import { Link } from "react-router-dom";
import axios from "axios";

const Conciertos = () => {
  function sendInformation(name) {

    // ----------------------- CAMBIAR ----------------------------------------
    const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    const length = 12;
    const charactersLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    // ------------------------------------------------------------------------
    axios.put(`http://127.0.0.1:5100/publisher`, {concierto: name, mensaje: result});
  }
  return (
    <div className="mt-5 mx-[10%] grid grid-cols-2 justify-items-center">
      {Concert.map((concert) => (
        <button
          onClick={() => sendInformation(concert.name)}
          className="rounded-md mx-10 my-5 w-[35rem] h-[15rem] 3xl:w-[40rem] 3xl:h-[18rem] shadow-md transition-all duration-500 ease-in-out hover:scale-110"
        >
          <div className="h-full w-full relative inline-block">
            <img
              className="h-full w-full  rounded-t-md "
              src={concert.image}
              alt={concert.name}
            />
            <div className="border-gray-500 font-mono absolute bottom-0 right-100">
              <p className="text-white font-bold mx-3 ">{concert.name}</p>
              <p className="text-gray-200 text-sm mx-2 ">{concert.date}</p>
            </div>
          </div>
        </button>
      ))}
    </div>
  );
};

export default Conciertos;
