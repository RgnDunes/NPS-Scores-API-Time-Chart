import React from "react";
import { Line } from "react-chartjs-2";

function Linechart(props) {
  return <Line data={props.data}></Line>;
}

export default Linechart;
