import urllib.request, json, pandas, datetime, hdfs

site= "http://whattomine.com/asic.json"
hdr = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	}

# connection = hdfs.InsecureClient('http://localhost:50070')

req = urllib.request.Request(site, headers=hdr)

timestamp = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')

page = urllib.request.urlopen(req)
string_response = page.read().decode('utf-8')
coins_json = json.loads(string_response)
with open('data_'+timestamp+'.json', 'w') as outfile:
    json.dump(coins_json['coins'], outfile)