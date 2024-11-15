import ctypes
import os
import subprocess


class Bootstrapper:
    def __init__(self, script_path, requirements_file=None, venv_dir='venv',
                 task_schedule_mins=2,
                 linux_args=None, windows_args=None):
        self.script_path = os.path.realpath(script_path)
        self.requirements_file = requirements_file or os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
        self.venv_dir = venv_dir
        self.task_schedule_mins = task_schedule_mins
        self.linux_args = linux_args
        self.windows_args = windows_args
        self.script_name = os.path.splitext(os.path.basename(
            self.script_path))[0]
        self.root_venv_path = os.path.join(os.path.expanduser('~'),
            self.venv_dir)
        self.venv_path = os.path.join(self.root_venv_path, self.script_name)
        self.pip_path = {
            'nt': os.path.join(self.venv_path, r'Scripts\pip.exe'),
            'posix': os.path.join(self.venv_path, 'bin/pip'),
        }[os.name]
        self.svc_py_path = {
            'nt': os.path.join(self.venv_path, r'Scripts\pythonw.exe'),
            'posix': os.path.join(self.venv_path, 'bin/python'),
        }[os.name]

    def _setup_venv(self):
        if not os.path.exists(self.root_venv_path):
            os.makedirs(self.root_venv_path)
        if not os.path.exists(self.svc_py_path):
            if os.name == 'nt':   # requires python3-virtualenv on linux
                subprocess.check_call(['pip', 'install', 'virtualenv'])
            subprocess.check_call(['virtualenv', self.venv_path])
        subprocess.check_call([self.pip_path, 'install', '-r',
            self.requirements_file])
        print(f'Created the virtualenv in {self.venv_path}')

    def _get_crontab_schedule(self):
        if 1 < self.task_schedule_mins < 60:
            return f'*/{self.task_schedule_mins} * * * *'
        return '* * * * *'

    def _setup_linux_task(self, cmd):
        res = subprocess.run(['crontab', '-l'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        current_crontab = res.stdout if res.returncode == 0 else ''
        new_job = f'{self._get_crontab_schedule()} {cmd}\n'
        updated_crontab = ''
        job_found = False
        for line in current_crontab.splitlines():
            if cmd in line:
                updated_crontab += new_job
                job_found = True
            else:
                updated_crontab += f'{line}\n'
        if not job_found:
            updated_crontab += new_job
        res = subprocess.run(['crontab', '-'], input=updated_crontab,
            text=True)
        if res.returncode != 0:
            raise SystemExit('Failed to update crontab')
        print('Successfully updated crontab')

    # def _setup_windows_task_onlogon(self, cmd, task_name):
    #     if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    #         raise SystemExit('Failed: must run as admin')
    #     subprocess.check_call(['schtasks', '/create',
    #         '/tn', task_name,
    #         '/tr', cmd,
    #         '/sc', 'onlogon',
    #         '/rl', 'highest',
    #         '/f',
    #     ])
    #     subprocess.check_call(['schtasks', '/run',
    #         '/tn', task_name,
    #     ])

    def _setup_windows_task(self, cmd, task_name):
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            raise SystemExit('Failed: must run as admin')
        subprocess.check_call(['schtasks', '/create',
            '/tn', task_name,
            '/tr', cmd,
            '/sc', 'minute',
            '/mo', str(self.task_schedule_mins),
            '/rl', 'highest',
            '/f',
        ])
        subprocess.check_call(['schtasks', '/run',
            '/tn', task_name,
        ])

    def _get_cmd(self, args):
        args = f' {" ".join(args)}' if args else ''
        return f'{self.svc_py_path} {self.script_path}{args}'

    def run(self):
        self._setup_venv()
        if os.name == 'nt':
            self._setup_windows_task(cmd=self._get_cmd(self.windows_args),
                task_name=self.script_name)
        else:
            self._setup_linux_task(cmd=self._get_cmd(self.linux_args))


Bootstrapper(
    script_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),
        'test_svc.py'),
).run()
