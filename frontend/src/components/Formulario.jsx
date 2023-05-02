import React, { useState } from "react";
import { useParams } from "react-router-dom";
import Concert from "../imports/Concert";

export default function Formulario() {
  const { id } = useParams();

  const concierto = Concert.find((c) => c.id == id);
  const [email, setEmail] = useState("");
  const [selectedSeat, setSelectedSeat] = useState("");

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleSeatChange = (event) => {
    setSelectedSeat(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Email: ${email}`);
    console.log(`Selected seat: ${selectedSeat}`);
    console.log(`Selected concert: ${concierto.name}`);
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
                  //value={fullname}
                  //onChange={handleFullnameChange}
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
                  //value={rut}
                  //onChange={handleRutChange}
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
                  //value={age}
                  //onChange={handleAgeChange}
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
                  //value={rut}
                  //onChange={handleRutChange}
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
                  //value={selectedSeat}
                  //onChange={handleSeatChange}
                  className="w-full border rounded-md py-2 px-3 text-gray-900"
                  required
                >
                  <option value="" disabled>
                    Seleccione un asiento
                  </option>
                  <option value="A1">A1</option>
                  <option value="A2">A2</option>
                  <option value="A3">A3</option>
                  <option value="B1">B1</option>
                  <option value="B2">B2</option>
                  <option value="B3">B3</option>
                </select>
              </div>
            </div>
          </div>
        </div>
        <div className="mt-10 mx-auto w-[27rem] h-[27rem]">
          <div className="flex flex-col">
            <img
              className="w-full h-[15rem]  md:mx-auto mx-0 md:mb-8 mb-0 mr-8 rounded-md"
              src={concierto.image}
              alt={concierto.name}
            />
            <p className="mt-5 md:mt-1 text-sm leading-6 text-gray-600">
              {concierto.description} <br /> Fecha del concierto:{" "}
              {concierto.date}
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
