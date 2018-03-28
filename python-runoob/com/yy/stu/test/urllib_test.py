from urllib.request import urlopen;
from timeit import Timer;

for line in urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl"):
    line = line.decode('utf-8');
    if "EST" in line or "EDT" in line:
        print(line);

x = Timer("t=a; a=b; b=t", "a=1; b=2").timeit();
print("x=", x);

y = Timer("a,b=b,a", "a=1; b=2").timeit();
print("y=", y);