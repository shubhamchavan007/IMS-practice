import { useEffect, useState } from "react";
import { getIncidents } from "../services/api";

export default function Dashboard({ onSelect }) {
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    getIncidents().then(setIncidents);
  }, []);

  return (
    <div>
      <h2>Incidents</h2>
      {incidents.map((i) => (
        <div
          key={i.id}
          onClick={() => onSelect(i)}
          style={{ border: "1px solid black", margin: 10, padding: 10 }}
        >
          <p>Component: {i.component_id}</p>
          <p>Status: {i.status}</p>
          <p>Severity: {i.severity}</p>
        </div>
      ))}
    </div>
  );
}