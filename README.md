https://www.whitehouse.gov/wp-content/themes/whitehouse/static-assets/flourish/flourish-geo-embed/map/index.html

*Newly added:** an ealier version of the map, whioch appears to be the same version which was the subject of [prior reporting by Maddy Varner Dell Cameron for Wired](https://www.wired.com/story/white-house-aliens-gov-us-citizens-arrested/). 

"In a statement provided post-publication, the White House said aliens.gov “pulls data directly from DHS, which initially included a handful of non-immigration HSI arrests,” adding that “this has been updated.” HSI, or Homeland Security Investigations, is a part of ICE. WIRED reviewed the updated data and found there were 270,214 fewer arrests listed."

This earlier data was obtained from a wayback machine snapshot and is is the _2026-05-29 versions in this repo. 

If you want to work with the pre-scrub set the file you want is "flourish_data_full_PRESCRUB_2026-05-29.json" otherwise 'flourish_data_full.json.' 

The difference looks to confirm number reproduces WIRED's reporting exactly:
  - 476,547 − 206,333 = 270,214 — the precise removal figure the White House admitted to.
  - 715 cells name a US-born ("UNITED STATES") arrestee — WIRED said 715. ✓
  - 83 cells where every arrestee is American — WIRED said 83. ✓
  - One cell lists Puerto Rico as a country of origin. ✓

  What the scrub actually did (the diff)

  This is something the article didn't break down — and it's more revealing than "they deleted some rows":
  - 3,725 cells deleted entirely (123 of which named US citizens)
  - 70 cells added
  - 5,221 surviving cells had their arrest counts revised downward (net −257,246)

*The information below is based on the later scrape of the same map.* Still working on this will update shortly. 
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
