with open('code/flight_prediction_delay.ipynb', 'r') as f:
    lines = f.readlines()

with open('flights_prediction.ipynb', 'w') as f:
    for line in lines:
        f.write(line.replace('"execution_count": "null"', '"execution_count": null'))
