const BASE_URL = "http://localhost:8000";

export async function getIncidents() {
  const res = await fetch(`${BASE_URL}/incidents`);
  return res.json();
}

export async function submitRCA(data) {
  const res = await fetch(`${BASE_URL}/rca`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}