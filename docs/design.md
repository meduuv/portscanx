# Design

PortScanX keeps scanning separate from presentation. Probe workers return structured results, while the CLI handles filtering and serialization. Network activity is limited to explicit TCP connection attempts.
