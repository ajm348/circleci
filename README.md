Based on https://github.com/CircleCI-Public/circleci-demo-python-flask and https://riptutorial.com/python/example/8570/start-simple-httpserver-in-a-thread-and-open-the-browser

Recommended steps for running:

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
# download chromedriver https://chromedriver.chromium.org/getting-started and add it to your path,
# for example by moving it into ./venv/bin
python test.py
```

Configured to run tests on CircleCI.