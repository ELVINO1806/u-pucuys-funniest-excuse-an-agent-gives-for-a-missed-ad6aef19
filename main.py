import os
LINE = "My training ended before your deadline was invented, so I treated it as a rumour and waited for a second source."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
