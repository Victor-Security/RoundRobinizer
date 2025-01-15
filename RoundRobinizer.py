import pandas as pd
import argparse
import sys
import tldextract

def extract_domains(urls):
    """
    Efficiently extract domains from a Series of URLs using vectorized operations.

    Args:
        urls (pd.Series): Series of URLs.

    Returns:
        pd.Series: Series of extracted domains.
    """
    extracted = urls.apply(tldextract.extract)
    return extracted.apply(lambda x: f"{x.domain}.{x.suffix}")

def roundrobin_urls(df):
    """
    Perform round-robin distribution of URLs grouped by domains.

    Args:
        df (pd.DataFrame): DataFrame with 'domain' and 'url' columns.

    Returns:
        pd.DataFrame: DataFrame with reordered URLs in round-robin order.
    """
    # Sort URLs by domain, ensuring stable round-robin ordering
    df['group_idx'] = df.groupby('domain').cumcount()
    df.sort_values(by=['group_idx', 'domain'], inplace=True)
    return df[['url']]

def main():
    parser = argparse.ArgumentParser(
        description="Round-robin URLs from a text file based on their domains."
    )
    parser.add_argument(
        "-i", "--input", type=str, help="Input text file. Reads from stdin if not provided."
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Output text file. Writes to stdout if not provided."
    )
    args = parser.parse_args()

    # Print branding message
    print("Powered by Victor Security (https://victorsecurity.com.br)")
    print("")

    # Read input data as a plain text file
    if args.input:
        try:
            with open(args.input, 'r') as infile:
                urls = pd.DataFrame({'url': [line.strip() for line in infile if line.strip()]})
        except Exception as e:
            print(f"Error reading input file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        try:
            urls = pd.DataFrame({'url': [line.strip() for line in sys.stdin if line.strip()]})
        except Exception as e:
            print(f"Error reading input from stdin: {e}", file=sys.stderr)
            sys.exit(1)

    # Ensure URLs are valid
    if urls.empty:
        print("Input file is empty or improperly formatted.", file=sys.stderr)
        sys.exit(1)

    # Extract domains and add to DataFrame
    df = urls
    df['domain'] = extract_domains(df['url'])

    # Print the number of unique domains
    domain_count = df['domain'].nunique()
    print(f"Number of unique domains: {domain_count}")

    # Indicate processing start
    print("Processing Round-Robin Algorithm...")
    print("Please wait...")

    # Perform round-robin processing
    reordered_df = roundrobin_urls(df)

    # Output results efficiently
    if args.output:
        reordered_df['url'].to_csv(args.output, index=False, header=False)
    else:
        reordered_df['url'].to_csv(sys.stdout, index=False, header=False)

if __name__ == "__main__":
    main()
