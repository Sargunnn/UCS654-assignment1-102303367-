import sys
import pandas as pd
import numpy as np
import os

def topsis(input_file, weights, impacts, output_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file not found")

    # Read Excel or CSV
    if input_file.endswith(".xlsx"):
        data = pd.read_excel(input_file)
    else:
        data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        raise Exception("Input file must contain at least 3 columns")

    matrix = data.iloc[:, 1:].values

    try:
        matrix = matrix.astype(float)
    except:
        raise Exception("All criteria columns must be numeric")

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    if len(weights) != len(impacts) or len(weights) != matrix.shape[1]:
        raise Exception("Weights, impacts and columns count must match")

    for i in impacts:
        if i not in ['+', '-']:
            raise Exception("Impacts must be + or -")

    # Normalization
    norm = matrix / np.sqrt((matrix ** 2).sum(axis=0))
    weighted = norm * weights

    # Ideal best & worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted[:, i].max())
            ideal_worst.append(weighted[:, i].min())
        else:
            ideal_best.append(weighted[:, i].min())
            ideal_worst.append(weighted[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Distances
    d_pos = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_neg = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = d_neg / (d_pos + d_neg)

    data["Topsis Score"] = score
    data["Rank"] = data["Topsis Score"].rank(ascending=False).astype(int)

    # SAVE OUTPUT (this was missing earlier)
    if output_file.endswith(".xlsx"):
        data.to_excel(output_file, index=False)
    else:
        data.to_csv(output_file, index=False)

    print("✅ Result saved to", output_file)


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python -m topsis <InputFile> <Weights> <Impacts> <OutputFile>")
        sys.exit(1)

    topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
