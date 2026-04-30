import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import IncidentDetail from "./pages/IncidentDetail";
import RCAForm from "./pages/RCAForm";

function App() {
  const [page, setPage] = useState("dashboard");
  const [selected, setSelected] = useState(null);

  if (page === "dashboard")
    return (
      <Dashboard
        onSelect={(i) => {
          setSelected(i);
          setPage("detail");
        }}
      />
    );

  if (page === "detail")
    return (
      <IncidentDetail
        incident={selected}
        onBack={() => setPage("dashboard")}
        onRCA={() => setPage("rca")}
      />
    );

  if (page === "rca")
    return (
      <RCAForm
        incident={selected}
        onBack={() => setPage("dashboard")}
      />
    );
}

export default App;