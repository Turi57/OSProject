from threading import Thread

def process(a,b):
    print(a + b * a * a * a * b /a -121243454 * 12133)

for _ in range(1000000000000000):
    thread = Thread(target=process, args=(1,2))
    thread.start()
