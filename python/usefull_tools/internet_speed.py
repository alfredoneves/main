#!/usr/bin/python3
# pip install speedtest-cli

import speedtest

tester = speedtest.Speedtest()

# download
print("testing download speed ...")
download_speed = tester.download()
print(f"download speed: {download_speed / 1024**2:.2f} MB/s")

# upload
print("testing upload speed ...")
upload_speed = tester.upload()
print(f"upload speed: {upload_speed / 1024**2:.2f} MB/s")

# latency
print(f"latency: {tester.results.ping:.2f} ms")
