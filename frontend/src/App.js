import './App.css';
import axios from 'axios';
import React, { useState } from 'react';
 
function App() {
  const [values, setValues] = useState({ val1: '', val2: '', val3: '' });
  const [totalSum, setTotalSum] = useState('');
 
  const handleChange = (event) => {
    const { name, value } = event.target;
    setValues({ ...values, [name]: value });
  };
 
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://192.168.0.120:5000/calculate_sum', { values: Object.values(values) });
      setTotalSum(response.data.total_sum);
    } catch (error) {
      console.error(error);
      setTotalSum('Error occurred');
    }
  };
 
  return (
    <div className="container">
      <h1 className="my-4">Sum Calculator</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Value 1:</label>
          <input
            type="number"
            className="form-control"
            name="val1"
            value={values.val1}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Value 2:</label>
          <input
            type="number"
            className="form-control"
            name="val2"
            value={values.val2}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Value 3:</label>
          <input
            type="number"
            className="form-control"
            name="val3"
            value={values.val3}
            onChange={handleChange}
          />
        </div>
        <button type="submit" className="btn btn-primary">Calculate Sum</button>
      </form>
      <div className="mt-4">
        <strong>Total Sum:</strong> {totalSum}
      </div>
    </div>
  );
}
 
export default App;
