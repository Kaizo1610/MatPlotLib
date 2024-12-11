import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

def draw_map():
    fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': ccrs.Miller()})

    # Add coastlines and countries
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    # Add gridlines
    gl = ax.gridlines(draw_labels=True)
    gl.top_labels = False
    gl.right_labels = False

    # Show the plot
    plt.title('World Map')
    plt.show()

if __name__ == "__main__":
    draw_map()