# GraphVisualiser (Python Data Visualization Tool)
# Tech Stack: Python, Matplotlib
# Developed by Deepanshu Yadav

import matplotlib.pyplot as plt

def graph_visualiser():
    print("=== Graph Visualiser ===")
    
    # Step 1: Take input from user
    data_input = input("Enter a list of numbers separated by commas: ")
    
    try:
        # Convert input string to list of floats/integers
        data = [float(x.strip()) for x in data_input.split(",")]
        
        if len(data) == 0:
            print("No data entered. Please try again.")
            return
        
    except ValueError:
        print("Invalid input! Please enter only numbers separated by commas.")
        return
    
    # Step 2: Generate indices for x-axis
    indices = list(range(1, len(data) + 1))
    
    # Step 3: Create subplots (5 graphs in one frame)
    fig, axs = plt.subplots(3, 2, figsize=(10, 10))
    fig.suptitle("Graph Visualiser - Multiple Views of Your Data", fontsize=14, fontweight='bold')
    
    # Line Graph
    axs[0, 0].plot(indices, data, marker='o', color='b')
    axs[0, 0].set_title("Line Graph")
    axs[0, 0].set_xlabel("Index")
    axs[0, 0].set_ylabel("Value")
    
    # Bar Graph
    axs[0, 1].bar(indices, data, color='orange')
    axs[0, 1].set_title("Bar Graph")
    axs[0, 1].set_xlabel("Index")
    axs[0, 1].set_ylabel("Value")
    
    # Horizontal Bar Graph
    axs[1, 0].barh(indices, data, color='green')
    axs[1, 0].set_title("Horizontal Bar Graph")
    axs[1, 0].set_xlabel("Value")
    axs[1, 0].set_ylabel("Index")
    
    # Pie Chart
    axs[1, 1].pie(data, labels=indices, autopct='%1.1f%%', startangle=90)
    axs[1, 1].set_title("Pie Chart")
    
    # Histogram
    axs[2, 0].hist(data, bins=5, color='purple', edgecolor='black')
    axs[2, 0].set_title("Histogram")
    axs[2, 0].set_xlabel("Value Range")
    axs[2, 0].set_ylabel("Frequency")
    
    # Hide unused subplot (bottom right corner)
    axs[2, 1].axis('off')
    
    # Adjust layout
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Run the visualizer
if __name__ == "__main__":
    graph_visualiser()
