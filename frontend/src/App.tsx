import { useState } from "react";
import "./App.css";

function App() {
  const [owner, setOwner] = useState("");
  const [repo, setRepo] = useState("");
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const analyzeRepository = async () => {
    if (!owner || !repo) {
      alert("Enter owner and repository name");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/summary/${owner}/${repo}`
      );

      const result = await response.json();

      setData(result);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch repository");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Software Archaeologist</h1>

      <div className="form">
        <input
          placeholder="Repository Owner (e.g. facebook)"
          value={owner}
          onChange={(e) => setOwner(e.target.value)}
        />

        <input
          placeholder="Repository Name (e.g. react)"
          value={repo}
          onChange={(e) => setRepo(e.target.value)}
        />

        <button onClick={analyzeRepository}>
          {loading ? "Analyzing..." : "Analyze Repository"}
        </button>
      </div>

      {data && (
        <div className="results">
          <h2>{data.repository}</h2>

          <p>{data.description}</p>

          <div className="card">
            <strong>Stars:</strong> {data.stars}
          </div>

          <div className="card">
            <strong>Forks:</strong> {data.forks}
          </div>

          <div className="card">
            <strong>Health Score:</strong> {data.health_score}
          </div>

          <div className="card">
            <strong>Languages:</strong>

            <ul>
              {data.top_languages.map((lang: string) => (
                <li key={lang}>{lang}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;