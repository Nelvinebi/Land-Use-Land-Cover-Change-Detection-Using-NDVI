# land_use_land_cover_change_detection.py
"""
Land-Use Land-Cover Change Detection using NDVI (Synthetic Data)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n_points = 150

x = np.random.uniform(0, 100, n_points)
y = np.random.uniform(0, 100, n_points)

ndvi_t1 = np.random.choice([np.random.uniform(-0.1, 0.1),
                            np.random.uniform(0.1, 0.3),
                            np.random.uniform(0.3, 0.6),
                            np.random.uniform(0.6, 0.9)],
                            size=n_points)

change = np.random.normal(0, 0.1, n_points)
ndvi_t2 = np.clip(ndvi_t1 + change, -0.1, 0.9)

def classify_ndvi(value):
    if value < 0.1:
        return "Water"
    elif 0.1 <= value < 0.3:
        return "Urban"
    elif 0.3 <= value < 0.6:
        return "Agriculture"
    else:
        return "Forest"

landcover_t1 = [classify_ndvi(val) for val in ndvi_t1]
landcover_t2 = [classify_ndvi(val) for val in ndvi_t2]

change_detected = ["Changed" if landcover_t1[i] != landcover_t2[i] else "No Change"
                   for i in range(n_points)]

df = pd.DataFrame({
    "X": x,
    "Y": y,
    "NDVI_T1": ndvi_t1,
    "NDVI_T2": ndvi_t2,
    "LandCover_T1": landcover_t1,
    "LandCover_T2": landcover_t2,
    "Change": change_detected
})

print(df.head())

plt.figure(figsize=(8,5))
sns.kdeplot(df["NDVI_T1"], label="NDVI Time 1", fill=True)
sns.kdeplot(df["NDVI_T2"], label="NDVI Time 2", fill=True)
plt.title("NDVI Distribution Over Time")
plt.xlabel("NDVI")
plt.ylabel("Density")
plt.legend()
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="X", y="Y", hue="Change", style="LandCover_T2", s=80)
plt.title("Land Use Land Cover Change Detection (Synthetic)")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend(bbox_to_anchor=(1.05,1), loc="upper left")
plt.show()

df.to_excel("synthetic_land_use_land_cover_ndvi.xlsx", index=False)
print("Synthetic dataset saved as synthetic_land_use_land_cover_ndvi.xlsx")
