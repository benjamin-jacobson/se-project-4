import { Routes, Route } from "react-router-dom";
import UserPage from "./UserPage";


function App() {

  return (
    <>
      <main>
        <Routes>
          <Route path="/" element={ <UserPage /> }/>
        </Routes>
      </main>
    </>
  );
}
  
  export default App;