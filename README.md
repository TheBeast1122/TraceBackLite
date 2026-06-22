# TracebackLite

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![DFIR](https://img.shields.io/badge/DFIR-Digital%20Forensics-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## Overview

TracebackLite is a lightweight Digital Forensics and Incident Response (DFIR) tool developed in Python that collects forensic artifacts from multiple Windows sources and correlates them into a unified investigative timeline.

Rather than presenting isolated events, TracebackLite reconstructs user activity by combining evidence from browser history, Windows Event Logs, Registry artifacts, USB device history, Prefetch execution records, and Recycle Bin artifacts. This helps investigators understand the sequence of actions performed on a system during an incident.

## Key Features

* Browser History Analysis
* Windows Event Log Collection
* Registry Artifact Extraction
* USB Device History Detection
* Prefetch File Analysis
* Recycle Bin Investigation
* Unified Timeline Generation
* CSV and JSON Export Support
* Investigator-Friendly Event Correlation

## Why TracebackLite?

Most beginner forensic tools simply export individual artifacts.

TracebackLite focuses on timeline-based investigation by bringing multiple forensic sources together into a single chronological view.

### Example Timeline

| Time  | Source      | Activity             |
| ----- | ----------- | -------------------- |
| 16:42 | Browser     | Visited website      |
| 16:45 | Prefetch    | Application executed |
| 16:47 | USB History | USB device inserted  |
| 16:50 | Recycle Bin | File deleted         |

This allows investigators to quickly understand what happened, when it happened, and how different artifacts relate to each other.

## Supported Artifacts

### Browser Artifacts

* Chrome History
* Edge History
* Firefox History (planned)

### Windows Artifacts

* Event Logs
* Registry Keys
* User Activity Records

### Execution Artifacts

* Prefetch Files

### Device Artifacts

* USB Connection History

### File System Artifacts

* Recycle Bin Entries

## Project Structure

```text
TracebackLite/
│
├── modules/
│   ├── browser_history.py
│   ├── event_logs.py
│   ├── registry_parser.py
│   ├── usb_history.py
│   ├── prefetch_parser.py
│   └── recycle_bin.py
│
├── reports/
│
├── output/
│
├── tracebacklite.py
│
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/TracebackLite.git
cd TracebackLite
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the tool:

```bash
python tracebacklite.py
```

Generate a timeline:

```bash
python tracebacklite.py --timeline
```

Export results:

```bash
python tracebacklite.py --export csv
```

## Sample Output

```text
[2026-06-12 16:42] Browser      - Visited website
[2026-06-12 16:45] Prefetch     - FTK Imager executed
[2026-06-12 16:47] USB          - Kingston USB inserted
[2026-06-12 16:50] Recycle Bin  - suspicious_file.zip deleted
```

## Use Cases

* Digital Forensics Investigations
* Incident Response
* Malware Analysis Support
* Insider Threat Investigations
* Academic DFIR Research
* Cybersecurity Learning Projects

## Future Roadmap

* Master File Table (MFT) Parsing
* Jump Lists Analysis
* SRUM Analysis
* Automatic Artifact Correlation
* HTML/PDF Report Generation
* GUI Dashboard
* Timeline Visualization
* Evidence Scoring System

## Author

Aditya Singh

Cybersecurity Enthusiast | Digital Forensics Learner | DFIR Researcher

## Disclaimer

This project is intended for educational, research, and authorized forensic investigation purposes only. Users are responsible for complying with applicable laws, organizational policies, and ethical guidelines.
