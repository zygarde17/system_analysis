\# System Resource Utilization Monitor



\*\*Overview\*\*  

This dashboard project collects system metrics (CPU, RAM, Disk, per-process CPU/RAM/Disk I/O) every minute using a Python script and visualizes the data in Power BI.



\*\*What it contains\*\*

\- `Python/system\_monitor.py` — Python script that logs system and per-process stats.

\- `PowerBI/` — (optional) Power BI files (.pbix or .pbit)

\- `README.md` — this file

\- `.gitignore` — excludes logs and large data files



\*\*Methods \& Tools\*\*

\- Data collection: `psutil`, `pandas`, `schedule`

\- Automation: Windows Startup / Task Scheduler (or pythonw)

\- Visualization: Power BI Desktop



\*\*How to run locally\*\*

1\. Create a Python venv and install deps:

&nbsp;  ```bash

&nbsp;  pip install -r requirements.txt







