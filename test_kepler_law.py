import numpy as np
import matplotlib.pyplot as plt
from kepler_law import *

def draw_period_vs_distance(distances, periods, a, b):
    # Draw original data and fitted power function curve, save as image file
    # Scatter plot of original data
    plt.scatter(distances, periods, color='blue', label='Observed Data')

    # Generate smooth curve using fitted model
    d_range = np.linspace(min(distances), max(distances), 100)
    T_fit = a * d_range**b

    # Plot fitted curve
    plt.plot(d_range, T_fit, color='red', label=f'Fitted Model: T = {a:.2f} * d^{b:.2f}')
    plt.xlabel('Distance (AU)')
    plt.ylabel('Period (years)')
    plt.title('Period vs. Distance')
    plt.legend()
    plt.grid(True)

    # Save the plot to a file instead of showing it
    plt.savefig("period_vs_distance.png", dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory

def calculate_model_mse(distances, periods, a, b):
    mse = 0
    # TODO: Calculate the mean squared error between model and actual data
    return mse

def kepler_law_test(period1, distance1, period2, distance2):
    diff = 0
    # TODO: Design and implement an error to compare (period1, distance1) and (period2, distance2)
    # according to the Kepler's Third Law (period^2 is proportional to distance^3)
    return diff

# Main program execution
def main():
    # Example data: [Mercury, Venus, Earth, Mars, Jupiter]
    # TODO: Replace these data with real data in the lecture slide
    distances = [0.39, 0.72, 1.00, 1.52, 5.20]  # In astronomical units (AU)
    periods =   [0.39, 0.72, 1.00, 1.52, 5.20]  # In Earth years

    # Fit power model
    a, b = period_vs_distance_fit(distances, periods)
    print(f"Fitted power model: T = {a:.4f} * d^{b:.4f}")

    # Draw plot and save image (TODO: Report the figure)
    draw_period_vs_distance(distances, periods, a, b)
    print("Plot saved as 'period_vs_distance.png'")

    # Calculate MSE
    mse = calculate_model_mse(distances, periods, a, b)
    print(f"Mean Squared Error (MSE): {mse:.6f}")

    # Test Kepler's Law (TODO: Report the errors)
    # An example:
    diff = kepler_law_test(period1=1.00, distance1=1.00, period2=1.88, distance2=1.88)
    print(f"Kepler Law Ratio Difference (Earth vs XXXX): {diff:.6f}")

if __name__ == "__main__":
    main()
