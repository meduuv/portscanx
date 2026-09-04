from __future__ import annotations

import argparse
import json
import socket

from .core import parse_ports, scan


def main() -> int:
    parser = argparse.ArgumentParser(description="Authorized TCP port scanner")
    parser.add_argument("host")
    parser.add_argument("--ports", default="1-1024")
    parser.add_argument("--timeout", type=float, default=0.5)
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    try:
        ports = parse_ports(args.ports)
        address = socket.gethostbyname(args.host)
        results = scan(address, ports, args.timeout, args.workers)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    if args.as_json:
        print(json.dumps([result.__dict__ for result in results], indent=2))
    else:
        for result in results:
            service = f" ({result.service})" if result.service else ""
            print(f"{result.port:5} {result.state}{service}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
