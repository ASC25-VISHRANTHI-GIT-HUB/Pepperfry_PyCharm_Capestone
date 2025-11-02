import os
import time

def capture(driver, name="screenshot"):
    ts = int(time.time())
    fname = f"{name}_{ts}.png"

    # Ensure screenshots are saved inside Pepperfry/reports/screenshots
    base_dir = os.path.dirname(os.path.dirname(__file__))  # points to Pepperfry/
    outdir = os.path.join(base_dir, "reports", "screenshots")

    try:
        os.makedirs(outdir, exist_ok=True)
        path = os.path.join(outdir, fname)
        driver.save_screenshot(path)
        print(f"Screenshot saved at: {path}")
        return path
    except Exception as e:
        print(f"Failed to save screenshot: {e}")
        return None
