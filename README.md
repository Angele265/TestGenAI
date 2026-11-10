# TestGenAI - AI-Powered Unit Test Generator
An intelligent Python code analysis tool that automatically analyses source code and generates unit test scenarios based on function parameters, conditional statements, return values, and exception handling.

## Project Overview

TestGenAI aims to simplify and accelerate software testing by automating the identification of test scenarios from Python source code.

The tool analyses a given Python function, identifies its structure and possible execution paths, and generates relevant test scenarios that can be used as a foundation for unit testing.

The project explores how Artificial Intelligence and automation can support software quality assurance and improve test coverage.

## Objectives
* Automatically analyse Python source code.
* Identify functions and their parameters.
* Extract conditional statements and validation rules.
* Generate positive and negative test scenarios.
* Support the development of automated unit tests.
* Explore AI-assisted software testing.

## Technologies Used
* Python 3.12
* Pytest
* Pytest-cov
* Streamlit
* Torch
* Transformers
* Sentencepiece
* Accelerate

## Project Structure

```
TestGenAI

├── data/
│   └── sample_code
│       └──calculator.py  
├── evaluation/
│   └── 
│
├──models/
│   ├── code_analyzer.py
│   ├── test_generator.py
│   ├── 
│   ├── 
│   └── 
│
├── tests/
│   ├── test_code_analyzer.py
│   ├── test_enviroment.py
│   ├── test_test_generator.py
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   └── 
│
│
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
└── requirements.txt
```
