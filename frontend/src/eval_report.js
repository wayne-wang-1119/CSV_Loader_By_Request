import React, { useState, useEffect } from "react";

function EvaluationReport() {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/eval/evaluation_results")
      .then((response) => response.json())
      .then((data) => setResults(data))
      .catch((error) =>
        console.error("Error fetching evaluation results:", error)
      );
  }, []);
  console.log(results);

  return (
    <div>
      <h2>Evaluation Results</h2>
      <table>
        <thead>
          <tr>
            <th>Index</th>
            <th>Result</th>
          </tr>
        </thead>
        <tbody>
          {results.map((result, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{result.Result}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EvaluationReport;
