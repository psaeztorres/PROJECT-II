import matplotlib.pyplot as plt
import os

def save_and_open (name):
    plt.savefig(f'images/{name}.png', bbox_inches='tight')
    command2 = f"start images/{name}.png"
    os.system(command2)
    plt.show()