import { useState } from 'react';
import axios from 'axios';

export default function Dashboard() {
  const [log, setLog] = useState('');
  const [result, setResult] = useState(null);

  const analyze = async () => {
    const response = await axios.post('http://127.0.0.1:5000/analyze', {
      log
    });

    setResult(response.data);
  };

  return (
    <div style={{padding:'40px'}}>
      <h1>SELF-HEALING AI SYSTEM</h1>

      <textarea
        rows='10'
        cols='80'
        value={log}
        onChange={(e)=>setLog(e.target.value)}
      />

      <br/><br/>

      <button onClick={analyze}>
        ANALYZE
      </button>

      {result && (
        <div>
          <h2>RESULT</h2>
          <p>Error: {result.error_type}</p>
          <p>Action: {result.action}</p>
          <p>Status: {result.status}</p>
        </div>
      )}
    </div>
  );
}
