import Conciertos from "../components/Conciertos";
import Header from "../components/Header";
import Carrousel from "../components/Carrousel";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="App">
      <div className="">
        <Carrousel />
      </div>

      <Conciertos />
    </div>
  );
}

export default Home;
