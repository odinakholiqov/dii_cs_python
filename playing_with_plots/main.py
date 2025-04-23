import matplotlib.pyplot as plt

def main():
    print("Hello from playing-with-plots!")

    x = [1, 2, 3, 4]
    y = [4, 6, 2, 1]

    plt.plot(
        x, y,
        color="red",
        linestyle="--"
    )
    plt.title("My graph")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
