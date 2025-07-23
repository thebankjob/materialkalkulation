import React, { useEffect, useState } from "react";
import axios from "axios";

type Material = {
  id: number;
  name: string;
  einheit: string;
  kategorie?: string;
  technische_eigenschaften?: string;
};

const MaterialTable: React.FC = () => {
  const [materialien, setMaterialien] = useState<Material[]>([]);

  useEffect(() => {
    axios.get("/api/materialien")
      .then(res => setMaterialien(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Materialien</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Kategorie</th>
            <th>Einheit</th>
            <th>Technische Eigenschaften</th>
          </tr>
        </thead>
        <tbody>
          {materialien.map(m => (
            <tr key={m.id}>
              <td>{m.name}</td>
              <td>{m.kategorie}</td>
              <td>{m.einheit}</td>
              <td>{m.technische_eigenschaften}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MaterialTable;
