import pandas as pd

# Define input and output file paths
INPUT_FEATURES_FILE = "large_twitch_features.csv"
INPUT_EDGES_FILE = "large_twitch_edges.csv"
OUTPUT_FEATURES_FILE = "filtered_twitch_features2.csv"
OUTPUT_EDGES_FILE = "filtered_twitch_edges2.csv"

# Read the features CSV file into a DataFrame
features_df = pd.read_csv(INPUT_FEATURES_FILE)

# Convert the 'created_at' column to datetime format
features_df["created_at"] = pd.to_datetime(features_df["created_at"])

# Filter the DataFrame for rows where 'created_at' is after 2016-01-01
filtered_features_df = features_df[features_df["created_at"] >= "2018-04-01"]

# Extract the numeric_id values from the filtered features DataFrame
filtered_numeric_ids = set(filtered_features_df["numeric_id"])

# Read the edges CSV file into a DataFrame
edges_df = pd.read_csv(INPUT_EDGES_FILE)

# Filter the edges DataFrame to include only rows where both numeric_id_1
# and numeric_id_2 are in the filtered numeric_ids
filtered_edges_df = edges_df[
    (edges_df["numeric_id_1"].isin(filtered_numeric_ids))
    & (edges_df["numeric_id_2"].isin(filtered_numeric_ids))
]

filtered_numeric_ids_by_edge = set(filtered_edges_df["numeric_id_1"]) | set(
    filtered_edges_df["numeric_id_2"]
)

# After filtering the edges, filter out the nodes that do not have any edges
filtered_features_df = filtered_features_df[
    (filtered_features_df["numeric_id"].isin(filtered_numeric_ids_by_edge))
]

# Write the filtered features DataFrame to a new CSV file
filtered_features_df.to_csv(OUTPUT_FEATURES_FILE, index=False)

# Write the filtered edges DataFrame to a new CSV file
filtered_edges_df.to_csv(OUTPUT_EDGES_FILE, index=False)

print(f"Filtered features data has been saved to {OUTPUT_FEATURES_FILE}")
print(f"Filtered edges data has been saved to {OUTPUT_EDGES_FILE}")
