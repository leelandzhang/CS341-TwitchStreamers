import pandas as pd

# Load the features and edges files
features = pd.read_csv("filtered_twitch_features.csv")
edges = pd.read_csv("filtered_twitch_edges.csv")

# Verify if the features file is sorted by numeric_id
is_sorted = features["numeric_id"].is_monotonic_increasing
print(f"Is the features file sorted by numeric_id? {is_sorted}")

if is_sorted:
    # Generate the mapping
    id_mapping = {
        old_id: new_id for new_id, old_id in enumerate(features["numeric_id"], start=1)
    }

    # Overwrite the numeric_id in the features file with the new IDs
    features["numeric_id"] = features["numeric_id"].map(id_mapping)

    # Update numeric_id_1 and numeric_id_2 in the edges file using the mapping
    edges["numeric_id_1"] = edges["numeric_id_1"].map(id_mapping)
    edges["numeric_id_2"] = edges["numeric_id_2"].map(id_mapping)

    # Save the updated features and edges files
    features.to_csv("mapped_twitch_features.csv", index=False)
    edges.to_csv("mapped_twitch_edges.csv", index=False)

    # Optionally, save the mapping to a file for reference
    pd.DataFrame(list(id_mapping.items()), columns=["original_id", "new_id"]).to_csv(
        "id_mapping.csv", index=False
    )

else:
    print(
        "Please make sure that the features data file is "
        "sorted in increasing order by 'numeric_id'!"
    )
