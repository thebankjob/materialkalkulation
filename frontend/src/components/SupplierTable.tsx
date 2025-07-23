import React, { useEffect, useState } from "react";
import axios from "axios";

type Supplier = {
  id: number;
  name: string;
  kontaktinfo?: string;
};

const SupplierTable: React.FC = () => {
  const [lieferanten, setLieferanten] = useState<Supplier[]>([]);

  useEffect(() => {
    axios.get("/api/lieferanten")
      .then(res => setLieferanten(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Lieferanten</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Kontaktinfo</th>
          </tr>
        </thead>
        <tbody>
          {lieferanten.map(l => (
            <tr key={l.id}>
              <td>{l.name}</td>
              <td>{l.kontaktinfo}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default SupplierTable;
