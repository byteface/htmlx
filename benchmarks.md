A quick benchmark test on using the compiled DOM vs the regular python dom.

note  - still a lot of runtime bugs. 

code to paste into a python session...
```
from htmlx.dom import *
from htmlx.dom import *  # do twice as throwing a bug first time
import time
def bench():
    t0 = time.time()
    print(str(HTMLDivElement()))
    t1 = time.time()
    print(t1-t0)
```

using compiled DOM render a single node. generate the .so files first

```
mypyc htmlx
```

>>> bench()
<div></div>
0.00011396408081054688
>>> bench()
<div></div>
0.0001442432403564453
>>> bench()
<div></div>
0.00010943412780761719
>>> bench()
<div></div>
0.00014209747314453125
>>> bench()
<div></div>
0.00011682510375976562
>>> bench()
<div></div>
0.00010919570922851562
>>> bench()
<div></div>
0.0001418590545654297
>>> bench()
<div></div>
0.00013756752014160156


using regular python DOM render a single node.

clear away the .so files and use the .py files directly
```
make clean
```

>>> import time
>>> bench()
<div></div>
0.0002512931823730469
>>> bench()
<div></div>
0.0002162456512451172
>>> bench()
<div></div>
0.00022149085998535156
>>> bench()
<div></div>
0.00022077560424804688
>>> bench()
<div></div>
0.0002658367156982422
>>> bench()
<div></div>
0.00024509429931640625
>>> bench()
<div></div>
0.00021338462829589844
>>> bench()
<div></div>
0.00019860267639160156
>>> 
