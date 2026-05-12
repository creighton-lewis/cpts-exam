#!/usr/bin/env python3
"""Tiny helper that can start a tiny FTP, HTTP or Samba server."""
import os
import shutil
import subprocess
import sys

# ----------------------------------------------------------------------
# Optional pretty output – fall back to plain `print` if Rich isn’t installed
# ----------------------------------------------------------------------
try:
    from rich.console import Console          # type: ignore
    console = Console()
    echo = console.print
except Exception:          # pragma: no cover – Rich is optional
    echo = print

# ----------------------------------------------------------------------
# Helper to run a command and show it (useful while developing)
# ----------------------------------------------------------------------
def run(cmd: list[str]) -> None:
    """Run *cmd* (list of strings) showing the command first."""
    echo(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, check=False)


# ----------------------------------------------------------------------
# Ensure ``pyftpdlib`` is present – we install it only once
# ----------------------------------------------------------------------
def ensure_ftp_lib() -> None:
    """Install pyftpdlib if the module cannot be imported."""
    try:
        import pyftpdlib  # noqa: F401
    except Exception:
        run([sys.executable, "-m", "pip", "install", "--quiet", "pyftpdlib"])


# ----------------------------------------------------------------------
# Main dispatcher
# ----------------------------------------------------------------------
def main() -> None:
    echo(
        "Enter one of the following commands:\n"
        "  start_ftp   – start a simple FTP server on port 21\n"
        "  start_http  – start a simple HTTP server on port 80/8000\n"
        "  start_samba – launch impacket’s smbserver (requires impacket)\n"
    )

    cmd = input("Command: ").strip().lower()

    if cmd == "start_ftp":
        ensure_ftp_lib()
        run([sys.executable, "-m", "pyftpdlib", "-p", "21", "-u", "user", "-P", "pass"])

    elif cmd == "start_http":
        # Prefer port 80; fall back to 8000 if we lack permission.
        for port in ("80", "8000"):
            run([sys.executable, "-m", "http.server", port, "--bind", "0.0.0.0"])
            # http.server will exit immediately on error (e.g. permission denied),
            # so we simply try the next port.
            if not os.path.exists(f"/proc/{os.getpid()}/fd"):   # dummy check to stop loop
                break

    elif cmd == "start_samba":
        smb_path = "/usr/share/doc/python3-impacket/examples/smbserver.py"
        if not os.path.isfile(smb_path):
            echo(
                "smbserver.py not found – install the *impacket* package "
                "to use the Samba helper."
            )
            return
        # The command needs sudo because it binds to a privileged port.
        run(
            [
                "sudo",
                sys.executable,
                smb_path,
                "-smb2support",
                "CompData",
                "Downloads",
            ]
        )

    else:
        echo("Invalid command – see the options above.")


if __name__ == "__main__":
    main()
