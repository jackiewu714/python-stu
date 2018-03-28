from com.yy.stu.obj.Point import Point

pt1 = Point();
pt2 = pt1;
pt3 = pt2;
print("id(pt1)=", id(pt1), "id(pt2)=", id(pt2), "id(pt3)=", id(pt3));

del pt1;
del pt2;
del pt3;
