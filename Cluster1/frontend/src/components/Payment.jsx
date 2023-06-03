import React from "react";
import { useState, useEffect } from "react";
import Config from "../config/config.json"

export default function Payment(props) {
    const [time, setTime] = useState(Math.floor((Config.min * 60000) + Math.random() * ((Config.max - Config.min) * 60000)));

    useEffect(() => {
        const intervalId = setInterval(() => {
            const probability = Math.floor( Math.random() * 100);
            if(probability <= Config.probability){
                console.log(probability);
                console.log(time/60000);
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

  