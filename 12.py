import os

DIR = r"C:\Users\Administrator\AppData\Roaming\PUC\PUC_Client\Log\Client_Log"


def compare(x, y):
    stat_x = os.stat(DIR + "/" + x)
    stat_y = os.stat(DIR + "/" + y)
    if stat_x.st_ctime < stat_y.st_ctime:
        return -1
    elif stat_x.st_ctime > stat_y.st_ctime:
        return 1
    else:
        return 0


iterms = os.listdir(r"C:\Users\Administrator\AppData\Roaming\PUC\PUC_Client\Log\Client_Log")

iterms.sort(compare)

for iterm in iterms:
    print iterm