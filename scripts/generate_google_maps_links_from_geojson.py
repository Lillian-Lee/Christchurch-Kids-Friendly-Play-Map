import geopandas as gpd
import pandas as pd
import os

# Set the folder path that contains the GeoJSON files
folder_path = "your_folder_path_here"  # ← Replace this with the actual folder path
output_list = []

# Loop through all .geojson files in the folder
for file in os.listdir(folder_path):
    if file.endswith(".geojson"):
        file_path = os.path.join(folder_path, file)
        try:
            gdf = gpd.read_file(file_path)

            # Ensure the coordinate reference system is WGS84 (latitude/longitude)
            if gdf.crs != "EPSG:4326":
                gdf = gdf.to_crs("EPSG:4326")

            # Extract latitude and longitude from geometry
            gdf["latitude"] = gdf.geometry.y
            gdf["longitude"] = gdf.geometry.x
            gdf["source_file"] = file

            # Generate Google Maps link for each feature
            gdf["Google_Maps_Link"] = gdf.apply(
                lambda row: f"https://www.google.com/maps/search/?api=1&query={row['latitude']},{row['longitude']}",
                axis=1
            )

            # Attempt to detect a name column
            name_col = None
            for col in gdf.columns:
                if "name" in col.lower():
                    name_col = col
                    break

            # Use detected name column, or generate placeholder names
            gdf["Name"] = gdf[name_col] if name_col else [f"{file}_#{i+1}" for i in range(len(gdf))]

            # Select columns for export
            export_df = gdf[["Name", "latitude", "longitude", "Google_Maps_Link", "source_file"]]
            output_list.append(export_df)

        except Exception as e:
            print(f"⚠️ Failed to read {file}: {e}")

# Concatenate and export all data into a single CSV
if output_list:
    result_df = pd.concat(output_list, ignore_index=True)
    result_df.to_csv("All_GeoJSON_Points_With_GoogleMaps.csv", index=False)
    print("✅ Exported to All_GeoJSON_Points_With_GoogleMaps.csv")
else:
    print("❌ No valid GeoJSON files were processed. Please check the folder path and file formats.")
