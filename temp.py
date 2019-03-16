f = open('script2', 'w')
for i in range(45):
    a = 'sphere\n0 0 0 45\ntorus\n-87 0 0 30 60\ntorus\n43 0 75 30 60\ntorus\n43 0 -75 30 60\nscale\n2 2 2\nident\nrotate\ny '
    a += str(int(8*i))
    a += '\nrotate\nx 40\nmove\n250 250 0\napply\nsave\nimg'
    a += str(i)
    a += '.png\nclear\n'
    f.write(a)
f.close()
