# RoundRobinizer

**RoundRobinizer** is an efficient Python tool designed to organize URLs into a **round-robin order** based on their domains. It is ideal for distributed scanning, load balancing, and web security testing, ensuring systematic and balanced URL distribution across tasks.

---

## Features

- **Domain-Based Grouping**: Extracts and groups URLs by their domains for organized processing.
- **Round-Robin Distribution**: Balances URL processing across domains in a cyclic manner.
- **Fuzz Pattern Integration**: Append fuzzing patterns to URLs in round-robin order for advanced testing scenarios.
- **Customizable Fuzz Separators**: Define a custom separator between URLs and fuzz patterns.
- **Scalable Performance**: Handles large datasets efficiently, powered by `pandas` and `tldextract`.
- **User-Friendly CLI**: Easily integrates into pipelines for automation and batch operations.

---

## Installation

### Prerequisites

- Python 3.8 or higher

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

### Cloning the Repository

To download the project and its folder structure, clone the repository using git:

```bash
git clone https://github.com/Victor-Security/RoundRobinizer.git
```

This will create a folder named `RoundRobinizer` containing all the necessary files and directories.

---

## Usage

### Input and Output Formats

- **Input**: A plain text file (`.txt`) with one URL per line.
- **Output**: A plain text file with URLs reordered in a round-robin pattern or fuzzed URLs based on provided patterns.

### Command-Line Usage

Run the script as follows:

```bash
python RoundRobinizer.py -i input.txt -o output.txt
```

- `-i`: Input file containing the list of URLs.
- `-o`: Output file to save the reordered or fuzzed URLs.
- `--fuzz`: Optional, path to a file containing fuzzing patterns.
- `--fuzz_separator`: Optional, defines the separator between the URL and fuzz pattern (default: `/`).
- `--mode`: Choose between:
  - `roundrobinizer`: Reorder URLs into a round-robin pattern.
  - `roundrobinizerfuzzlist`: Append fuzzing patterns to URLs in round-robin order.

### Example

#### Reordering URLs

**Input File (`input.txt`):**
```
http://example.com/page1
https://sub.example.com/page2
http://test.com/page3
https://example.com/page4
http://test.com/page5
```

**Command:**
```bash
python RoundRobinizer.py -i input.txt -o output.txt --mode roundrobinizer
```

**Output File (`output.txt`):**
```
http://example.com/page1
http://test.com/page3
https://sub.example.com/page2
https://example.com/page4
http://test.com/page5
```

#### Generating Fuzzed URLs with Custom Separator

**Fuzz File (`fuzz_patterns.txt`):**
```
!.gitignore
.env
config.php
```

**Command (Using Default `/` Separator):**
```bash
python RoundRobinizer.py -i input.txt -o fuzzed_output.txt --fuzz fuzz_patterns.txt --mode roundrobinizerfuzzlist
```

**Output File (`fuzzed_output.txt`):**
```
https://example.com/!.gitignore
https://test.com/!.gitignore
https://sub.example.com/!.gitignore
https://example.com/.env
https://test.com/.env
https://sub.example.com/.env
https://example.com/config.php
https://test.com/config.php
https://sub.example.com/config.php
```

**Command (Using `-` as Separator):**
```bash
python RoundRobinizer.py -i input.txt -o fuzzed_output_custom.txt --fuzz fuzz_patterns.txt --fuzz_separator "-" --mode roundrobinizerfuzzlist
```

**Output File (`fuzzed_output_custom.txt`):**
```
https://example.com-!.gitignore
https://test.com-!.gitignore
https://sub.example.com-!.gitignore
https://example.com-.env
https://test.com-.env
https://sub.example.com-.env
https://example.com-config.php
https://test.com-config.php
https://sub.example.com-config.php
```

---

### Progress Indicators

The script provides:
- The number of unique domains.
- Progress updates:
  ```
  Powered by Victor Security (https://victorsecurity.com.br)

  Number of unique domains: 3
  Processing Round-Robin Algorithm...
  Please wait....
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

