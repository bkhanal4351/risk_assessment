import React, { useState } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/predict/";

function App() {
  const [formData, setFormData] = useState({
    chemical_concentration: "",
    air_quality_index: "",
    water_toxicity: "",
    soil_contamination: "",
  });
  const [riskLevel, setRiskLevel] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(API_URL, formData);
      setRiskLevel(response.data.risk_level);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <h2>EPA Risk Assessment</h2>
      <form onSubmit={handleSubmit}>
        <input type="number" name="chemical_concentration" placeholder="Chemical Concentration" onChange={handleChange} required />
        <input type="number" name="air_quality_index" placeholder="Air Quality Index" onChange={handleChange} required />
        <input type="number" name="water_toxicity" placeholder="Water Toxicity" onChange={handleChange} required />
        <input type="number" name="soil_contamination" placeholder="Soil Contamination" onChange={handleChange} required />
        <button type="submit">Predict Risk</button>
      </form>
      {riskLevel && <h3>Predicted Risk Level: {riskLevel}</h3>}
    </div>
  );
}

export default App;

