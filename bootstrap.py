import os
import urllib.request

cwd = os.path.dirname(os.path.realpath(__file__))
url = 'https://raw.githubusercontent.com/jererc/svcutils/refs/heads/main/svcutils/bootstrap.py'
exec(urllib.request.urlopen(url).read().decode('utf-8'))
Bootstrap(
    name='test_svc',
    script_module='test_svc.main',
    script_args=['collect', '--path', cwd, '--task'],
    install_requires=[
        'test_svc @ https://github.com/jererc/test_svc/archive/refs/heads/main.zip',
    ],
    force_reinstall=True,
    schedule_mins=1,
).run()
