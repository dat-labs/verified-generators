# verified-generators

This repository contains verified generators [?](http://dat.com/what-are-verified-actors) to be used in the `dat` project.

## Local Development Setup

To run this project locally, follow these steps:

### 0. Fork this repo on Github

This can be done by clicking [here](https://github.com/dat-labs/verified-generators/fork).

### 1. Set up Python Environment

Make sure you have `Python 3.10` (minimum version) installed on your computer. If not, you can download and install it from [Python's official website](https://www.python.org/downloads/).

### 2. Clone the Repository

```bash
git clone git@github.com:{your-github-username}/verified-generators.git
```

### 3. Create a Virtual Environment
Navigate into the cloned directory and create a virtual environment using your preferred method. If you're using `venv`, you can create a virtual environment like this:

```bash
cd verified-generators
python -m venv .venv
```

### 4. Activate the Virtual Environment
Activate the virtual environment. The command to activate it depends on your operating system.

- On Unix and MacOS:
    ```bash
    source .venv/bin/activate
    ```
- On Windows:
    ```bash
    .venv\Scripts\activate
    ```

### 5. Install Dependencies

```bash
pip install poetry
poetry install
```

This will install all the necessary dependencies for the project.

## Developing
Please refer the detailed guide given [here](http://path-to-guide.com).

## Contributing
If you want to contribute to this project, please read the [contribution guidelines](CONTRIBUTING).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries or issues regarding the project, feel free to contact us at <team@datlabs.com>.