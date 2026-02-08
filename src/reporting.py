def generate_summary(summary_dict, path):
    with open(path, "w", encoding="utf-8") as f:   
        f.write("DATA ANALYSIS SUMMARY REPORT\n") 
        f.write("="*40 + "\n\n")

        for key, value in summary_dict.items():
            f.write(f"{key}: {value}\n")

    print("Report generated successfully.")


