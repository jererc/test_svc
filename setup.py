from setuptools import setup, find_packages

setup(
    name='test_svc',
    version='0.1.0',
    author='jererc',
    author_email='jererc@gmail.com',
    url='https://github.com/jererc/test_svc',
    packages=find_packages(exclude=['tests*']),
    python_requires='>=3.10',
    # entry_points={
    #     'console_scripts': [
    #         'test_svc=test_svc.test_svc:run',
    #     ],
    # },
    install_requires=[
        'svcutils @ git+https://github.com/jererc/svcutils.git@main#egg=svcutils',
        'webutils @ git+https://github.com/jererc/webutils.git@main#egg=webutils',
    ],
    extras_require={
        'dev': ['pytest', 'flake8'],
    },
    include_package_data=True,
)