import React from "react";
import CompanyForm from "./components/CompanyForm";
import CompanyList from "./components/CompanyList";

function App() {
  return (
    <div className="App">
      <h1>Company Manager</h1>
      <CompanyForm />
      <hr />
      <CompanyList />
    </div>
  );
}

export default App;
