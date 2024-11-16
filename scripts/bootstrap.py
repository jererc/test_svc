import os
import urllib.request

url = 'https://raw.githubusercontent.com/jererc/svcutils/refs/heads/main/svcutils/bootstrap.py'
response = urllib.request.urlopen(url)
code = response.read().decode('utf-8')
exec(code)
Bootstrapper(
    name='test_svc',
    script_path=os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'run.py'),
    requires=[
        # 'https://github.com/jererc/test_svc/archive/refs/heads/main.zip',
        'git+https://github.com/jererc/test_svc.git',
    ],
).run()
