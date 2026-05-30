https://www.whitehouse.gov/wp-content/themes/whitehouse/static-assets/flourish/flourish-geo-embed/map/index.html

White House map (Flourish viz `22588820`) of **immigration-enforcement arrests by location**, covering **01/21/25 – 05/28/26** (inauguration day through the day before today).


| file | size | what |
|---|---|---|
| `index.html` | 4.2 MB | raw scraped page |
| `arrests_events.csv` | 1.2 MB | **8,218 arrest locations** — the real data |
| `arrests_points.geojson` | 3.0 MB | same points as GeoJSON for mapping |
| `flourish_data_full.json` | 2.7 MB | full parsed dump (all 4 datasets + column names + settings) |
| `extract_data.py` | — | the balanced-brace extractor |

**The data (`arrests_events.csv`)**

Columns: `Neighborhood`, `Latitude`, `Longitude`, `Total Arrests`, `Dates of Arrest`, `Criminal Charges`, `Countries of Origin`, `Gang Affiliation` (the last is a ✅ flag).

- **8,218** points · **206,333** total arrests · max **5,921** at a single point
- Top locations: Laredo 5,921 · San Antonio 4,759 · Dallas 4,666 · Miami 4,395 · Houston 4,204 · New York 3,640 · San Diego 2,809 · Chantilly VA 2,748 · Newark 2,548
- Each row lists the full charge categories and country-of-origin list for that location (e.g. Laredo: Colombia, Cuba, El Salvador, Ghana, Guatemala, Honduras, Mali, Mexico, Nicaragua, Peru, Spain, Sweden, Tonga, Venezuela).
