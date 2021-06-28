import React from "react";
import ReactDOM from "react-dom";

const App = () => {
  return (
    <React.Fragment>
      <h1>Hi There!</h1>
    </React.Fragment>
  )
}

ReactDOM.render(<App/>, document.querySelector('#root'));