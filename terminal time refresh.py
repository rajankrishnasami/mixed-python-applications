import datetime , time
def tim():
    while True:
        time.sleep(1)
        yield str(datetime.datetime.now())
for i in tim():
	print(i)
