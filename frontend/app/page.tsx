"use client";

import { useEffect, useState } from "react";

type Overview = { product_name: string; pitch: string; problem: string; target_users: string[]; features: string[]; demo_data: boolean };
const apiUrl = "https://run-an-compass-15c5604-public-api.onrender.com";

export default function Home() {
  const [overview, setOverview] = useState<Overview | null>(null);
  const [error, setError] = useState("");
  useEffect(() => {
    fetch(`${apiUrl}/api/overview`).then(async (response) => {
      if (!response.ok) throw new Error("The MVP API is starting up. Try again shortly.");
      setOverview(await response.json() as Overview);
    }).catch((caught: unknown) => setError(caught instanceof Error ? caught.message : "Could not load the demo."));
  }, []);
  return <main><section className="hero"><p className="eyebrow">GENESIS-GENERATED MVP</p><h1>Run An Compass</h1><p className="lede">Run An Compass helps merchant, sales, and customer-success teams turn scattered evidence into a human-approved next action and prove whether the workflow improves a measurable outcome.</p><a href="#workflow">Explore the workflow ↓</a><a href="/pitch">View the investor pitch →</a></section><section id="workflow" className="panel">{error ? <p className="error">{error}</p> : !overview ? <p>Loading your live MVP…</p> : <><p className="eyebrow">THE FIRST WEDGE</p><h2>{overview.problem}</h2><p>Designed for {overview.target_users.join(", ")}.</p><div className="grid">{overview.features.map((feature, index) => <article key={feature}><span>0{index + 1}</span><h3>{feature}</h3><p>A focused, reviewable product slice for the pilot.</p></article>)}</div><p className="note">Demo mode: this launch uses synthetic data and is ready for product validation, not real regulated or customer data.</p></>}</section></main>;
}
