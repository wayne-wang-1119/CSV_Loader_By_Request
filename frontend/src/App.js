import React, { useState } from "react";
import { uploadFile, submitPrompt } from "./api";

function App() {
  const [prompt, setPrompt] = useState("");
  const [filePath, setFilePath] = useState("");

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (file) {
      const path = await uploadFile(file);
      setFilePath(path);
    }
  };

  const handleSubmit = async () => {
    if (prompt && filePath) {
      console.log("Submit prompt and file path:", prompt, filePath);
      submitPrompt(prompt, filePath);
    } else {
      alert("Please upload a file and enter a prompt.");
    }
  };

  return (
    <div>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your prompt here"
        rows="10"
        cols="50"
      ></textarea>
      <br />
      <input type="file" onChange={handleFileChange} />
      <br />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default App;
