import json
stories = 1

header = '''
summon falling_block ~ ~1 ~ {Time: 1,BlockState: {Name:redstone_block
    },Passengers: [
        {id:armor_stand,Health: 0,Passengers: [
                {id:falling_block,Time: 1,BlockState: {Name:activator_rail
                    },Passengers: [
                        {id:command_block_minecart,Command:"gamerule commandBlockOutput false"
                        },
                        {id:command_block_minecart,Command:"data merge block ~ ~-2 ~ {auto: 0
                            }"
                        },
'''

at2 = '''
{
    "block": [
        {
            "id": "command_block_minecart",
            "Command": "fill ~1 ~-3 ~1 ~9 ~3 ~9 minecraft:quartz_block hollow"
        },
        {
            "id": "command_block_minecart",
            "Command": "fill ~4 ~-1 ~1 ~6 ~1 ~1 glass outline"
        },
        {
            "id": "command_block_minecart",
            "Command": "fill ~1 ~1 ~4 ~1 ~1 ~6 glass outline"
        },
        {
            "id": "command_block_minecart",
            "Command": "fill ~1 ~-1 ~7 ~1 ~1 ~7 glass outline"
        },
        {
            "id": "command_block_minecart",
            "Command": "fill ~1 ~-1 ~3 ~1 ~1 ~3 glass outline"
        },
        {
            "id": "command_block_minecart",
            "Command": "fill ~9 ~-1 ~4 ~9 ~1 ~6 glass outline"
        },
        {
            "id": "command_block_minecart",
            "Command": "fill ~4 ~-1 ~9 ~6 ~1 ~9 glass outline"
        },
        {
            "id": "command_block_minecart",
            "Command": "fill ~4 ~-3 ~4 ~6 ~-3 ~6 minecraft:sea_lantern outline"
        },
        {
            "id": "command_block_minecart",
            "Command": "fill ~4 ~3 ~4 ~6 ~3 ~6 minecraft:sea_lantern outline"
        }
    ]
}
'''

footer = '''
,
                    {'id':'command_block_minecart','Command':'setblock ~1 ~-2 ~5 minecraft:oak_door[facing=east,half=lower
                        ]'
                    },
                    {'id':'command_block_minecart','Command':'setblock ~1 ~-1 ~5 minecraft:oak_door[facing=east,half=upper
                        ]'
                    },
                    {'id':'command_block_minecart','Command':'setblock ~ ~1 ~ command_block{auto: 1,Command:fill ~ ~ ~ ~ ~-2 ~ air
                        }'
                    },
                    {'id':'command_block_minecart','Command':'kill @e[type=command_block_minecart,distance=..1
                        ]'
                    }
                ]
            }
        ]
    }
]
}
'''



at2_json = json.loads(at2)

at2_whole = str(at2_json["block"])[1:-1]

command = header + at2_whole + footer
# f = open("filename.json", 'w')
# f.write(command)

for x in at2_json["block"]:
    x["Command"] = "blah"
print(at2_json["block"])
print(at2_json["block"][0])
    # for y in x:
    #     print(y)