#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PYTHONUNBUFFERED=1 PYTHONPATH="$SCRIPT_DIR:$SCRIPT_DIR/src" "$SCRIPT_DIR/.venv/bin/python" src/start/main.py
