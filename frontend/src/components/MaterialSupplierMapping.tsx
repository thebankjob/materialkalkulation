// Basisgerüst für die Material-Lieferant-Mapping Tabelle
import React, { useEffect, useState } from "react";
import api from "../api";

type Mapping = {
  id: number;
  material_id: number;
  lieferant_id: number;
  artikelnummer?: string;
  verpackungseinheit?: string;
  kommentar?: string;
};

const MaterialSupplierMapping: React.FC = () => {
  const [mappings, setMappings] = useState<Mapping[]>([]);

  useEffect(() => {
    api
      .get("/material_lieferant")
      .then((res) => setMappings(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h2>Material-Lieferant Mapping</h2>
      <table>
        <thead>
          <tr>
            <th>Material-ID</th>
            <th>Lieferant-ID</th>
            <th>Artikelnummer</th>
            <th>Verpackungseinheit</th>
            <th>Kommentar</th>
          </tr>
        </thead>
        <tbody>
          {mappings.map(m => (
            <tr key={m.id}>
              <td>{m.material_id}</td>
              <td>{m.lieferant_id}</td>
              <td>{m.artikelnummer}</td>
              <td>{m.verpackungseinheit}</td>
              <td>{m.kommentar}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MaterialSupplierMapping;
