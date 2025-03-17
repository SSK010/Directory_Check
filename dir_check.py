import os

def check_directory(path):
    """Recursively checks directories and lists if they are empty or contain files."""
    results = []
    
    # Ensure the path exists and is a directory
    if not os.path.exists(path) or not os.path.isdir(path):
        results.append(f"Invalid path: {path}")
        return results

    # Walk through the directory
    for root, dirs, files in os.walk(path):
        # Check if the current directory is empty
        if not dirs and not files:
            results.append(f"{root} empty")
        else:
            # If there are files, record the directory and the files found
            if files:
                results.append(f"{root} contains file(s): {', '.join(files)}")
    
    return results

def save_results(results, save_path, filename):
    """Save the results to a text file in the specified location."""
    full_path = os.path.join(save_path, filename)
    
    # Ensure the directory exists
    os.makedirs(save_path, exist_ok=True)

    try:
        with open(full_path, 'w') as file:
            for result in results:
                file.write(result + "\n")
        print(f"Results saved to {full_path}")
    except Exception as e:
        print(f"Error saving results: {e}")

def main():
    # Ask the user for the directory path to check
    source_path = input("Enter the path of the directory to check: ")

    # Get the results of the directory check
    results = check_directory(source_path)

    # Ask for the filename and path to save the results
    save_path = input("Enter the path where the results should be saved: ")
    filename = input("Enter the filename to save the results (e.g., 'results.txt'): ")

    # Save the results to the specified text file
    save_results(results, save_path, filename)

if __name__ == "__main__":
    main()
