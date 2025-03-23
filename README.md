FloodX - UDP Flood Attack Tool

FloodX is a powerful UDP flood attack tool designed for network security testing and educational purposes. It utilizes multiple processes for maximum performance to generate a high volume of UDP packets towards the target machine.

Features:

Multi-threaded for optimal performance

Supports custom packet size and port configuration

Simple command-line interface

Safe for educational and testing purposes


Requirements:

Python 3.x

multiprocessing and socket libraries (Pre-installed with Python)


Installation:

Clone the repository:

git clone https://github.com/mirac-s/FloodX.git
cd FloodX

Install dependencies (if any):

pip install -r requirements.txt

Usage:

Run the script with the following command:

python3 FloodX.py --target <TARGET_IP> --port <PORT> --size <PACKET_SIZE> --processes <NUM_PROCESSES>

For example:

python3 FloodX.py --target 192.168.1.1 --port 80 --size 8192 --processes 8

Options:

--help : Display help information.

--target : Target IP address or domain.

--port : Target port (default: 80).

--size : Packet size (default: 8192 bytes).

--processes : Number of processes to run (default: CPU count * 20).


Disclaimer:

FloodX is meant for educational purposes and ethical hacking only. Always get explicit permission before testing any network. Unauthorized attacks are illegal.

Contributing:

Since I'm relatively new to this project, I welcome any contributions! Feel free to open issues, suggest features, or submit pull requests. Your feedback and collaboration are highly appreciated.

License:

This project is licensed under the MIT License.

📒 WIKI PAGE:
https://github.com/mirac-s/FloodX/wiki/How-to-Use

📂 DOWNLOAD LINK:
https://github.com/mirac-s/FloodX/archive/refs/tags/v1.0.zip
