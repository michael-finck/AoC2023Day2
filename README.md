# AoC2023Day2

## Overview

AoC2023Day2 is a Python script designed for analyzing network packet logs in CSV format. It utilizes the pandas library for efficient data manipulation and matplotlib for creating insightful visualizations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Installation

Ensure you have the required libraries installed by running:

```bash
pip install pandas matplotlib
```

Clone the repository:

git clone https://github.com/michael-finck/AoC2023Day2.git
cd AoC2023Day2

## Usage

1. Place your network packet log file (network_traffic.csv) in the same directory as the script.
2. Run the script:

python AoC2023Day2.py

## Features

1. Packet Count: Displays the total number of packets captured during the session.

2. Most Active IP Address: Identifies the IP address responsible for the highest traffic volume.

3. Most Frequent Protocol: Determines the most commonly occurring protocol in the packet log.

## Example Output

Packet Count:
PacketNumber    100
Timestamp       100
Source          100
Destination     100
Protocol        100
dtype: int64

Most Active IP Address:
Source
192.168.1.1    30
192.168.1.2    25
...

Most Frequent Protocol:
TCP     40
UDP     30
ICMP    20
...

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.