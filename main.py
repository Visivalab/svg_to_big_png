import os
import math

iterations = 35
svgHeight = 3259
svgWidth = 2244
#svgHeight = 99
#svgWidth = 91
exportHeight = 1500000
filename = "layoutmappaHERA.svg"

# probabilmente è possibile velocizzare il tutto usando parallelismo
for x in range(0, iterations):
    for y in range(0, iterations):
        command = """inkscape --export-area=%s:%s:%s:%s --export-filename=%s.png --export-height=%s \
                    %s""" %(x * math.ceil(svgWidth / iterations), y * math.ceil(svgHeight / iterations),
                            x * math.ceil(svgWidth / iterations) + math.ceil(svgWidth / iterations),
                            y * math.ceil(svgHeight / iterations) + math.ceil(svgHeight / iterations),
                            str(x) + "-" + str(y),
                            exportHeight,
                            filename)
        os.system(command)