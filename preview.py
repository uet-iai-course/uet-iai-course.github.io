#!/usr/bin/env python3
"""
Preview server cho landing page IAI Courses.

Dùng: python preview.py [port]
  port  cổng local (mặc định: 8080)
"""

import http.server
import os
import sys
import time
import threading
import hashlib
from pathlib import Path

ROOT = Path(__file__).parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

WATCH_EXTENSIONS = {".html", ".css", ".js"}
POLL_INTERVAL = 0.8  # giây


# ── File watcher ──────────────────────────────────────────────────────────────

def _file_digest(path: Path) -> str:
    try:
        return hashlib.md5(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def _snapshot(root: Path) -> dict[str, str]:
    return {
        str(p): _file_digest(p)
        for p in root.rglob("*")
        if p.suffix in WATCH_EXTENSIONS and ".git" not in p.parts
    }


def _watch(root: Path) -> None:
    prev = _snapshot(root)
    while True:
        time.sleep(POLL_INTERVAL)
        curr = _snapshot(root)
        changed = [f for f in curr if curr[f] != prev.get(f)]
        added   = [f for f in curr if f not in prev]
        removed = [f for f in prev if f not in curr]

        for f in changed:
            print(f"  ~ changed  {Path(f).relative_to(root)}")
        for f in added:
            print(f"  + added    {Path(f).relative_to(root)}")
        for f in removed:
            print(f"  - removed  {Path(f).relative_to(root)}")

        if changed or added or removed:
            print("  [reload] Ctrl+R trong browser để xem thay đổi.")

        prev = curr


# ── HTTP server ───────────────────────────────────────────────────────────────

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, format, *args):  # noqa: A002
        # args từ request: ('"GET /path HTTP/1.1"', '200', '-')
        # args từ log_error: (HTTPStatus.NOT_FOUND, 'File not found') — bỏ qua
        if not args or not isinstance(args[0], str):
            return
        parts = args[0].split()
        path = parts[1] if len(parts) > 1 else "-"
        code = str(args[1]) if len(args) > 1 else "-"
        if code != "304" and path != "/favicon.ico":
            print(f"  {code}  {path}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    os.chdir(ROOT)

    server = http.server.HTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://localhost:{PORT}"

    print(f"\n  IAI Courses — preview server")
    print(f"  {'─' * 34}")
    print(f"  URL   {url}")
    print(f"  Root  {ROOT}")
    print(f"  Watching .html .css .js — Ctrl+C to stop\n")

    threading.Thread(target=_watch, args=(ROOT,), daemon=True).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopped.")
        server.server_close()


if __name__ == "__main__":
    main()
