export default function IncidentDetail({ incident, onBack, onRCA }) {
  if (!incident) return null;

  return (
    <div>
      <button onClick={onBack}>Back</button>

      <h2>Incident Detail</h2>

      <p>ID: {incident.id}</p>
      <p>Component: {incident.component_id}</p>
      <p>Status: {incident.status}</p>
      <p>Severity: {incident.severity}</p>

      <button onClick={onRCA}>Submit RCA</button>
    </div>
  );
}