import Conciertos from "../components/Conciertos";
import Carrousel from "../components/Carrousel";

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
