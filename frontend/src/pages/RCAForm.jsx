import { useState } from "react";
import { submitRCA } from "../services/api";

export default function RCAForm({ incident, onBack }) {
  const [rootCause, setRootCause] = useState("");
  const [fix, setFix] = useState("");

  const handleSubmit = async () => {
    await submitRCA({
      work_item_id: incident.id,
      root_cause: rootCause,
      fix: fix,
    });

    alert("RCA Submitted");
    onBack();
  };

  return (
    <div>
      <button onClick={onBack}>Back</button>

      <h2>RCA Form</h2>

      <input
        placeholder="Root Cause"
        value={rootCause}
        onChange={(e) => setRootCause(e.target.value)}
      />

      <br />

      <textarea
        placeholder="Fix Applied"
        value={fix}
        onChange={(e) => setFix(e.target.value)}
      />

      <br />

      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}