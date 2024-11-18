import os
import urllib.request

cwd = os.path.join(os.path.dirname(__file__))
url = 'https://raw.githubusercontent.com/jererc/svcutils/refs/heads/main/svcutils/bootstrap.py'
exec(urllib.request.urlopen(url).read().decode('utf-8'))

Bootstrap(
    script_name='testsvc',
    script_args=[],
    install_requires=[
        # 'git+https://github.com/jererc/itemz.git',
        'testsvc @ https://github.com/jererc/testsvc/archive/refs/heads/main.zip',
    ],
    force_reinstall=True,
).run()
