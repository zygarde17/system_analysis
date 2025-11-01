import psutil
import pandas as pd
import datetime
import os
import schedule
import time

def log_system_data():
    # Define paths
    base_dir = r"E:\System Analysis"
    data_folder = os.path.join(base_dir, "Data")
    csv_file = os.path.join(data_folder, "system_usage.csv")

    # Create folder if it doesn't exist
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Get timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Collect system stats
    cpu_total = psutil.cpu_percent(interval=1)
    ram_total = psutil.virtual_memory().percent
    disk_total = psutil.disk_usage('/').percent

    # Collect process-level stats
    process_data = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            io_counters = proc.io_counters() if proc.io_counters() else None
            read_bytes = io_counters.read_bytes if io_counters else 0
            write_bytes = io_counters.write_bytes if io_counters else 0

            process_data.append([
                timestamp,
                cpu_total,
                ram_total,
                disk_total,
                proc.info['name'],
                proc.info['cpu_percent'],
                proc.info['memory_percent'],
                read_bytes,
                write_bytes
            ])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    # Create DataFrame
    df = pd.DataFrame(process_data, columns=[
        "Timestamp",
        "Total_CPU(%)",
        "Total_RAM(%)",
        "Total_Disk(%)",
        "Process_Name",
        "Process_CPU(%)",
        "Process_RAM(%)",
        "Disk_Read_Bytes",
        "Disk_Write_Bytes"
    ])

    # Write or append to CSV file
    if not os.path.isfile(csv_file):
        df.to_csv(csv_file, index=False)
    else:
        df.to_csv(csv_file, mode='a', header=False, index=False)

    print(f"Logged {len(process_data)} processes at {timestamp}")
    print(f"Saved in: {csv_file}")

# Schedule every 1 minute
schedule.every(1).minutes.do(log_system_data)

print(" System monitoring started... saving data in E:\\System Analysis\\Data\\system_usage.csv\n")

while True:
    schedule.run_pending()
    time.sleep(1)
