import React from "react";
import { useState, useEffect } from "react";
import Config from "../config/config.json"
import { useLocation } from 'react-router-dom';
import moment from 'moment';
import swal from 'sweetalert'
import axios from "axios";

export default function Payment() {
    // Tiempo entre min y max del archivo config medido en milisegundos
    const [time, setTime] = useState(Math.floor((Config.min * 60000) + Math.random() * ((Config.max - Config.min) * 60000)));
    const location = useLocation();
    const props = location.state;
    // Luego de "time" tiempo (Ej: entre 2 y 3 min) se genera un numero aleatorio entre 0 y 100 que representa la probabilidad del pago
    // Si es menor a la probabilidad establecida en el archivo config, entonces se inserta a la base de datos, en caso contrario, se descarta
    useEffect(() => {
        const intervalId = setInterval(() => {
            const probability = Math.floor( Math.random() * 100);
            console.log(probability);
            if(probability <= Config.probability){
                axios.post(Config.routes.upload, {
                    Nombre: props.Nombre,
                    Rut: props.Rut,
                    Correo: props.Correo,
                    Edad: props.Edad,
                    Asiento: props.Asiento,
                    Id_concierto: props.Id_concierto,
                    Nombre_Concierto: props.Nombre_Concierto,
                    Token: props.Token,
                    T1: props.T1,
                    T2: moment().format('YYYY-MM-DD HH:mm:ss')
                });
                setTime(900000000);
                swal({
                    text: "'Pago realizado correctamente!'",
                    icon: "success",
                    timer: "5000"
                  }).then(function(){ 
                    window.location.href = "/"
                    }
                  )
            }else{
                setTime(900000000);
                swal({
                    text: "'Pago no realizado!'",
                    icon: "error",
                    timer: "5000"
                  }).then(function(){ 
                    window.location.href = "/"
                    }
                  )
            }
            
        }, time);
    
        return () => {
          clearInterval(intervalId);
        };
      }, []);

     return (
        <div
        className='fixed inset-0 flex items-center justify-center flex-col bg-fixed bg-center bg-cover bg-no-repeat'
        >
        <div
        className='fixed inset-0 flex items-center justify-center flex-col bg-fixed bg-center bg-cover bg-no-repeat'
        style={{
            backgroundImage: 'url("https://static3.pisapapeles.net/uploads/2022/10/Captura-de-pantalla-2022-10-26-a-las-23.04.16.jpg")',
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            opacity: '0.3',
        }}
        />
        <h1 className="font-bold text-lg mb-4">Simulando el pago...</h1>
        <div
            className="inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-current border-r-transparent align-[-0.125em] motion-reduce:animate-[spin_1.5s_linear_infinite]"
            role="status"
        >
            <span className="!absolute !-m-px !h-px !w-px !overflow-hidden !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]">
            Loading...
            </span>
        </div>
        </div>
    );
};

  