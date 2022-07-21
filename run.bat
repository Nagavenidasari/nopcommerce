@ECHO OFF

pytest -v --capture=tee-sys -m"sanity"  --html=Reports\sanityreportchrome.html Testcases/ --browser chrome
pytest -v --capture=tee-sys -m"sanity"  --html=Reports\sanityreportfirefox.html Testcases/ --browser firefox



pytest -v --capture=tee-sys -m"regression"  --html=Reports\regressionreport.html Testcases/ --browser chrome


