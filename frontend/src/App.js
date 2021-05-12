import logo from "./logo.svg";
import "./App.css";
import testApiService from "./services/test.service";
import React, { useState } from "react";
function App() {
  const [input, setInput] = useState("");
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(input);
    const data = {
      input: input,
    };

    testApiService
      .postData(data)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <form onSubmit={(e) => handleSubmit(e)}>
          <input
            onChange={(e) => setInput(e.target.value)}
            type="text"
            placeholder="Enter Here"
          />
          <button type="submit">Submit</button>
        </form>
      </header>
    </div>
  );
}

export default App;
