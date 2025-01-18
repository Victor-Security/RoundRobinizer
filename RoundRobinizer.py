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

def roundrobin_domains(df):
    """
    Perform round-robin distribution of domains grouped by unique values.

    Args:
        df (pd.DataFrame): DataFrame with 'domain' column.

    Returns:
        pd.DataFrame: DataFrame with reordered domains in round-robin order.
    """
    df['group_idx'] = df.groupby('domain').cumcount()
    df.sort_values(by=['group_idx', 'domain'], inplace=True)
    return df[['domain']].drop_duplicates()

def generate_fuzz_list(domains, fuzz_patterns, output_file):
    """
    Append fuzz patterns to domains while preserving round-robin order.

    Args:
        domains (pd.DataFrame): DataFrame with 'domain' column in round-robin order.
        fuzz_patterns (list): List of fuzzing patterns.
        output_file (str): Path to the output file.

    Returns:
        None
    """
    with open(output_file, 'w') as outfile:
        for pattern in fuzz_patterns:
            fuzzed_urls = [f"https://{domain}/{pattern}" for domain in domains['domain']]
            fuzzed_df = pd.DataFrame({'url': fuzzed_urls})
            fuzzed_df['url'].to_csv(outfile, index=False, header=False, mode='a', lineterminator='\n')

def create_fuzz_list(domains_file, fuzz_file, output_file):
    """
    Create a fuzz list by appending each fuzz pattern to all domains in round-robin order.

    Args:
        domains_file (str): Path to the file containing domains.
        fuzz_file (str): Path to the fuzzing pattern file.
        output_file (str): Path to the output file.

    Returns:
        None
    """
    try:
        with open(fuzz_file, 'r') as f:
            fuzz_patterns = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading fuzz file: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(domains_file, 'r') as infile:
            domains = pd.DataFrame({'domain': [line.strip() for line in infile if line.strip()]})
    except Exception as e:
        print(f"Error reading domains file: {e}", file=sys.stderr)
        sys.exit(1)

    generate_fuzz_list(domains, fuzz_patterns, output_file)

def main():
    parser = argparse.ArgumentParser(
        description="Round-robin domains from a text file and optionally generate fuzzed lists."
    )
    parser.add_argument(
        "-i", "--input", type=str, help="Input text file containing URLs. Reads from stdin if not provided."
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Output text file. Writes to stdout if not provided."
    )
    parser.add_argument(
        "--fuzz", type=str, help="Path to a fuzzing pattern file to generate a fuzzed list."
    )
    parser.add_argument(
        "--mode", type=str, choices=['roundrobinizer', 'roundrobinizerfuzzlist'],
        default='roundrobinizer', help="Choose the operation mode: roundrobinizer or roundrobinizerfuzzlist."
    )
    args = parser.parse_args()

    # Print branding message
    print("Powered by Victor Security (https://victorsecurity.com.br)")
    print("")

    if not args.input:
        print("Error: Input file is required.", file=sys.stderr)
        sys.exit(1)

    if args.mode == 'roundrobinizerfuzzlist' and not args.fuzz:
        print("Error: --fuzz argument is required in roundrobinizerfuzzlist mode.", file=sys.stderr)
        sys.exit(1)

    if args.mode == 'roundrobinizer':
        try:
            with open(args.input, 'r') as infile:
                urls = pd.DataFrame({'url': [line.strip() for line in infile if line.strip()]})
            urls['domain'] = extract_domains(urls['url'])

            print(f"Number of unique domains: {urls['domain'].nunique()}")
            print("Processing Round-Robin Algorithm for domains...")
            print("Please wait...")

            reordered_df = roundrobin_domains(urls)

            if args.output:
                reordered_df.to_csv(args.output, index=False, header=False)
            else:
                reordered_df.to_csv(sys.stdout, index=False, header=False)
        except Exception as e:
            print(f"Error processing input file: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.mode == 'roundrobinizerfuzzlist':
        if not args.output:
            print("Error: Output file is required for roundrobinizerfuzzlist mode.", file=sys.stderr)
            sys.exit(1)

        print("Processing domains for round-robin...")
        try:
            with open(args.input, 'r') as infile:
                urls = pd.DataFrame({'url': [line.strip() for line in infile if line.strip()]})
            urls['domain'] = extract_domains(urls['url'])

            reordered_domains = roundrobin_domains(urls)

            print("Generating fuzzed list...")
            create_fuzz_list(
                domains_file=args.input,
                fuzz_file=args.fuzz,
                output_file=args.output
            )
        except Exception as e:
            print(f"Error during fuzz list generation: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
