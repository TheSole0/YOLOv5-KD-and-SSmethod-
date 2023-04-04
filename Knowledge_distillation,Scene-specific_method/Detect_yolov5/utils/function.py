
import os
import sys
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


###########################################################################################
#head_stages = [4, 6, 10, 13, 14, 17, 20, 23]  # if you want head 3 
head_stages = [2, 4, 6, 10, 13, 14, 17, 18, 21, 24, 27, 30] # if you want head 4 

start, end, head = 22, 30, 1 #start of cut, end of cut, How many will you use to head

# 네트워크 차단
def convert(q, w, r):    
        # if head 3
        if q == 18 and w ==23 and r == 1:
            out = [17]
            print("only 17(80x80) head")
            return out, 0, 1
        elif q == 21 and w ==23 and r == 2:
            out = [17, 20]
            print("17(80x80) head and 20(40x40) head")
            return out, 0, 2
        elif q == 0 and w ==0 and r == 0:
            out = [17, 20, 23]
            print("default")
            return out, 0, 3
        
        # if head 4 
        elif q == 22 and w ==30 and r == 1:
            out = [21]
            print("21(160x160)")
            return out, 0, 1
        elif q == 25 and w ==30 and r == 2:
            out = [21, 24]
            print("21(160x160) and 24(80x80)")
            return out, 0, 2      
        elif q == 28 and w ==30 and r == 3:
            out = [21, 24, 27]
            print("21(160x160) and 24(80x80)head and 27(40x40)head")
            return out, 0, 3
        elif q == 0 and w ==0 and r == 1:
            out = [21, 24, 27, 30]
            print("default of head 4")
            return out, 0, 4
        
        else:
            [print("\n\n[Please check to command in function of convert (yolo.py line 42)]\n\n") for x in range(5)]  
