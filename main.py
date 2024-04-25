import pandas as pd
import glob
import os


def ingest_directory(directory: str, output_file: str):

    sentiment: list[str] = []
    phrase: list[str] = []
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' not found")
    files: list[str] = glob.glob(f"{directory}/*/*.txt")
    for file in files:
        with open(file, "r") as f:
            lines = f.readlines()
            sentiment.append(file.split("/")[-2])
            phrase.append(lines[0].strip())
    df = pd.DataFrame({"phrase": phrase, "sentiment": sentiment})
    df.to_csv(output_file, index=False)


def main():
    ingest_directory("test", "test_dataset.csv")
    ingest_directory("train", "train_dataset.csv")


if __name__ == "__main__":
    main()
