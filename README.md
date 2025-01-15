# RoundRobinizer

**RoundRobinizer** is an efficient Python tool designed to organize URLs into a **round-robin order** based on their domains. It is ideal for distributed scanning, load balancing, and web security testing, ensuring systematic and balanced URL distribution across tasks.

---

## Features

- **Domain-Based Grouping**: Extracts and groups URLs by their domains for organized processing.
- **Round-Robin Distribution**: Balances URL processing across domains in a cyclic manner.
- **Scalable Performance**: Handles large datasets efficiently, powered by `pandas` and `tldextract`.
- **User-Friendly CLI**: Easily integrates into pipelines for automation and batch operations.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Required libraries:
  - `pandas`
  - `tldextract`

Install dependencies with pip:

```bash
pip install pandas tldextract
```

---

## Usage

### Input and Output Formats

- **Input**: A plain text file (`.txt`) with one URL per line.
- **Output**: A plain text file with URLs reordered in a round-robin pattern.

### Command-Line Usage

Run the script as follows:

```bash
python roundrobin_urls.py -i input.txt -o output.txt
```

- `-i`: Input file containing the list of URLs.
- `-o`: Output file to save the reordered URLs.

### Example

#### Input File (`input.txt`):
```
http://example.com/page1
https://sub.example.com/page2
http://test.com/page3
https://example.com/page4
http://test.com/page5
```

#### Command:
```bash
python roundrobin_urls.py -i input.txt -o output.txt
```

#### Output File (`output.txt`):
```
http://example.com/page1
http://test.com/page3
https://sub.example.com/page2
https://example.com/page4
http://test.com/page5
```

### Pipeline Usage

You can also use the script in a pipeline:

```bash
cat input.txt | python roundrobin_urls.py > output.txt
```

### Progress Indicators

The script provides:
- The number of unique domains.
- Progress updates:
  ```
  Powered by Victor Security (https://victorsecurity.com.br)

  Number of unique domains: 2
  Processing Round-Robin Algorithm...
  Please wait...
  ```

---

## Contributing

We welcome contributions to make **RoundRobinizer** even better! Feel free to:
- Fork this repository.
- Submit a pull request with your improvements.
- Report issues or suggest features in the [issues section](https://github.com/Victor-Security/RoundRobinizer/issues).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## About Us

**Powered by [Victor Security](https://victorsecurity.com.br)**  
Innovating web security solutions with performance, scalability, and efficiency in mind.
