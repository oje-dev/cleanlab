# Instructions

The lemon.ipynb file should contain all of the code output and details of the task - if you would like to run the cells yourself and see the code in action, please do the following:

1. First, create a new virtual environment in the root directory:

    ```sh
    python3.11 -m venv lemon
    ```
2. Activate the virtual environment:
    ```sh
    source lemon/bin/activate
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Open lemon.ipynb in Jupyter Notebooks or VSCode
5. Ensure that the notebook is using the virtualenv that you just created
6. Click the run all button to run all the cells.
7. To Run the tests use:
    ```sh
    python -m pytest tests/lexical_quality/test_lexical_quality.py
    ```
