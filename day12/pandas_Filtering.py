import pandas as pd

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day12\\test01.csv")

tall_pokemon = df[df['Height'] > 2]
heavy_pokemon = df[df['Weight'] > 100]
water_pokemon = df[df['Type1'] == 'Water']
fire_and_flying_pokemon = df[(df['Type1'] == 'Fire') &
                             (df['Type2'] == 'Flying')]


print(fire_and_flying_pokemon)