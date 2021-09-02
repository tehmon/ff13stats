characters = ["sazh", "lightning", "snow", "hope", "vanille", "fang"]
stats = ["hp", "str", "mag"]

def main():
    for c in characters:
        for s in stats:
            file_name = "../files/" + c + "_" + s + ".txt"
            with open(file_name, "w+") as f:
                pass

if __name__ == "__main__":
    main()
