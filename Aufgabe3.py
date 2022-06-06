import time

while(True):
    seconds = time.time()
    local_time = time.ctime(seconds)
    nextarrival=seconds-seconds%1800 +1800
    john=nextarrival-seconds
    duetime=time.localtime(john)

    print("Aktuelle Uhrzeit:", local_time)
    print("Der naechste Zug kommt um:", time.ctime(nextarrival))
    print("Der naechste Zug kommt in:  00:",duetime.tm_min, " minutes")     #Webb der Zug alle 30minuten kommt dann kann der Maximal Wert an Minuten nur 30 und der minimal Wert 0 sein
    time.sleep(60)