import os
import datetime


directory = input("Ievadiet direktorija, ko nolistēt, pilnu ceļu: ")
if not os.path.isdir(directory):
    print("Tāds direktorijs neeksistē!")
    exit(1)

#Ja beigās ir /, tad to novācam, lai nebūtu problēmu ar prefiksiem un nolistētu arī galveno direktoriju
directory = directory.rstrip("/")
#Windows beigu \ novācam
directory = directory.rstrip("\\")

for root, dirs, files in os.walk(directory, topdown=True):
    path = root.split(os.sep)
    depth = root[len(directory):].count(os.sep)
    prefix = "----" * depth
    print(f"{prefix}{os.path.basename(root)}")
    for file in files:
        try:
            path = os.path.join(root, file)
            if depth != 0:
                prefix_file = prefix + "----"
            else:
                prefix_file = "----"
            size = os.stat(path).st_size
            ctime = os.stat(path).st_ctime
            ctime_datetime = datetime.datetime.fromtimestamp(ctime)
            ctime_as_date = ctime_datetime.strftime("%d-%m-%Y %H:%M:%S")
            print(f"{prefix_file+file:<60} {str(size):>20} baiti            Fails izveidots{ctime_as_date:>20}")
        except Exception:
            pass