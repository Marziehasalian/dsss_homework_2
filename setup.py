from setuptools import setup
setup(
    name='dsss_homework_2',
    version='0',
    packages=['math_quiz'],
    install_requires=[],
    entry_points={
'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',
        ],
    },
)
