# cloud_migration_planner.py
import pandas as pd

# Define sample cloud service data (can be extended)
cloud_services = [
    {
        "Provider": "AWS",
        "Compute": 0.05,      # $ per hour
        "Storage": 0.023,     # $ per GB per month
        "Latency": 50,        # ms
        "Availability": 99.9  # %
    },
    {
        "Provider": "Azure",
        "Compute": 0.045,
        "Storage": 0.020,
        "Latency": 55,
        "Availability": 99.95
    },
    {
        "Provider": "GCP",
        "Compute": 0.048,
        "Storage": 0.026,
        "Latency": 60,
        "Availability": 99.9
    }
]

# Convert to DataFrame for easy comparison
df = pd.DataFrame(cloud_services)

# User input: weight of each parameter in decision (sum to 1.0)
weights = {
    "Compute": 0.4,
    "Storage": 0.2,
    "Latency": 0.2,
    "Availability": 0.2
}

# Normalize parameters (lower is better for cost/latency, higher better for availability)
df["Compute_score"] = 1 / df["Compute"]
df["Storage_score"] = 1 / df["Storage"]
df["Latency_score"] = 1 / df["Latency"]
df["Availability_score"] = df["Availability"]  # Already higher is better

# Weighted score
df["Total_score"] = (
    df["Compute_score"] * weights["Compute"] +
    df["Storage_score"] * weights["Storage"] +
    df["Latency_score"] * weights["Latency"] +
    df["Availability_score"] * weights["Availability"]
)

# Sort and display best option
df_sorted = df.sort_values(by="Total_score", ascending=False)
print("=== Cloud Service Comparison ===")
print(df_sorted[["Provider", "Total_score"]])

# Optional: save to CSV for reporting
df_sorted.to_csv("cloud_service_comparison.csv", index=False)
