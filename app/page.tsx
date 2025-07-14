"use client";
import React, { useEffect, useState } from "react";

const DATA_PATHS = [
  "arxiv_ai/2025-07-08-papers.json",
  "github/2025-07-08/top.json",
  "github/2025-07-08/trending.json",
  "github/tracked/th-ch_youtube-music.json",
  "github/tracked/pocketbase_pocketbase.json",
  "github/tracked/rustfs_rustfs.json",
  "github/tracked/smallcloudai_refact.json",
  "github/tracked/dockur_macos.json",
  "github/tracked/ed-donner_llm_engineering.json",
  "github/tracked/humanlayer_12-factor-agents.json",
  "github/tracked/anthropics_prompt-eng-interactive-tutorial.json",
  "github/tracked/CodeWithHarry_Sigma-Web-Dev-Course.json",
  "github/tracked/commaai_openpilot.json",
  "movies/movies_0.csv",
  "movies/movies_1998.csv",
  "movies/movies_2017.csv",
  "movies/movies_2018.csv",
  "songs_2000/songs_2000_data.csv",
];

type GenericObject = Record<string, unknown>;

function Collapsible({ title, children }: { title: string; children: React.ReactNode }) {
  const [open, setOpen] = useState(false);
  return (
    <div style={{ border: "1px solid #ddd", borderRadius: 8, marginBottom: 16, background: "#fafbfc" }}>
      <button
        onClick={() => setOpen((o) => !o)}
        style={{
          width: "100%",
          textAlign: "left",
          padding: 12,
          fontWeight: 600,
          fontSize: 18,
          background: "#f5f6f7",
          border: "none",
          borderRadius: 8,
          cursor: "pointer",
        }}
      >
        {open ? "▼" : "▶"} {title}
      </button>
      {open && <div style={{ padding: 16, fontSize: 15 }}>{children}</div>}
    </div>
  );
}

function renderStructured(data: unknown): React.ReactNode {
  if (Array.isArray(data)) {
    if (data.length === 0) return <span>No data</span>;
    if (typeof data[0] === "object" && data[0] !== null) {
      const keys = Object.keys(data[0] as GenericObject);
      return (
        <div style={{ overflowX: "auto" }}>
          <table style={{ borderCollapse: "collapse", width: "100%", fontSize: 14 }}>
            <thead>
              <tr>
                {keys.map((k) => (
                  <th key={k} style={{ borderBottom: "1px solid #ccc", textAlign: "left", padding: 6 }}>{k}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {(data as GenericObject[]).map((row, i) => (
                <tr key={i} style={{ background: i % 2 ? "#f7f8fa" : undefined }}>
                  {keys.map((k) => (
                    <td key={k} style={{ padding: 6, borderBottom: "1px solid #eee", verticalAlign: "top" }}>{String(row[k])}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
    }
    return (
      <ul style={{ paddingLeft: 20 }}>
        {data.map((item, i) => (
          <li key={i}>{renderStructured(item)}</li>
        ))}
      </ul>
    );
  }
  if (typeof data === "object" && data !== null) {
    return (
      <dl style={{ display: "grid", gridTemplateColumns: "max-content 1fr", gap: 8 }}>
        {Object.entries(data as GenericObject).map(([k, v]) => (
          <React.Fragment key={k}>
            <dt style={{ fontWeight: 600 }}>{k}</dt>
            <dd style={{ margin: 0 }}>{renderStructured(v)}</dd>
          </React.Fragment>
        ))}
      </dl>
    );
  }
  return <span>{String(data)}</span>;
}

export default function Home() {
  const [data, setData] = useState<Record<string, unknown>>({});
  const [loading, setLoading] = useState<Record<string, boolean>>({});
  const [error, setError] = useState<Record<string, string>>({});

  useEffect(() => {
    DATA_PATHS.forEach((p) => {
      setLoading((l) => ({ ...l, [p]: true }));
      fetch(`/api/${p}`)
        .then((res) => {
          if (!res.ok) throw new Error(res.statusText);
          return res.json();
        })
        .then((d) => setData((dt) => ({ ...dt, [p]: d })))
        .catch((e) => setError((er) => ({ ...er, [p]: e.message })))
        .finally(() => setLoading((l) => ({ ...l, [p]: false })));
    });
  }, []);

  return (
    <main style={{ maxWidth: 900, margin: "40px auto", padding: 24, fontFamily: "Inter, sans-serif" }}>
      <h1 style={{ fontSize: 36, fontWeight: 800, marginBottom: 8 }}>Spidey Data Dashboard</h1>
      <p style={{ color: "#555", marginBottom: 32 }}>Fast, clean view of all scraped JSON/CSV data files.</p>
      {DATA_PATHS.map((p) => (
        <Collapsible key={p} title={p}>
          {loading[p] && <span>Loading...</span>}
          {error[p] && <span style={{ color: "#c00" }}>Error: {error[p]}</span>}
          {!loading[p] && !error[p] && renderStructured(data[p])}
        </Collapsible>
      ))}
    </main>
  );
} 