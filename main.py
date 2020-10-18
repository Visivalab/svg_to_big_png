import os

for x in range(0, 25):
    for y in range(0, 25):
        command = """inkscape --export-area=%s:%s:%s:%s --export-filename=%s.png --export-height=40000
                    layoutmappaHERA.svg""" %(x * 89, y * 130, x * 89 + 89, y * 130 + 130, str(x) + "-" + str(y))
        os.system(command)