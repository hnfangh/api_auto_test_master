import os
import pytest


if __name__ == "__main__":
    mark = "smoke" # todo [smoke:冒烟、regress：回归] 执行时只执行带有特定标记case
    pytest.main(["-v", "-s", "./testcases/regress/", "--alluredir=./reports/allure-results", "--clean-alluredir"])
    os.system("allure generate ./reports/allure-results -o ./reports/allure-report  --clean")