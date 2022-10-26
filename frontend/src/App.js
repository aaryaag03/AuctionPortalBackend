import "./style.css";
import React, { Component } from "react";

import Login from "./components/Login";
import Register from "./components/Register";
// import Home from "./components/Home";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Login />
        <Register />
        {/* <Home/> */}
      </div>
    );
  }
}
export default App;
