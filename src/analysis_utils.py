def sales_summary(df):
    if "Sales" in df.columns:
        col = "Sales"
    elif "Total" in df.columns:
        col = "Total"
    elif "Revenue" in df.columns:
        col = "Revenue"
    else:
        raise ValueError("No sales column found in dataset.")

    return {
        "Total Sales": df[col].sum(),
        "Average Sales": df[col].mean()
    }


def top_categories(df, col, metric):
    return df.groupby(col)[metric].sum().sort_values(ascending=False)
