import Concerts from "../components/Concerts";
import Carrousel from "../components/Carrousel";

function Home() {
  return (
    <div className="App">
      <div className="">
        <Carrousel />
      </div>
      <Concerts />
    </div>
  );
}

export default Home;
