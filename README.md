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

## 📊 Live Dashboard Preview

<p align="center">
  <a href="https://app.powerbi.com/view?r=eyJrIjoiYTQ1MGFmYWQtOTFmZi00NDFlLTkxMjQtYThjYTI5MWVjZDBiIiwidCI6IjJmYzg3NDI5LWI0YWItNDVlYi04Yzc1LTA0YjM5MzkzNjg0OSJ9">
    <img src="docs/dashboard_screenshot.png" alt="Live Dashboard" width="800">
  </a>
</p>

live dashboard.


## 📊 Power BI Dashboard Preview

Here’s a glimpse of the **System Resource Utilization Dashboard** built using Power BI:


<img width="1437" height="809" alt="Report" src="https://github.com/user-attachments/assets/f3f5d51a-2832-4b6b-a879-c3a41477879d" />





