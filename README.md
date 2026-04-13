# 📦 Procurement Intelligence Dashboard

> An interactive, self-contained procurement analytics dashboard built with vanilla HTML, CSS, and Chart.js — no backend required.

[![Data](https://img.shields.io/badge/dataset-777%20POs-blue?style=flat-square)](data/Procurement_KPI_Analysis_Dataset.csv)
[![Period](https://img.shields.io/badge/period-2022--2023-orange?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

---

## 🔗 Live Demo

Open `index.html` in any browser — no server needed.

---

## 📊 Dashboard Features

### KPI Summary Cards
| Metric | Value |
|---|---|
| Total Spend | $49.3M |
| Cost Savings (Negotiated) | $3.93M (7.97%) |
| Avg Defect Rate | 6.5% |
| Compliance Rate | 83% |
| Order Count | 777 POs |

### Visualizations
- **Monthly Spend & Savings Trend** — dual-axis line chart with defect rate overlay (Jan 2022 – Jan 2024)
- **Category Spend Breakdown** — interactive donut chart (5 categories)
- **Defect Rate by Supplier** — horizontal bar chart with risk-colored bars
- **Compliance Rate by Supplier** — horizontal bar chart with threshold coloring
- **Order Status Mix** — pie chart (Delivered / Pending / Partial / Cancelled)
- **Supplier Spend vs. Savings** — grouped bar chart
- **Price Inflation** — unit price vs. negotiated price by quarter
- **Risk Scatter Matrix** — Defect Rate × Compliance positioning per supplier

### Supplier Scorecard Table
Full comparison of all 5 suppliers with:
- Total spend & savings %
- Defect rate with mini progress bar
- Compliance rate with mini progress bar
- Risk classification (LOW / MEDIUM / HIGH)

### Filters
- Filter by supplier, category, order status, and year
- KPI cards update dynamically on supplier selection
- Reset button restores all views

---

## 🗂 Project Structure

```
procurement-dashboard/
├── index.html                          # Main dashboard (self-contained)
├── data/
│   └── Procurement_KPI_Analysis_Dataset.csv   # Source dataset
├── scripts/
│   └── analysis.py                     # Python KPI analysis script
├── README.md
└── LICENSE
```

---

## 📁 Dataset Overview

**File:** `data/Procurement_KPI_Analysis_Dataset.csv`  
**Records:** 777 purchase orders  
**Period:** January 2022 – January 2024

| Column | Type | Description |
|---|---|---|
| `PO_ID` | string | Unique purchase order ID |
| `Supplier` | categorical | One of 5 anonymized suppliers |
| `Order_Date` | date | Date PO was placed |
| `Delivery_Date` | date | Actual delivery date (may be null) |
| `Item_Category` | categorical | MRO / Electronics / Office Supplies / Raw Materials / Packaging |
| `Order_Status` | categorical | Delivered / Pending / Partially Delivered / Cancelled |
| `Quantity` | integer | Units ordered |
| `Unit_Price` | float | Market/list price per unit |
| `Negotiated_Price` | float | Final agreed price per unit |
| `Defective_Units` | float | Number of defective units (null if not delivered) |
| `Compliance` | boolean | Yes/No — policy compliance |

---

## 🏭 Supplier Summary

| Supplier | Orders | Spend | Defect Rate | Compliance | Risk |
|---|---|---|---|---|---|
| Alpha_Inc | 141 | $8.5M | 1.8% | 94% | 🟢 LOW |
| Beta_Supplies | 156 | $10.7M | 7.4% | 76% | 🟡 MEDIUM |
| Delta_Logistics | 171 | $10.0M | **10.6%** | **61%** | 🔴 HIGH |
| Epsilon_Group | 166 | $10.7M | 2.6% | **98%** | 🟢 LOW |
| Gamma_Co | 143 | $9.3M | 4.5% | 86% | 🟡 MEDIUM |

---

## 🐍 Python Analysis Script

For deeper analysis, run the standalone Python script:

```bash
pip install pandas numpy
python scripts/analysis.py
```

Outputs:
- Global KPIs
- Supplier performance breakdown
- Category spend summary
- Monthly trends
- Quarterly price inflation
- Compliance violations by supplier

---

## 🚀 Getting Started

### Option 1 — Open Directly (Recommended)
```bash
git clone https://github.com/YOUR_USERNAME/procurement-dashboard.git
cd procurement-dashboard
open index.html      # macOS
start index.html     # Windows
xdg-open index.html  # Linux
```

### Option 2 — Local Server
```bash
# Python 3
python -m http.server 8000
# then open http://localhost:8000
```

### Option 3 — GitHub Pages
1. Push to GitHub
2. Go to **Settings → Pages**
3. Set source to `main` branch, `/ (root)`
4. Your dashboard is live at `https://YOUR_USERNAME.github.io/procurement-dashboard`

---

## 💡 Key Insights

1. **Delta_Logistics** is the highest-risk supplier with a 10.6% defect rate and only 61% compliance — immediate review recommended.
2. **Epsilon_Group** is the benchmark supplier: 98% compliance, 2.6% defect rate, $845K in negotiated savings.
3. **March 2023** was the peak spend month at $3.03M, with $290K in savings — the highest single-month negotiation outcome.
4. Inflationary pressure is visible in the Unit Price trend: avg prices rose ~36% from Q1 2022 to Q4 2023.
5. Negotiated prices tracked inflation closely, maintaining a ~$5–8 spread and consistent 7–9% savings.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Markup | HTML5 |
| Styling | CSS3 (custom properties, grid, flexbox) |
| Charts | [Chart.js 4.4.1](https://www.chartjs.org/) |
| Fonts | Google Fonts (Syne + DM Mono) |
| Analysis | Python 3 + pandas |

No build step. No dependencies to install for the dashboard.

---

## 📄 License

MIT — free to use, fork, and adapt.
