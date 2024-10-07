import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("clash_of_clans.csv", nrows=100)
df.to_csv('clash_of_clans_reducido.csv', index=False)