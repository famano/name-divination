#!/user/bin/env python3

import click
import ast
from components import getTrylist, getRank, getUnsei

@click.command()
@click.option("--family_name", required=True)
@click.option("--first_name", required=True)
@click.option("--count", default=10)
def main(family_name, first_name, count):
    family_name = ast.literal_eval(family_name)
    first_name = ast.literal_eval(first_name)

    try_list = getTrylist(first_name) # 名字は決まっているため、名前のみを探索

    name_list = []
    for single_try in try_list:
        unsei = getUnsei(family_name, single_try)
        unsei_rank = getRank(unsei)
        name_list.append([family_name,single_try,unsei,unsei_rank])

    result = sorted(name_list, key=lambda data: sum(data[3]))

    for line in result[0:count]: 
        print(line, sum(line[3]))
    
if __name__ == "__main__":
    main()