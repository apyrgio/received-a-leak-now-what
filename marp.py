#!/usr/bin/env python3
import argparse
import logging
import os
import shutil
import signal
import subprocess
import sys
import time
import webbrowser

log = logging.getLogger("marp")

IMAGE = "docker.io/marpteam/marp-cli:latest"
WORKDIR = "/home/marp/app"


def _runtime():
    for name in ("podman", "docker"):
        if shutil.which(name):
            return name
    log.error("No container runtime found (install podman or docker)")
    sys.exit(1)


RUNTIME = _runtime()


def container_run(args, init=True, ports=None, detach=False):
    cmd = [
        RUNTIME, "run",
        "--rm",
        "-v", f"{os.getcwd()}:{WORKDIR}",
        "-e", f"LANG={os.environ.get('LANG', 'C.UTF-8')}",
        "-e", "MARP_USER=root:root",
    ]
    if init:
        cmd.append("--init")
    if ports:
        for host_port, container_port in ports:
            cmd.extend(["-p", f"{host_port}:{container_port}"])
    if detach:
        cmd.append("-d")
    cmd.extend([IMAGE] + args)
    log.debug("Running: %s", " ".join(cmd))
    return cmd


def cmd_cli(args):
    rest = args.args
    log.info("Running marp CLI with: %s", " ".join(rest) if rest else "(default)")
    os.execvp(RUNTIME, container_run(rest))


def cmd_serve(args):
    port = args.port
    extra = ["-s", ".", "--allow-local-files"]
    cmd = container_run(extra, ports=[(port, "8080"), (37717, 37717)])

    log.info("Starting server at http://localhost:%d", port)
    proc = subprocess.Popen(cmd)

    def handle_signal(signum, frame):
        log.info("Shutting down server ...")
        proc.terminate()
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    if args.open:
        time.sleep(2)
        url = f"http://localhost:{port}"
        log.info("Opening %s ...", url)
        webbrowser.open(url)

    proc.wait()


def cmd_pdf(args):
    extra = ["slides.md", "--pdf", "--allow-local-files", "-o", "slides.pdf"]
    log.info("Generating PDF ...")
    subprocess.run(container_run(extra), check=True)
    log.info("Done: slides.pdf")


def cmd_html(args):
    extra = ["slides.md", "--allow-local-files"]
    log.info("Generating HTML ...")
    subprocess.run(container_run(extra), check=True)
    log.info("Done: html/index.html")


def main():
    parser = argparse.ArgumentParser(
        description="Marp slide deck builder (via Podman or Docker)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Enable debug logging"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_cli = sub.add_parser("cli", help="Run arbitrary marp CLI command")
    p_cli.add_argument("args", nargs=argparse.REMAINDER)

    p_serve = sub.add_parser("serve", help="Start Marp server mode")
    p_serve.add_argument("--port", "-p", type=int, default=8080)
    p_serve.add_argument("--open", "-o", action="store_true")

    sub.add_parser("pdf", help="Generate slides.pdf")
    sub.add_parser("html", help="Generate HTML under html/")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="[%(levelname)s] %(message)s",
    )

    if args.command == "cli":
        cmd_cli(args)
    elif args.command == "serve":
        cmd_serve(args)
    elif args.command == "pdf":
        cmd_pdf(args)
    elif args.command == "html":
        cmd_html(args)


if __name__ == "__main__":
    main()
