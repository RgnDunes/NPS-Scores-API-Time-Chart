import React, { Component, useEffect, useState } from "react";
import "./App.css";
import Linechart from "./components/Linechart";

function App() {
  const [alpha, beeta] = useState({});
  var data = {};
  var keys = [];
  var values = [];

  useEffect(() => {
    fetch("/getnps")
      .then((res) => res.json())
      .then((data1) => {
        for (var key in data1) {
          keys.push(key);
          values.push(data1[key]);
        }
      });
  }, []);

  data = {
    labels: keys,
    datasets: [
      {
        label: "Daily Basis",
        backgroundColor: "rgba(142, 195, 230,0.75)",
        data: values,
      },
    ],
  };

  console.log("DATA : ", { data });
  return (
    <div className="chart">
      <Linechart data={data} />
    </div>
  );
}

export default App;
