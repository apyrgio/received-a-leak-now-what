# [SLIDES] Dataharvest 2026 - You received a leak, now what? A hands-on OPSEC simulation

This repo contains the slides for Alex's and Kolja's presentation on Dataharvest 2026, titled ["You received a leak, now what? A hands-on OPSEC simulation"](https://dataharvest26.sched.com/event/2L8gG/you-received-a-leak-now-what-a-hands-on-opsec-simulation).

A live version of the slides can be found in https://apyrgio.github.io/received-a-leak-now-what/

## Overview

This is a [Marp](https://marp.app/) presentation built with **Podman** (or **Docker**) — no Node.js or Chrome required on your host.

The script `marp.py` auto-detects which container runtime is available, preferring `podman` over `docker`.

## Prerequisites

- [Podman](https://podman.io/) or [Docker](https://docker.com/) installed
- The official Marp CLI container image:

```sh
podman pull docker.io/marpteam/marp-cli:latest
```

## Commands

All actions go through `marp.py`:

### `python3 marp.py cli [args...]`

Pass arbitrary arguments directly to the Marp CLI inside the container.

```sh
python3 marp.py cli slides.md --theme gaia -o output.html
python3 marp.py cli --version
```

### `python3 marp.py serve [--port PORT] [--open]`

Start Marp in server mode at `http://localhost:8080` (default).

```sh
python3 marp.py serve                        # http://localhost:8080
python3 marp.py serve --port 9000            # http://localhost:9000
python3 marp.py serve --open                 # auto-open browser
```

### `python3 marp.py pdf`

Generate `slides.pdf` from `slides.md`.

```sh
python3 marp.py pdf
```

### `python3 marp.py html`

Generate `html/index.html` from `slides.md`.

```sh
python3 marp.py html
```

## CI/CD

A GitHub Action (`.github/workflows/publish.yml`) runs on every push that touches:

- `slides.md`
- `themes/**`
- `marp.py`
- `.github/workflows/**`

On every matching push the workflow **builds** HTML and PDF slides. On pushes to the `main` branch it additionally **deploys** the HTML slides to **GitHub Pages**.

Built artifacts (from any branch) can be downloaded via the workflow run page.
