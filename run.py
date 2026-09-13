import pytest
import os


if __name__ == "__main__":
    os.system("pytest")
    os.system("allure generate reports/allure-results -o reports/allure-report --clean")