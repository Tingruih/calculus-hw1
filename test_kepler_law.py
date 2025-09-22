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
    # TODO: Calculate the mean squared error between model and actual data
    
    # 使用擬合模型計算預測週期
    predicted_periods = a * (distances ** b)
    
    # 計算預測值與實際值之間的差的平方
    squared_errors = (predicted_periods - periods) ** 2
    
    # 計算平均平方誤差
    mse = np.mean(squared_errors)
    
    return mse

def kepler_law_test(period1, distance1, period2, distance2):
    # TODO: Design and implement an error to compare (period1, distance1) and (period2, distance2)
    # according to the Kepler's Third Law (period^2 is proportional to distance^3)
    
    # 根據克卜勒第三定律，T^2/d^3 對所有行星應該是常數
    # 計算兩個行星的 T^2/d^3 比值
    ratio1 = (period1 ** 2) / (distance1 ** 3)
    ratio2 = (period2 ** 2) / (distance2 ** 3)
    
    # 計算比值間的絕對差異，作為誤差指標
    diff = abs(ratio1 - ratio2)
    
    return diff

# Main program execution
def main():
    # TODO: Replace these data with real data in the lecture slide
    # 根據提供的圖片資料更新行星資料
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    distances = np.array([0.387, 0.723, 1.000, 1.523, 5.203, 9.541, 19.190, 30.086])  # In astronomical units (AU)
    periods = np.array([0.241, 0.615, 1.000, 1.881, 11.861, 29.457, 84.008, 164.784])  # In Earth years

    # Fit power model
    a, b = period_vs_distance_fit(distances, periods)
    print(f"Fitted power model: T = {a:.4f} * d^{b:.4f}")

    # Draw plot and save image
    draw_period_vs_distance(distances, periods, a, b)
    print("Plot saved as 'period_vs_distance.png'")

    # Calculate MSE
    mse = calculate_model_mse(distances, periods, a, b)
    print(f"Mean Squared Error (MSE): {mse:.6f}")

    # Test Kepler's Law for all planets against Earth
    print("\n--- Kepler's Law Test (comparing each planet to Earth) ---")
    earth_idx = planets.index("Earth")
    
    for i, planet in enumerate(planets):
        # 跳過地球本身
        if i == earth_idx:
            continue
        
        diff = kepler_law_test(
            period1=periods[earth_idx],
            distance1=distances[earth_idx],
            period2=periods[i],
            distance2=distances[i]
        )
        print(f"Difference between Earth and {planet:<8}: {diff:.6f}")


if __name__ == "__main__":
    main()
