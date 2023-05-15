import React from "react";
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";
import Image from "../assets/metallica_logo.webp";
import Weeknd from "../assets/the_weeknd_logo.webp";
import Siames from "../assets/siames2.jpg";
import molotov from "../assets/molotov.jpg";
import MovimientoOriginal from "../assets/movimientoOriginal.png";
import Chystemc from "../assets/chystemc.png";

export default function Formulario(props) {
  const imagenes = [
    Image,
    Weeknd,
    Siames,
    molotov,
    MovimientoOriginal,
    Chystemc,
  ];

  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [selectedSeat, setSelectedSeat] = useState("");
  const [rut, setRut] = useState("");
  const [age, setAge] = useState("");
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
  const handleNameChange = (event) => {
    setName(event.target.value);
  };
  const handleRutChange = (event) => {
    setRut(event.target.value);
  };
  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };
  const handleAgeChange = (event) => {
    setAge(event.target.value);
  };
  const handleSeatChange = (event) => {
    setSelectedSeat(event.target.value);
  };
  // -----------------------------------------------------
  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post(`http://127.0.0.1:5001/subir`, {
      Nombre: name,
      Rut: rut,
      Correo: email,
      Edad: age,
      Asiento: parseInt(selectedSeat),
      Id_concierto: parseInt(props.concierto[1][0]),
      Nombre_Concierto: props.concierto[1][5],
      Token: token,
    });
    window.location.href = "/";
  };
  return (
    <form onSubmit={handleSubmit}>
      <div className="grid md:grid-cols-2 justify-items-center ">
        <div className=" pb-12">
          <h2 className="text-base font-bold leading-7 text-gray-900">
            Ingresar informacion personal
          </h2>
          <p className="mt-1 text-sm leading-6 text-gray-600">
            Recuerde ingresar su correo electronico personal, pues a este
            llegaran las entradas.
          </p>
          <div className="mt-5 flex flex-col gap-x-6 gap-y-8">
            <div className="sm:col-span-3">
              <label
                htmlFor="name"
                className="block  text-sm font-bold leading-6 text-gray-900"
              >
                Nombre completo
              </label>
              <div className="mt-2">
                <input
                  type="fullname"
                  id="fullname"
                  value={name}
                  onChange={handleNameChange}
                  placeholder="Ingrese su nombre completo"
                  className="w-full border rounded-md py-2 px-3 text-gray-900"
                  required
                />
              </div>
            </div>
            <div className="sm:col-span-3">
              <label
                htmlFor="rut"
                className="block text-sm font-bold leading-6 text-gray-900"
              >
                Rut
              </label>
              <div className="mt-2">
                <input
                  type="rut"
                  id="rut"
                  value={rut}
                  onChange={handleRutChange}
                  placeholder="Ingrese su rut"
                  className="w-full border rounded-md py-2 px-3 text-gray-900"
                  required
                />
              </div>
            </div>
            <div className="sm:col-span-3">
              <label
                htmlFor="email"
                className="block text-sm font-bold leading-6 text-gray-900"
              >
                Email
              </label>
              <div className="mt-2">
                <input
                  type="email"
                  id="email"
                  value={email}
                  onChange={handleEmailChange}
                  placeholder="Ingrese su Email"
                  className="w-full border rounded-md py-2 px-3 text-gray-900"
                  required
                />
              </div>
            </div>
            <div className="sm:col-span-3">
              <label
                htmlFor="age"
                className="block text-sm font-bold leading-6 text-gray-900"
              >
                Edad
              </label>
              <div className="mt-2">
                <input
                  type="age"
                  id="age"
                  value={age}
                  onChange={handleAgeChange}
                  placeholder="Ingrese su edad"
                  className="w-full border rounded-md py-2 px-3 text-gray-900"
                  required
                />
              </div>
            </div>
            <div className="sm:col-span-3">
              <label
                htmlFor="Asiento"
                className="block text-sm font-bold leading-6 text-gray-900"
              >
                Asiento
              </label>
              <div className="mt-2">
                <select
                  id="seat"
                  value={selectedSeat}
                  onChange={handleSeatChange}
                  className="w-full border rounded-md py-2 px-3 text-gray-900"
                  required
                >
                  <option value="" disabled>
                    Seleccione un asiento
                  </option>
                  {props.concierto[0].map((asiento) => (
                    <option value={asiento}>{asiento}</option>
                  ))}
                </select>
              </div>
            </div>
          </div>
        </div>
        <div className="mt-10 mx-auto w-[27rem] h-[27rem]">
          <div className="flex flex-col">
            <img
              className="w-full h-[15rem]  md:mx-auto mx-0 md:mb-8 mb-0 mr-8 rounded-md"
              src={imagenes[props.concierto[1][0] - 1]}
              alt={props.concierto[1][2]}
            />
            <h3>Información General</h3>
            <p className="mt-5 md:mt-1 text-sm leading-6 text-gray-600">
              Nombre: {props.concierto[1][1]}
              <br />
              Precio: ${props.concierto[1][2]} <br />
              Fecha del concierto: {props.concierto[1][3]}
            </p>
            <h3>Ubicación</h3>
            <p className="mt-5 md:mt-1 text-sm leading-6 text-gray-600">
              Lugar: {props.concierto[2][1]}
              <br />
              Ciudad: {props.concierto[2][2]} <br />
              Región: {props.concierto[2][3]}
            </p>
            <button
              type="submit"
              className="bg-green-500 mt-5 text-white rounded-md py-2 px-5 hover:bg-green-600"
            >
              Pagar
            </button>
          </div>
        </div>
      </div>
    </form>
  );
}
