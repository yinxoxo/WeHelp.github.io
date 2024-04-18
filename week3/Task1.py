import json
import csv
import urllib.request

serial_to_stitle = {}  # 存放serial_no:stitle
serial_to_district = {}  # 存放serial_no:{各種data}

# 讀入第一個網址
url1 = (
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
)
with urllib.request.urlopen(url1) as response:
    data1 = json.loads(response.read().decode())

for result in data1["data"]["results"]:
    serial_no = result["SERIAL_NO"]
    stitle = result["stitle"]
    serial_to_stitle[serial_no] = stitle
    # 抓出經緯度、.jpg網址
    longitude = result["longitude"]
    latitude = result["latitude"]
    files = result.get("filelist", "")
    jpg_urls = [url for url in files.split("https://") if ".jpg" in url.lower()]
    first_jpg_url = f"https://{jpg_urls[0]}" if jpg_urls else ""

    # 先存放數據，後寫入csv
    serial_to_district[serial_no] = {
        "stitle": stitle,
        "longitude": longitude,
        "latitude": latitude,
        "jpg_url": first_jpg_url,
    }

# 讀入第二個網址
url2 = (
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
)
with urllib.request.urlopen(url2) as response:
    data2 = json.loads(response.read().decode())

mrt_to_stitles = {}
for result in data2["data"]:
    mrt_station = result["MRT"]
    serial_no = result["SERIAL_NO"]
    stitle = serial_to_stitle.get(serial_no)
    if mrt_station in mrt_to_stitles:
        mrt_to_stitles[mrt_station].add(stitle)
    else:
        mrt_to_stitles[mrt_station] = set([stitle])

    if serial_no in serial_to_district:
        district_data = serial_to_district[serial_no]
        district_data["district"] = result["address"].split()[1][:3]

# 景點資料寫入spot.csv
with open("spot.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    for serial_no, data in serial_to_district.items():
        writer.writerow(
            [
                data["stitle"],
                data["district"],
                data["longitude"],
                data["latitude"],
                data["jpg_url"],
            ]
        )

# MRT捷運站資料寫入mrt.csv
with open("mrt.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    for mrt_station, stitles in mrt_to_stitles.items():
        row = [mrt_station]
        row.extend(stitles)  # 將每個景點作為單獨一個欄位添加到行中
        writer.writerow(row)
