import numpy as np
import pandas as pd
import cartopy

filenames = ["TestData.txt"]
#filenames = ["McGovern1.asc", "McGovern2.asc", "McGovern3.asc", "McGovern4.asc", "McGovern5.asc"]
columns = ["Date", "Time", "Lat", "Lon", "Magnitude", "Type"]

print("Reading in files...")

for filename in filenames:
    dataframe = pd.read_csv(filename, header = None, delim_whitespace=True, names=columns)

print(dataframe)

coords = [[],[]]
counter = []

len = dataframe["Date"].count()

top = 49.3457868 # north lat
bottom =  24.7433195 # south lat

left = -124.7844079 # west long
right = -66.9513812 # east long

lats = np.arange(bottom, top, 0.1)
lons = np.arange(left, right, 0.1)

df_test = pd.DataFrame({'Lat': dataframe["Lat"],'Lon': dataframe["Lon"], 'Time': dataframe['Time'], 'Strike': True})
df_test = df_test.set_index(['Lat', 'Lon', 'Time'])

xr_test = df_test.to_xarray()

#da = xr.DataArray(dims=["Lat", "Lon"],coords=dict(lat=(["LatNorth", "LatSouth"], lats),lon=(["LonWest", "LonEast"], lons)),
#    attrs=dict(description="Lightning graph", units="number of strikes",),)
#
#da = da.isel(lat=coords[0][0], lon=coords[1][0]) +1

print(df_test)
for n in xr_test["Lat"]:
    print(n)
for n in xr_test["Lon"]:
    print(n)
print(xr_test)


lightning = xr_test.isel()
lightning.plot()