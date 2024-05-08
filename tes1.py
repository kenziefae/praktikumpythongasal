import speedtest

def speed_test():
    speed_tester = speedtest.Speedtest()

    dwnld_speed = speed_tester.download()
    upload_speed = speed_tester.upload()

    return (dwnld_speed, upload_speed)

download_speed, upload_speed = speed_test()

print("Download Speed:", download_speed / 10**6, "Mbps")
print("Upload Speed:", upload_speed / 10**6, "Mbps")