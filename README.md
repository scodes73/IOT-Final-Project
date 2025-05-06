Here is the `README.md` content in **Markdown format**, ready to paste into your GitHub repo:


# 🛡️ Static Security Analysis of Top-Grossing Health & Fitness Android Apps with IoT Connectivity (2025)

This repository contains the full workflow, scripts, and data used for a static security analysis of the top 100 grossing Health & Fitness apps on the U.S. Play Store (as of April 2025). The project evaluates apps against categories from the OWASP MASVS framework using APKHunt.

---

## 📁 Project Structure

```

├── Apps-Top-100-Grossing-Sorted        # Sorted app ID and metadata (from AppFigures)
├── HTML                                # Raw HTML dumps from the 
├── Parser
│   ├── parser.py                       # Static analysis parser
│   └── combined\_report.xlsx            # Final MASVS summary per app
├── Scripts
│   ├── apkpure-dl.sh                   # Script to fetch HTML for each app
│   ├── jq.sh                           # Extract app IDs from snapshot JSON
│   ├── sample_snapshot.json                           # sample snapshot JSON from Appfigures
│   ├── xapk-to-apk.py                  # Convert .xapk to .apk (if applicable)
│   └── xargs-code.sh                   # Utility script for automation

├── Sentiment Embedding for Description
│   └── sentiment\_embedding.py          # Embeds app descriptions (optional)
├── TXT                                 # Parsed MASVS flags per app


````

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/scodes73/IOT-Final-Project
cd health-fitness-security-analysis
````

### 2. Install dependencies and System Environment

Requires: `jq`, `python3`, `bash`, `unzip`, `jadx`, `dex2jar`, `go`, `apktool`, `zipalign`, `apksigner`, `curl`, `jq`


### 3. Extract app IDs from snapshot
Acquire the snapshot.json from AppFigures website, select your filters on the webpage while the dev tools being open, you can get the `snapshot.json`
```bash
bash Scripts/jq.sh Scripts/snapshot_sample.json > app_ids.txt
```

### 4. Fetch APKs from APKPure

```bash
bash Scripts/xargs-code.sh
```
This uses underlying Scripts/apkpure-dl.sh 


### 5. Converting xapk to apk
Run this in your folder where you have .xapk files, uses xapk-to-apk.py from https://github.com/LuigiVampa92/xapk-to-apk
```bash
for i in *.xapk; do python xapk-to-apk.py $i;done
```


### 6. Passing .apk to APKHunt
```bash
go run apkhunt.go -m ~/path-to-your-apk-directory -l
```
This will generate all the .html and .txt files

### 7. Run the parser
Run the parse in the existing folder with all the .txt or change the folder path in parser.py
```bash
python Parser/parser.py 
```

This extracts relevant MASVS findings from HTML into `.txt` files.

### 6. Review aggregated results

The final output is located at:

```
Parser/combined_report.xlsx
```

---

## ✅ MASVS Categories Analyzed

* **MSTG-STORAGE** 
* **MSTG-PLATFORM**
* **MSTG-NETWORK**
* **MSTG-CRYPTO**
* **MSTG-CODE**
* **MSTG-ARCH**
* **MSTG-RESILIENCE**

---

## 🤝 Acknowledgements

* [OWASP MASVS](https://owasp.org/www-project-mobile-security/)

* [APKPure](https://apkpure.com/), [APKMirror](https://apkmirror.com/), [AppFigures](https://appfigures.com/)

* https://github.com/LuigiVampa92/xapk-to-apk

* https://github.com/Cyber-Buddy/APKHunt

* https://gist.github.com/tokland/867814e1a4c50e07037b29eca9da0c5d

---

## ⚠️ Disclaimer

This repository is intended for **research purposes only**. All data was collected from **public sources**. Use responsibly and in accordance with applicable laws.

```

Let me know if you'd like me to generate a matching `requirements.txt`, a license file, or badges for GitHub display.
```
