import React from "react";
import ReactDOM from "react-dom";

import UserSearch from "./refs/UserSearch";

const App = () => {
  return (
    <React.Fragment>
      <UserSearch />
    </React.Fragment>
  )
}

ReactDOM.render(<App/>, document.querySelector('#root'));