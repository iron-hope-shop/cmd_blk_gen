import json
import time
import math

X_OFFSET = 1
Y_OFFSET = -3
Z_OFFSET = 1


def building(x1, y1, z1, x2, y2, z2):
    body = f'{{"id": "command_block_minecart", "Command": "fill ~{x1} ~{y1} ~{z1} ~{x1+x2-1} ~{y1+y2-1} ~{z1+z2-1} minecraft:quartz_block hollow"}}'
    # w1 = f'{{"id": "command_block_minecart", "Command": "fill ~4 ~-1 ~1 ~6 ~1 ~1 glass outline"}}'
    # w2 = f'{{"id": "command_block_minecart", "Command": "fill ~1 ~1 ~4 ~1 ~1 ~6 glass outline"}}'
    # w3 = f'{{"id": "command_block_minecart", "Command": "fill ~1 ~-1 ~7 ~1 ~1 ~7 glass outline"}}'
    # w4 = f'{{"id": "command_block_minecart", "Command": "fill ~1 ~-1 ~3 ~1 ~1 ~3 glass outline"}}'
    # w5 = f'{{"id": "command_block_minecart", "Command": "fill ~9 ~-1 ~4 ~9 ~1 ~6 glass outline"}}'
    # w6 = f'{{"id": "command_block_minecart", "Command": "fill ~4 ~-1 ~9 ~6 ~1 ~9 glass outline"}}'
    return body


def building_block(xspacing, yspacing, size, amount):
    per_row = int(math.sqrt(amount))
    total_rows = int(amount/per_row)
    block = []
    for row in range(total_rows):
        for b in range(per_row):
            f = building(X_OFFSET+(xspacing*b)+(size*b), Y_OFFSET,
                         Z_OFFSET+(yspacing*row)+(size*row), size, size, size)
            block.append(f)
    return block


def create_command(payload):
    file_name = f'./out/{int(time.time())-1580000000}.json'
    with open(file_name, 'w') as f:
        f.write(payload)
    percent_total = round((len(payload)/32767*100), 2)
    print("* " * 35 +
          f"\nStored command in {file_name}.\n{len(payload)} Characters, {percent_total}% full.\n" + "* " * 35)


def compile(listOfBuilds):
    string = ''
    for i in listOfBuilds:
        string = string + i + ","
    return string


def build_payload(body):
    COMMAND_HEADER = 'summon falling_block ~ ~1 ~ {Time: 1,BlockState: {Name:redstone_block},Passengers: [{id:armor_stand,Health: 0,Passengers: [{id:falling_block,Time: 1,BlockState: {Name:activator_rail},Passengers: [{id:command_block_minecart,Command:"gamerule commandBlockOutput false"},{id:command_block_minecart,Command:"data merge block ~ ~-2 ~ {auto: 0}"},'
    COMMAND_FOOTER = '{"id":"command_block_minecart","Command":"setblock ~ ~1 ~ command_block{auto: 1,Command:fill ~ ~ ~ ~ ~-2 ~ air}"},{"id":"command_block_minecart","Command":"kill @e[type=command_block_minecart,distance=..1]"}]}]}]}'
    return COMMAND_HEADER + body + COMMAND_FOOTER


if __name__ == "__main__":
    # cube0 = building(X_OFFSET, Y_OFFSET, Z_OFFSET, 4, 4, 4)
    # cube1 = building(X_OFFSET+8, Y_OFFSET, Z_OFFSET, 4, 4, 4)
    # cube2 = building(X_OFFSET+16, Y_OFFSET, Z_OFFSET, 4, 4, 4)
    arr = building_block(10, 8, 5, 3)
    args = compile(arr)
    command = build_payload(args)
    create_command(command)
