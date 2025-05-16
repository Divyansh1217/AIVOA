// frontend/src/components/CompanyForm.js

import React, { useState } from "react";
import axios from "axios";

const CompanyForm = () => {
  const [formData, setFormData] = useState({
    id: "",
    name: "",
    address: "",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/company", formData);
      setMessage(`Company "${response.data.name}" created successfully!`);
      setFormData({ id: "", name: "", address: "" });
    } catch (error) {
      if (error.response?.data?.detail) {
        setMessage(`Error: ${error.response.data.detail}`);
      } else {
        setMessage("An error occurred.");
      }
    }
  };

  return (
    <div>
      <h2>Create Company</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="id"
          placeholder="ID"
          value={formData.id}
          onChange={handleChange}
          required
        />
        <br />
        <input
          type="text"
          name="name"
          placeholder="Company Name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <br />
        <input
          type="text"
          name="address"
          placeholder="Address"
          value={formData.address}
          onChange={handleChange}
          required
        />
        <br />
        <button type="submit">Create Company</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default CompanyForm;
