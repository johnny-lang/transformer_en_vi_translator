import React, { useState } from "react";
import axios from "axios";

function App() {
  const [inputText, setInputText] = useState("");
  const [translatedText, setTranslatedText] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleTranslate = async () => {
    if (!inputText.trim()) return; // Không gửi request nếu input rỗng

    setLoading(true);
    setError("");

    try {
      const response = await axios.post("http://127.0.0.1:8000/translate/", {
        text: inputText,
      });

      setTranslatedText(response.data.translated_text);
    } catch (error) {
      setError("Translation failed. Please try again.");
      console.error("Translate Error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Translator</h1>

      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Input Text..."
        rows="5"
        cols="60"
      />

      <br />
      <button onClick={handleTranslate} disabled={loading} style={{ margin: "10px", padding: "10px" }}>
        {loading ? "Translating..." : "Translate"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <h1>Result:</h1>
      <textarea
        value={translatedText}
        readOnly
        placeholder="Translation Output..."
        rows="5"
        cols="60"
      />
    </div>
  );
}

export default App;
