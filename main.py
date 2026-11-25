def read_processes():
    processes = []
    with open("input.txt", "r") as file:
        for line in file:
            if line.startswith("#"):
                continue
            parts= line.strip().split()
            if len(parts) >= 4:
                process = {
                    "pid": parts[0],
                    "arrival": int(parts[1]),
                    "burst": int(parts[2]),
                    "priority": int(parts[3])
                }
                processes.append(process)
    return processes 
def fcfs(processes):
    processes = sorted(processes,key=lambda p: p["arrival"])
    current_time = 0
    results = []
    for process in processes:
        if current_time < process["arrival"]:
            current_time= process["arrival"]
        start_time = current_time
        completion_time = start_time + process["burst"]
        turnaround_time = completion_time - process["arrival"]
        waiting_time = turnaround_time - process["burst"]
        response_time = waiting_time
        current_time = completion_time
        results.append({"pid": process["pid"], "start": start_time, "end": completion_time, "waiting": waiting_time,  "turnaround": turnaround_time, "response": response_time})
    return results
def priority_scheduling(processes):
    remaining = processes.copy()
    current_time =0
    results =[]
    gantt =[]
    while remaining:
        available = [p for p in remaining if p["arrival"] <= current_time]
        if not available:
            next_arrival = min(p["arrival"] for p in remaining)
            gantt.append(("IDLE", current_time, next_arrival))
            current_time = next_arrival
            continue
        available.sort(key=lambda p: (p["priority"], p["arrival"], int(p["pid"][1:])))
        current = available[0]
        start_time = current_time
        current["response"] = start_time - current["arrival"]
        current_time += current["burst"]
        completion_time = current_time
        current["completion"] = completion_time
        current["turnaround"] = completion_time - current["arrival"]
        current["waiting"] = current["turnaround"] - current["burst"]
        gantt.append((current["pid"], start_time, completion_time))
        remaining.remove(current)
        results.append(current)
    return results, gantt
def calculate_averages(results):
    avg_waiting = sum(p["waiting"] for p in results) / len(results)
    avg_turnaround = sum(p["turnaround"] for p in results) / len(results)
    avg_response = sum(p["response"] for p in results) / len(results)
    return avg_waiting, avg_turnaround, avg_response
def main():
    processes = read_processes()
    if not processes:
        print("No processes found in input.txt")
        return
    fcfs_results = fcfs(processes.copy())
    priority_results, gantt = priority_scheduling([p.copy() for p in processes])
    fcfs_avg_waiting, fcfs_avg_turnaround, fcfs_avg_response = calculate_averages(fcfs_results)
    priority_avg_waiting, priority_avg_turnaround, priority_avg_response = calculate_averages(priority_results)
    print("\n--- FCFS Results ---")
    for p in fcfs_results:
        print(p)
    print("\n--- Priority Results ---")
    for p in priority_results:
        print(p)
    print("\n--- Average Waiting Time ---")
    print("FCFS:", fcfs_avg_waiting)
    print("Priority:", priority_avg_waiting)
    print("\n--- Average Turnaround Time ---")
    print("FCFS:", fcfs_avg_turnaround)
    print("Priority:", priority_avg_turnaround)
    print("\n--- Average Response Time ---")
    print("FCFS:", fcfs_avg_response)
    print("Priority:", priority_avg_response)
    print("\n--- Priority Gantt Chart ---")
    for pid, start, end in gantt:
        print(f"{pid}: {start} -> {end}")
    print("\n--- FCFS Gantt Chart ---")
    previous_end = 0
    for p in fcfs_results:
        if p["start"] > previous_end:
            print(f"IDLE: {previous_end} -> {p['start']}")
        print(f"{p['pid']}: {p['start']} -> {p['end']}")
        previous_end = p["end"]
    print("\n--- FCFS Process Table ---")
    for p in fcfs_results:
        print(
            p["pid"],
            "Completion:", p["end"],
            "Turnaround:", p["turnaround"],
            "Waiting:", p["waiting"],
            "Response:", p["response"]
        )
    print("\n--- Priority Process Table ---")
    for p in priority_results:
        print(
            p["pid"],
            "Completion:", p["completion"],
            "Turnaround:", p["turnaround"],
            "Waiting:", p["waiting"],
            "Response:", p["response"]
        )
    print("\n--- Scheduling Comparison ---")
    print("FCFS Average Waiting:", fcfs_avg_waiting)
    print("Priority Average Waiting:", priority_avg_waiting)
    print("FCFS Average Turnaround:", fcfs_avg_turnaround)
    print("Priority Average Turnaround:", priority_avg_turnaround)
    print("FCFS Average Response:", fcfs_avg_response)
    print("Priority Average Response:", priority_avg_response)
    print("\n--- Better Algorithm ---")
    if fcfs_avg_waiting < priority_avg_waiting:
        print("Waiting Time: FCFS is better")
    elif priority_avg_waiting < fcfs_avg_waiting:
        print("Waiting Time: Priority is better")
    else:
        print("Waiting Time: Both are equal")
    if fcfs_avg_turnaround < priority_avg_turnaround:
        print("Turnaround Time: FCFS is better")
    elif priority_avg_turnaround < fcfs_avg_turnaround:
        print("Turnaround Time: Priority is better")
    else:
        print("Turnaround Time: Both are equal")
    if fcfs_avg_response < priority_avg_response:
        print("Response Time: FCFS is better")
    elif priority_avg_response < fcfs_avg_response:
        print("Response Time: Priority is better")
    else:
        print("Response Time: Both are equal")
main()
    

    




 
              
                    
                

                

