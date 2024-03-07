
# old notebook
with open('../code/flights_prediction.ipynb', 'r') as f:
    lines = f.readlines()

# replace with new notebook
with open('../code/flights_prediction.ipynb', 'w') as f:
    for line in lines:
        f.write(line.replace('"execution_count": "null"', '"execution_count": null'))
