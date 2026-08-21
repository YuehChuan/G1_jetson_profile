#!/usr/bin/env python3

import re
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log_path", default="tegrastats_20260821_140945.log")
    parser.add_argument("--output", default="tegra_stats.dat")
    return parser.parse_args()

def parse_line(line):
    ram = re.search(r"RAM\s+(\d+)/(\d+)MB", line)
    gpu = re.search(r"GR3D_FREQ\s+(\d+)%", line)
    cpu = re.search(r"CPU\s+\[(.*?)\]", line)
    cpu_temp = re.search(r"CPU@([\d.]+)C", line)
    gpu_temp = re.search(r"GPU@([\d.]+)C", line)

    cpu_values = [int(x) for x in re.findall(r"(\d+)%@", cpu.group(1))] if cpu else []
    cpu_values += [0] * (8 - len(cpu_values))
    cpu_values = cpu_values[:8]

    return {
        "gpu": int(gpu.group(1)) if gpu else 0,
        "cpu": cpu_values,
        "ram": int(ram.group(1)) if ram else 0,
        "ram_total": int(ram.group(2)) if ram else 0,
        "cpu_temp": float(cpu_temp.group(1)) if cpu_temp else 0,
        "gpu_temp": float(gpu_temp.group(1)) if gpu_temp else 0
    }

args = parse_args()

with open(args.log_path) as f, open(args.output, "w") as out:
    out.write("# time GPU CPU0 CPU1 CPU2 CPU3 CPU4 CPU5 CPU6 CPU7 RAM RAM_TOTAL CPU_TEMP GPU_TEMP\n")

    for i, line in enumerate(f):
        d = parse_line(line)
        cpus = " ".join(str(x) for x in d["cpu"])
        out.write(f"{i} {d['gpu']} {cpus} {d['ram']} {d['ram_total']} {d['cpu_temp']:.2f} {d['gpu_temp']:.2f}\n")

print(f"Saved: {args.output}")
