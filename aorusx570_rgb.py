import hid

zone_dict = {
    "IO_LED"  : (0x20,0x01),
    "LED_CPU" : (0x21,0x02),
    "LED_SID" : (0x23,0x08),
    "LED_CX"  : (0x24,0x10),
    "D_LED1"  : (0x25,0x20),
    "D_LED2"  : (0x26,0x40)
}

class AorusRGBController:
    def __init__(self, vid=0x048d, pid=0x8297):
        assert isinstance(vid, int), "Vendor ID should be an integer"
        assert isinstance(pid, int), "Product ID should be an integer"
        self.vid = vid
        self.pid = pid
        #report ID is 0xcc, 23 bytes appears to be the smallest I can
        #make the report and still have it function properly
        self.rgb_report = [0xcc] + [0x00]*10 + [0x01,0x5a] + [0x00]*10
        self.commit_report = [0xcc,0x28,0xff] + [0x00]*20

    def set_rgb(self, zone, r, g, b):
        assert isinstance(r,int), "r component should be an integer"
        assert isinstance(g,int), "g component should be an integer"
        assert isinstance(b,int), "b component should be an integer"
        assert isinstance(zone,str), "Zone should be a string"
        assert zone in zone_dict, "Provided zone is not in zone_dict"

        if (r < 0 or r > 255):
            print("r is out of bounds [0-255]")
            return

        if (g < 0 or g > 255):
            print("g is out of bounds [0-255]")
            return

        if (b < 0 or b > 255):
            print("b is out of bounds [0-255]")
            return

        try:
            h = hid.device()
            h.open(self.vid,self.pid)
            self.rgb_report[1] = zone_dict[zone][0]
            self.rgb_report[2] = zone_dict[zone][1]
            self.rgb_report[14] = b
            self.rgb_report[15] = g
            self.rgb_report[16] = r
            h.send_feature_report(self.rgb_report)
            h.send_feature_report(self.commit_report)
            h.close()
        except:
            print("Failed to set rgb! Check USB permissions or run as root!")

if __name__ == "__main__":
    print("Please import this into your own application.")
    exit()
