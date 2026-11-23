def read_processes():
    processes = []
    with open("input.txt", "r") as file:
        for line in file:
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
    while remaining:
        available = [p for p in remaining if p["arrival"]<= current_time]
        if not available:
            current_time + =1 
 
              
                    
                

                

