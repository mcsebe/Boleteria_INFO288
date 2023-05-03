import React, { useState, useEffect, useRef } from "react";
import Concert from "../imports/Concert";
import { GrFormPrevious, GrFormNext } from "react-icons/gr";

let count = 0;
let slideInterval;
const Carrousel = () => {
  const intervalTime = 5000;
  const [index, setIndex] = useState(0);
  const slideRef = useRef();
  const removeAnimation = () => {
    slideRef.current.classList.remove("fade-anim");
  };
  useEffect(() => {
    slideRef.current.addEventListener("animationend", removeAnimation);
    slideRef.current.addEventListener("mouseenter", pauseSlider);
    slideRef.current.addEventListener("mouseleave", startSlider);
    startSlider();
    return () => {
      pauseSlider();
    };
  }, []);

  const startSlider = () => {
    slideInterval = setInterval(() => {
      nextSlide();
    }, intervalTime);
  };
  const nextSlide = () => {
    count = (count + 1) % Concert.length;
    setIndex(count);
    slideRef.current.classList.add("fade-anim");
  };
  const prevSlide = () => {
    count = (index - 1 + Concert.length) % Concert.length;
    setIndex(count);
    slideRef.current.classList.add("fade-anim");
  };
  const pauseSlider = () => {
    clearInterval(slideInterval);
  };
  return (
    <div ref={slideRef} className="w-full select-none relative">
      <div className="w-full h-[30rem]">
        <img className="h-full w-full" src={Concert[index].image} alt="" />
      </div>
      <div className="absolute w-full top-1/2 transform -traslate-y-1/2 px-3 flex justify-between items-center">
        <button
          onClick={prevSlide}
          className="bg-white  text-white rounded-full bg-opacity-50 cursor-pointer hover:bg-opacity-100 transition"
        >
          <GrFormPrevious size={30} color="white" />
        </button>
        <button
          onClick={nextSlide}
          className="bg-white text-white rounded-full bg-opacity-50 cursor-pointer hover:bg-opacity-100 transition"
        >
          <GrFormNext size={30} />
        </button>
      </div>
    </div>
  );
};

export default Carrousel;
