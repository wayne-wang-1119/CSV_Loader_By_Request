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

  // Dynamically generate table headers based on the keys of the first result object
  const generateHeaders = () => {
    if (results.length > 0) {
      return Object.keys(results[0]).map((key) => <th key={key}>{key}</th>);
    }
    return null;
  };

  // Dynamically generate table rows and columns based on results
  const generateRows = () => {
    return results.map((result, index) => (
      <tr key={index}>
        {Object.values(result).map((value, valueIndex) => (
          <td key={valueIndex}>{value.toString()}</td>
        ))}
        <td>
          <button onClick={() => handleFeedback(index, "thumbs up")}>👍</button>
          <button onClick={() => handleFeedback(index, "thumbs down")}>
            👎
          </button>
        </td>
      </tr>
    ));
  };

  // Example function to handle thumbs up/down actions
  const handleFeedback = (index, feedback) => {
    console.log(`Feedback for index ${index}: ${feedback}`);
    // Implement feedback logic here, possibly sending feedback to your backend
  };

  return (
    <div>
      <h2>Evaluation Results</h2>
      <table>
        <thead>
          <tr>
            {generateHeaders()}
            <th>Feedback</th>
          </tr>
        </thead>
        <tbody>{generateRows()}</tbody>
      </table>
    </div>
  );
}

export default EvaluationReport;
