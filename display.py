import os
import pathlib
import random
import numpy as np
import matplotlib.pyplot as plt


ROOT_PATH = pathlib.Path(__file__).resolve().parent.absolute()
RAW_PATH = os.path.join(ROOT_PATH, 'dataset', 'raw')
if not os.path.exists(RAW_PATH):
    raise RuntimeError("Data does not exist, please download it")


def main():
    """
    Chooses randomly one of the 100 signatures to display, and then runs display_9_signatures
    """
    idx = random.randint(0, 99)
    display_9_signatures(idx)


def display_9_signatures(sig_idx):
    """
    Prints 9 randomly chosen signatures, taken from the 25 availiables
    Args:
    - sig_idx: index of the signature to show
    """

    list_idx = random.sample(range(0, 25), 9)

    sig_to_display = [f'{sig_idx}v{idx}.txt' for idx in list_idx]
    list_sig_data = []
    list_sig_dotted = []

    for sig in sig_to_display:
        fpath = os.path.join(RAW_PATH, sig)
        data = []
        with open(fpath, 'r') as f:
            for line in f:
                line = line.strip('\n\r')
                line_val = [int(num) for num in line.split(' ')]
                data.append(line_val)
        data = np.array(data)
        list_sig_data.append(data)
        list_sig_dotted.append(data[:, 2] != 0)

    fig = plt.figure(figsize=(12, 8))

    for i in range(1, 10):
        ax = fig.add_subplot(3, 3, i)
        data = list_sig_data[i - 1]
        dotted = list_sig_dotted[i - 1]
        ax.plot(data[dotted][:, 0], data[dotted][:, 1])
        ax.plot(data[np.invert(dotted)][:, 0], data[np.invert(dotted)][:, 1], linestyle='dashed')
        ax.axis('scaled')
        ax.axis('off')

    fig.suptitle(f'9 examples of signature {sig_idx}')
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
