import React from "react";
import { Route } from "react-router-dom";
import { getEmployees } from "./actions/employees";

const BaseRouter = () => {
  <div>
    <Route exact path="/" component={getEmployees} />
    <Route exact path="/employeeID/" component={getEmployees} />
  </div>;
};

export default BaseRouter;
