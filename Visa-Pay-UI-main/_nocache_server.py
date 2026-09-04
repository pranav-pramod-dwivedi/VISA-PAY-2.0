"""
NovaPay dev server - serves the static UI with strict no-cache headers.

Usage:
    python _nocache_server.py            # serves on 0.0.0.0:8899
    python _nocache_server.py 9000       # serve on a custom port

Press Ctrl+C to stop.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCache(SimpleHTTPRequestHandler):
    """Static handler that sends headers preventing any browser/CDN caching."""

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, *args):
        pass


def main():
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8899
    server = ThreadingHTTPServer(("0.0.0.0", port), NoCache)
    print(f"NovaPay dev server on http://0.0.0.0:{port}  (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()


if __name__ == "__main__":
    main()
