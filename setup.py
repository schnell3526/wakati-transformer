from setuptools import find_packages, setup

setup(
    name='wakaformer',
    packages=find_packages(include=['wakaformer']),
    version='0.1.0',
    description='Japanese simple word separater with BERT',
    author='schnell',
    license='MIT',
    install_requires=["transformers", "torch==1.11.0", "fugashi", "ipadic", "wheel"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)