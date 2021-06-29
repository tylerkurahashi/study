import React from "react";
import ReactDOM from "react-dom";

import UserSearch from './state/UserSearch';

const App = () => {
  return (
    <React.Fragment>
      <UserSearch />
    </React.Fragment>
  )
}

ReactDOM.render(<App/>, document.querySelector('#root'));