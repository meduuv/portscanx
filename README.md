# PortScanX

A small, dependency-free TCP port scanner for authorized diagnostics and lab work.

## Features

- IPv4 TCP connect scanning
- Port ranges and comma-separated ports
- Configurable timeout and concurrency
- Reverse DNS display
- JSON and terminal output
- Deterministic result ordering
- No exploitation or credential testing

## Usage

```text
python -m portscanx 127.0.0.1 --ports 22,80,443
python -m portscanx 127.0.0.1 --ports 1-1024 --timeout 0.3 --workers 64
```

Only scan systems you own or are explicitly authorized to test.

Built by medu. Credits: https://guns.lol/meduu
