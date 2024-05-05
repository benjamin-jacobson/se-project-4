import { Routes, Route } from "react-router-dom";
import Home from "./Home";
import UserPage from "./UserPage";


function App() {

  return (
    <>
      <main>
        <Routes>
          <Route path="/" element={ <Home /> }/>
          <Route path="/users" element={ <UserPage /> }/>
        </Routes>
      </main>
    </>
  );
}
  
  export default App;