import requests
import time


url = "http://comtrade.un.org/api/get?"
maxrecord = 50000
datatype = "C"  # C for commodities, S for services
freq = "A"		# M for monthly, A for Annually
px = "HS"		# classification
ps = "2010,2011,2012,2013,2014"	# time period. for looping
r = "360"		# reporting area. refer to: https://comtrade.un.org/data/cache/reporterAreas.json
p = "all"		# partner country
rg = "all"		# trade flow 1=import 2=export
cc = [46, 47]		# classification code. refer to https://comtrade.un.org/data/cache/classificationHS.json
fmt = "csv"		# format is json or csv

all_try = 0
# Note: for Monthly frequency, you cannot have "all" as partner
# Monthly frequency can only used for "all" reporter and world (0) partner


#def combine(url, maxrecord, datatype, freq, px, ps, r, p, rg, cc, fmt):
#link = f"{url}max={maxrecord}&type={datatype}&freq={freq}&px={px}&ps={ps}&r={r}&p={p}&rg={rg}&cc={cc}&fmt={fmt}"

for c_code in cc:
	link = f"{url}max={maxrecord}&type={datatype}&freq={freq}&px={px}&ps={ps}&r={r}&p={p}&rg={rg}&cc={c_code}&fmt={fmt}"

	print(f"getting {link}")

	with open(f"comtrade-{r}-{c_code}.{fmt}", "w") as outfile:
		api_request = requests.get(link).text

		outfile.write(api_request)

		all_try = all_try + 1

		print(f"number of requests: {all_try}")

		if all_try % 95 ==0:
			time.sleep(3650)
			print("waiting for 1 hour...")
		else:
			time.sleep(2)





