#!/usr/bin/env python3


import argparse
import os
import subprocess
import sys
from typing import List

# ----------------------------------------------------------------------
# Optional pretty printing – fall back to plain `print` if Rich is missing
# ----------------------------------------------------------------------
try:
    from rich.console import Console  # type: ignore
    console = Console()
    echo = console.print
except Exception:  # pragma: no cover
    echo = print

# ----------------------------------------------------------------------
# Helper to run an external command and show it
# ----------------------------------------------------------------------
def run(cmd: List[str]) -> None:
    """Execute *cmd* (list of arguments) and print the command first."""
    echo(f"$ {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=False)
    except FileNotFoundError:
        echo(f"[red]Command not found:[/red] {cmd[0]}")
    except Exception as exc:  # pragma: no cover
        echo(f"[red]Error while running {' '.join(cmd)}:[/red] {exc}")


# ----------------------------------------------------------------------
# Argument handling
# ----------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="myprogram",
        description="Run a quick set of reconnaissance tools against a single URL.",
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Target URL (e.g. https://example.com).",
    )
    return parser


# ----------------------------------------------------------------------
# Core enumeration – each external tool is called in its own function.
# This keeps the logic readable and makes unit‑testing easier.
# ----------------------------------------------------------------------
def curl_basic(target: str) -> None:
    run(["curl", "-s", target])


def curl_headers(target: str) -> None:
    run(["curl", "-s", "-I", target])


def fetch_robots(target: str) -> None:
    run(["curl", "-s", f"{target.rstrip('/')}/robots.txt"])


def whois_lookup(target: str) -> None:
    run(["whois", target])


def nikto_scan(target: str) -> None:
    run(["nikto", "-h", target])


def whatweb_fingerprint(target: str) -> None:
    try:
        run(["whatweb", target])
    except Exception:
        print("whatweb not found, skipping fingerprinting.")
    run(["whatweb", target, "-v"])


def dns_queries(target: str) -> None:
    # `dig axfr` is the most useful for zone transfers; keep it optional.
    run(["dig", "axfr", target])
    run(["nslookup", target])


def nmap_http_title(target: str) -> None:
    out = f"{target.replace('://', '_')}-scan-0"
    run(
        [
            "nmap",
            "-p",
            "80,443",
            "--script",
            "http-title",
            target,
            "-oN",
            out,
        ]
    )


def nmap_http_enum(target: str) -> None:
    out = f"{target.replace('://', '_')}-scan-0"
    run(
        [
            "nmap",
            "-sV",
            "--script",
            "http-enum",
            "--append-output",
            target,
            "-oN",
            out,
        ]
    )


def enumerate_target(url: str) -> None:
    """Run the whole toolbox against *url*."""
    echo(f"[bold green]Starting enumeration for:[/bold green] {url}")

    curl_basic(url)
    curl_headers(url)
    fetch_robots(url)
    whois_lookup(url)
    nikto_scan(url)
    whatweb_fingerprint(url)
    dns_queries(url)
    nmap_http_title(url)
    nmap_http_enum(url)

    echo("[bold green]Enumeration finished.[/bold green]")


# ----------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------
def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    enumerate_target(args.url)


if __name__ == "__main__":
    main()
