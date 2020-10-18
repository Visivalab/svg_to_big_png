import os

iterations = 40
svgHeight = 3259
svgWidth = 2244

# probabilmente è possibile velocizzare il tutto usando parallelismo
for x in range(0, iterations):
    for y in range(0, iterations):
        command = """inkscape --export-area=%s:%s:%s:%s --export-filename=%s.png --export-height=40000
                    layoutmappaHERA.svg""" %(x * (svgWidth / iterations), y * (svgHeight / iterations),
                                             x * (svgWidth / iterations) + (svgWidth / iterations),
                                             y * (svgHeight / iterations) + (svgHeight / iterations),
                                             str(x) + "-" + str(y))
        os.system(command)