import ee

ee.Initialize()

# Import the Current Glacier Collection
data = ee.FeatureCollection("GLIMS/current")

# Initial date of interest (inclusive).
initial_date = '2000-01-01'

# Final date of interest (exclusive).
final_date = '2020-01-01'

# Correct bands of data
data = data.filterDate(initial_date, final_date)

# Location of the biggest glacer in Alaska: Bering Glacier
beringGlacier_lon = -143.0240662617101
beringGlacier_lat = 60.406796113351575
beringGlacier_poi = ee.Geometry.Point(beringGlacier_lon, beringGlacier_lat)

scale = 306  # scale in meters

print(data)

"""
# Print the elevation near Lyon, France.
elv_urban_point = elv.sample(u_poi, scale).first().get('elevation').getInfo()
print('Ground elevation at urban point:', elv_urban_point, 'm')

# Calculate and print the mean value of the LST collection at the point.
lst_urban_point = lst.mean().sample(u_poi, scale).first().get('LST_Day_1km').getInfo()
print('Average daytime LST at urban point:', round(lst_urban_point*0.02 -273.15, 2), '°C')

# Print the land cover type at the point.
lc_urban_point = lc.first().sample(u_poi, scale).first().get('LC_Type1').getInfo()
print('Land cover value at urban point is:', lc_urban_point)
"""
