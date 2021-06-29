import React from "react";
import ReactDOM from "react-dom";

import EventComponent from "./events/EventComponent";

const App = () => {
  return (
    <React.Fragment>
      <EventComponent />
    </React.Fragment>
  )
}

ReactDOM.render(<App/>, document.querySelector('#root'));