if len(line) > 24:
    time_start = line[3:22]
    print time_start
    timeArray = time.strptime(time_start, "%Y-%m-%d %H:%M:%S")
    if timeArray >= start_Time:
        plugin_Line.append(line)
if start_Time in line:
    line = str(line)
    plugin_Line.append(line)