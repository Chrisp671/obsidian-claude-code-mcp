import sys
import os
import threading
import time

def main():
    from winpty import PtyProcess

    # Build command from argv
    cmd = sys.argv[1] if len(sys.argv) > 1 else "powershell.exe"

    # Spawn process in ConPTY
    proc = PtyProcess.spawn(cmd, dimensions=(24, 120))

    exit_code = [None]

    def read_pty():
        """Read from ConPTY and write to stdout (goes to Node.js)"""
        while proc.isalive():
            try:
                data = proc.read(4096)
                if data:
                    if isinstance(data, str):
                        sys.stdout.buffer.write(data.encode("utf-8", "replace"))
                    else:
                        sys.stdout.buffer.write(data)
                    sys.stdout.buffer.flush()
            except EOFError:
                break
            except Exception:
                break
        exit_code[0] = proc.exitstatus if proc.exitstatus is not None else 1

    def read_stdin():
        """Read from stdin (from Node.js) and write to ConPTY"""
        stdin_fd = sys.stdin.fileno()
        while proc.isalive():
            try:
                data = os.read(stdin_fd, 4096)
                if not data:
                    break
                text = data.decode("utf-8", "replace")
                proc.write(text)
            except (OSError, EOFError):
                break
            except Exception:
                break

    # Start I/O threads
    pty_thread = threading.Thread(target=read_pty, daemon=True)
    stdin_thread = threading.Thread(target=read_stdin, daemon=True)
    pty_thread.start()
    stdin_thread.start()

    # Wait for PTY output thread to finish (means process exited)
    pty_thread.join()

    # Small delay for any final output
    time.sleep(0.1)

    sys.exit(exit_code[0] if exit_code[0] is not None else 1)

if __name__ == "__main__":
    main()
