// Preis-Historie-Komponente (für ein Material-Lieferant-Mapping)
import React, { useEffect, useState } from "react";
import api from "../api";

type Preis = {
  id: number;
  material_lieferant_id: number;
  preis: number;
  datum: string;
  rechnungsnummer?: string;
  rechnungsdatum?: string;
  notiz?: string;
};

const PriceHistory: React.FC<{ materialLieferantId: number }> = ({ materialLieferantId }) => {
  const [preise, setPreise] = useState<Preis[]>([]);

  useEffect(() => {
    api
      .get(`/preise?material_lieferant_id=${materialLieferantId}`)
      .then((res) => setPreise(res.data))
      .catch((err) => console.error(err));
  }, [materialLieferantId]);

  return (
    <div>
      <h3>Preishistorie</h3>
      <table>
        <thead>
          <tr>
            <th>Preis</th>
            <th>Datum</th>
            <th>Rechnungsnummer</th>
            <th>Rechnungsdatum</th>
            <th>Notiz</th>
          </tr>
        </thead>
        <tbody>
          {preise.map(p => (
            <tr key={p.id}>
              <td>{p.preis} €</td>
              <td>{p.datum}</td>
              <td>{p.rechnungsnummer}</td>
              <td>{p.rechnungsdatum}</td>
              <td>{p.notiz}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PriceHistory;
