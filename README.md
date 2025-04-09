# Christchurch Kids Play Map

## Project Overview

**Christchurch Kids Play Map** is an interactive map application for the **Canterbury** region, which showcases parks, walking tracks, bike tracks, recreation centers, and other child-friendly facilities. The map helps parents easily find playgrounds and recreational spaces based on various needs, such as the number of playground facilities, Google ratings, types of play equipment, and proximity.

### Project Goals:
- Provide an interactive map displaying all parks, walking tracks, bike paths, and other recreation areas.
- Filter and recommend locations based on amenities, ratings, and other criteria.
- Visualize data to make it easier for users to browse and choose suitable places.

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (using Leaflet.js or other mapping libraries)
- **Backend**: Python (for data processing and analysis)
- **Data Source**: Open datasets from Canterbury (GeoJSON, Shapefile)
- **Database**: None (data stored in files)

---

## Project Structure

```plaintext
MapProject/
├── data/
│   ├── geojson/           ← Store all GeoJSON files
│   └── shapefile/         ← Store all Shapefile files
├── scripts/               ← Python scripts
│   └── generate_links.py  ← Script to generate Google Maps links
├── outputs/               ← Output files like CSVs, logs, temporary files
├── notebooks/             ← Jupyter Notebooks (optional)
├── webapp/                ← Web application for interactive map
│   ├── index.html
│   ├── map.js
│   └── style.css
├── README.md              ← Project description and usage guide
├── .gitignore             ← Files to ignore in Git
└── requirements.txt       ← Python dependencies for the project
```

## Installation and Setup
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Christchurch-Kids-PlayMap.git
cd Christchurch-Kids-PlayMap
```


### 2. Set up a virtual environment and install dependencies
```bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
## Usage Guide
1.Run the generate_links.py script to generate Google Maps links for all parks and play facilities.

2.Open webapp/index.html to view the interactive map.

## Data Sources
Public datasets for the Canterbury region, available at: [canterburymaps.govt.nz](https://www.canterburymaps.govt.nz/)

## Contributing
We welcome pull requests to contribute code or suggestions. If you encounter issues, please report them via the Issues section.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

