import requests
from threading import Thread

def task():
	limit = 10000
	for n in range(1, limit + 1):
	    url = f"https://www.larvalabs.com/public/images/cryptopunks/punk{n:04}.png"
	    r = requests.get(url)
	    
		
	    a = "output/img_{}.png".format(n)
	    f = open(a, "wb")
	    f.write(r.content)
	    f.close()
	    print("Downloaded", url)

threads = []
for n in range(1, 11):
    t = Thread(target=task)
    threads.append(t)
    t.start()
