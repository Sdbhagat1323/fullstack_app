import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
// Added
//import { BrowserRouter as Router, Route } from "react-router-dom";
//import BaseRouter from "./routes";

import { transitions, positions, Provider as AlertProvider } from "react-alert";
import Header from "./components/layout/Header";
import Dashboard from "./components/employees/Dashboard";
import { Provider } from "react-redux";
import store from "./Store";

class App extends Component {
  render() {
    return (
      //<Route>
      //redux provider
      <Provider store={store}>
        <Fragment>
          <Header />

          <div className="container">
            <Dashboard />
          </div>
        </Fragment>
      </Provider>
      //</Route>
    );
  }
}

//ReactDOM.render(<App />, document.getElementById('app'));

export default App;
