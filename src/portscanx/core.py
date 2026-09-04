from __future__ import annotations

import concurrent.futures
import socket
from dataclasses import dataclass


@dataclass(frozen=True)
class ScanResult:
    port: int
    state: str
    service: str | None = None


def parse_ports(value: str) -> list[int]:
    ports: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            left, right = part.split("-", 1)
            start, end = int(left), int(right)
            if start > end:
                raise ValueError("port range must be ascending")
            ports.update(range(start, end + 1))
        else:
            ports.add(int(part))
    if not ports or any(port < 1 or port > 65535 for port in ports):
        raise ValueError("ports must be between 1 and 65535")
    return sorted(ports)


def _probe(host: str, port: int, timeout: float) -> ScanResult:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        state = "open" if sock.connect_ex((host, port)) == 0 else "closed"
    service = None
    if state == "open":
        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            pass
    return ScanResult(port, state, service)


def scan(host: str, ports: list[int], timeout: float = 0.5, workers: int = 32) -> list[ScanResult]:
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    if workers < 1:
        raise ValueError("workers must be positive")
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(lambda p: _probe(host, p, timeout), ports))
    return sorted(results, key=lambda result: result.port)
