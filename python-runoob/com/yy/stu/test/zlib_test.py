import zlib;
import doctest;

s = b"witch which has which wiches wrist watch";
print("before compress, s=", s);
print("before compress, s.length=", len(s));

t = zlib.compress(s);
print("after compress, t=", t);
print("after compress, t.length=", len(t));

d = zlib.decompress(t);
print("after decompress, d=", d);

doctest.testmod();