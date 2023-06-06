import React from "react";
import { useState, useEffect } from "react";
import Image from "../assets/metallica_logo.webp";
import Weeknd from "../assets/the_weeknd_logo.webp";
import Siames from "../assets/siames2.jpg";
import molotov from "../assets/molotov.jpg";
import MovimientoOriginal from "../assets/movimientoOriginal.png";
import Chystemc from "../assets/chystemc.png";
import { useNavigate  } from 'react-router-dom';
import moment from 'moment';

export default function Form(props) {

  // Crear diccionario vacío
  const places = {};
  let j = 0;
  // Recorrer el arreglo de dos en dos
  for (let i = 0; i < props.concert[0].length; i += 2) {
    const key = props.concert[0][i];
    const value =  [props.concert[2][j + 5] - props.concert[0][i + 1], props.concert[1][j + 2]];
    j = j + 1;
  
    // Asignar el valor al diccionario
    places[key] = value;
  }
  const history = useNavigate();
  const images = [Image, Weeknd, Siames, molotov, MovimientoOriginal, Chystemc];
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [selectedSeat, setSelectedSeat] = useState("");
  const [rut, setRut] = useState("");
  const [age, setAge] = useState("");
  const [price, setPrice] = useState("-");
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
    setPrice(places[event.target.value][1]);
  };
  // -----------------------------------------------------
  const handleSubmit = (event) => {
    event.preventDefault();

    const propsToSend = {
      Nombre: name,
      Rut: rut,
      Correo: email,
      Edad: age,
      Asiento: selectedSeat,
      Id_concierto: parseInt(props.concert[1][0]),
      Nombre_Concierto: props.concert[1][7],
      Token: token,
      T1: moment().format('YYYY-MM-DD HH:mm:ss'),
      Price: price
    };
    const paymentUrl = `/concierto/${parseInt(props.concert[1][0])}/pago`
    history(paymentUrl , { state: propsToSend });
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
                Lugar
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
                    Seleccione el Lugar
                  </option>
                  {Object.entries(places).map(([keyP, valueP]) => (
                    valueP[0] !== 0 && (
                      <option value={keyP}>{keyP} ({valueP[0]} disponibles)</option>
                    )
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
              src={images[props.concert[1][0] - 1]}
              alt={props.concert[1][2]}
            />
            <h3>Información General</h3>
            <p className="mt-5 md:mt-1 text-sm leading-6 text-gray-600">
              Nombre: {props.concert[1][1]}
              <br />
              Precio: ${price} <br />
              Fecha del concierto: {props.concert[1][5]}
            </p>
            <h3>Ubicación</h3>
            <p className="mt-5 md:mt-1 text-sm leading-6 text-gray-600">
              Lugar: {props.concert[2][1]}
              <br />
              Ciudad: {props.concert[2][2]} <br />
              Región: {props.concert[2][3]}
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
