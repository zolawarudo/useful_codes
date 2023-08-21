# assign folder containing data
folder_path = r"C:/Users/Samuele/folder1"
# assign folder that stores pickled files
pickle_folder_path = r"C:/Users/Samuele/folder2"

# Loop through all CSV files in the folder
for filename in tqdm(os.listdir(folder_path)):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # Read the CSV file and store it as a Pandas DataFrame
        df = pd.read_csv(file_path, names = column_names, header = None)
        # Create the pickle file path by replacing the extension of the CSV file with ".pkl"
        pickle_path = os.path.join(pickle_folder_path, os.path.splitext(filename)[0] + ".pkl")
        # Save the DataFrame as a pickled file
        with open(pickle_path, "wb") as f:
            pickle.dump(df, f)
