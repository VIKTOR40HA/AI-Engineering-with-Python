import sys
materials = {"shards":0,
         "fragments": 0,
         "motes":0 }
junk = {}
winner = ""
for line in sys.stdin:
    input_line = line.split()
    
for index in range(0,len(input_line),2):
    quantity = int(input_line[index])
    material = input_line[index+1]
    material = material.lower()
    if material in materials.keys():
        materials[material] += quantity
        if materials[material] >=250:
            if material =="shards":
                winner = "Shadowmourne"
            elif material =="fragments":
                winner = "Valanyr"
            else:
                winner = "Dragonwrath"
            materials[material] -= 250
            break
    else:
        if material in junk:
            junk[material] += quantity

        else:
            junk[material] = quantity
if winner !="":
    print(f"{winner} obtained!")
for key, value in materials.items():
    print(f"{key}: {value}")
for key, value in junk.items():
    print(f"{key}: {value}")

