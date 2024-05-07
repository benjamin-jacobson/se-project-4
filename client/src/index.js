// import React from 'react';
// import ReactDOM from 'react-dom/client';
// import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();

// // Routing v1 use this later
// import React from "react";
// import ReacDOM from 'react-dom/client';
// import { createBrowserRouter, RouterProvider } from "react-router-dom";

// import Home from "./pages/Home";

// const router = createBrowserRouter([
//   {
//     path:"/",
//     element: <Home />
//   }
// ]);

// const root = ReacDOM.createRoot(document.getElementById("root"));
// root.render(<Home />)

// import React from "react";
// import ReactDOM from "react-dom";
// import "./index.css";
// import App from "./components/App";
// import { BrowserRouter } from "react-router-dom";

// ReactDOM.render(
//   <React.StrictMode>
//     <BrowserRouter>
//       <App />
//     </BrowserRouter>
//   </React.StrictMode>,
//   document.getElementById("root")
// );

import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import routes from "./routes.js";
import "./index.css"

const router = createBrowserRouter(routes);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<RouterProvider router={router} />);