"""
Procurement KPI Analysis Script
================================
Analyzes the Procurement_KPI_Analysis_Dataset.csv and outputs
key metrics used to power the interactive dashboard.

Requirements:
    pip install pandas matplotlib seaborn

Usage:
    python scripts/analysis.py
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ── Load Data ──────────────────────────────────────────────────────────────────
DATA_PATH = Path(__file__).parent.parent / "data" / "Procurement_KPI_Analysis_Dataset.csv"
df = pd.read_csv(DATA_PATH)

# Parse dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"], errors="coerce")

# Derived columns
df["Total_Spend"] = df["Quantity"] * df["Unit_Price"]
df["Total_Negotiated"] = df["Quantity"] * df["Negotiated_Price"]
df["Savings"] = df["Total_Spend"] - df["Total_Negotiated"]
df["Lead_Time_Days"] = (df["Delivery_Date"] - df["Order_Date"]).dt.days
df["Defect_Rate"] = df["Defective_Units"] / df["Quantity"]
df["YearMonth"] = df["Order_Date"].dt.to_period("M")
df["Year"] = df["Order_Date"].dt.year

# ── Top-Level KPIs ─────────────────────────────────────────────────────────────
print("=" * 60)
print("GLOBAL KPIs")
print("=" * 60)
total_spend   = df["Total_Spend"].sum()
total_savings = df["Savings"].sum()
avg_defect    = df[df["Order_Status"] == "Delivered"]["Defect_Rate"].mean() * 100
compliance    = (df["Compliance"] == "Yes").mean() * 100
total_orders  = len(df)

print(f"  Total Spend:       ${total_spend:>14,.0f}")
print(f"  Cost Savings:      ${total_savings:>14,.0f}  ({total_savings/total_spend*100:.1f}% of spend)")
print(f"  Avg Defect Rate:   {avg_defect:>13.2f}%")
print(f"  Compliance Rate:   {compliance:>13.1f}%")
print(f"  Total Orders:      {total_orders:>14,}")

# ── Supplier Performance ────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("SUPPLIER PERFORMANCE")
print("=" * 60)

delivered = df[df["Order_Status"] == "Delivered"]
sup = df.groupby("Supplier").agg(
    orders       = ("PO_ID", "count"),
    spend        = ("Total_Spend", "sum"),
    savings      = ("Savings", "sum"),
    compliance   = ("Compliance", lambda x: (x == "Yes").mean() * 100),
).round(2)

defect_by_sup = delivered.groupby("Supplier")["Defect_Rate"].mean() * 100
sup["defect_rate"] = defect_by_sup
sup["savings_pct"]  = sup["savings"] / sup["spend"] * 100

# Risk classification
def classify_risk(row):
    if row["defect_rate"] > 8 or row["compliance"] < 70:
        return "HIGH"
    elif row["defect_rate"] > 5 or row["compliance"] < 85:
        return "MEDIUM"
    return "LOW"

sup["risk"] = sup.apply(classify_risk, axis=1)
print(sup[["orders","spend","savings","savings_pct","defect_rate","compliance","risk"]].to_string())

# ── Category Breakdown ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("SPEND BY CATEGORY")
print("=" * 60)
cat = df.groupby("Item_Category").agg(
    orders = ("PO_ID", "count"),
    spend  = ("Total_Spend", "sum"),
    savings= ("Savings", "sum"),
).sort_values("spend", ascending=False)
cat["savings_pct"] = cat["savings"] / cat["spend"] * 100
print(cat.to_string())

# ── Monthly Trend ──────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("MONTHLY TRENDS (2022-2023)")
print("=" * 60)
monthly = df.groupby("YearMonth").agg(
    orders  = ("PO_ID", "count"),
    spend   = ("Total_Spend", "sum"),
    savings = ("Savings", "sum"),
).sort_index()
monthly["defect_rate"] = df.groupby("YearMonth")["Defect_Rate"].mean() * 100
print(monthly.to_string())

# ── Order Status ───────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("ORDER STATUS DISTRIBUTION")
print("=" * 60)
status = df["Order_Status"].value_counts()
status_pct = (status / len(df) * 100).round(1)
print(pd.DataFrame({"count": status, "pct": status_pct}).to_string())

# ── Compliance Violations ──────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("NON-COMPLIANT ORDERS BY SUPPLIER")
print("=" * 60)
non_compliant = df[df["Compliance"] == "No"].groupby("Supplier").size().sort_values(ascending=False)
print(non_compliant.to_string())

# ── Price Inflation ────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("AVG UNIT PRICE vs NEGOTIATED PRICE (Quarterly)")
print("=" * 60)
df["Quarter"] = df["Order_Date"].dt.to_period("Q")
qtr = df.groupby("Quarter").agg(
    avg_unit = ("Unit_Price", "mean"),
    avg_neg  = ("Negotiated_Price", "mean"),
).round(2)
qtr["spread"] = qtr["avg_unit"] - qtr["avg_neg"]
print(qtr.to_string())

print("\n" + "=" * 60)
print("Analysis complete. See dashboard/index.html for the interactive view.")
print("=" * 60)
