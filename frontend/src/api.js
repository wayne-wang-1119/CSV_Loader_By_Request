export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://localhost:5000/data/upload", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) throw new Error("File upload failed");
    const data = await response.json();
    return data.file;
  } catch (error) {
    console.error("Upload error:", error);
    return "";
  }
};

export const submitPrompt = async (prompt, file) => {
  try {
    const response = await fetch("http://localhost:5000/eval/evaluate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt, file }),
    });

    if (!response.ok) throw new Error("Evaluation failed");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Submission error:", error);
  }
};
