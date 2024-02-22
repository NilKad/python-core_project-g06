# from setuptools import setup, find_packages

# setup(
#     name='python-core_project-g06',
#     version='0.1',
#     packages=find_packages(),
#     install_requires=[
#         'prompt_toolkit',
#         'autocomplete'
#     ],
#     entry_points={
#         'console_scripts': [
#             'python-core_project-g06=src.main:main',
#         ],
#     },
# )

from setuptools import setup, find_namespace_packages

setup(
    name='python-core_project-g06',
    version='0.1',
    description='CLI personal assistant',
    author='NilKad',
    author_email='aleksandrkadulin@gmail.com',
    url='https://github.com/NilKad/python-core_project-g06.git',
    packages=find_namespace_packages(),
    data_files=[('python-core_project-g06-main', [python-core_project-g06-main/cash.bin, python-core_project-g06-main/storage_contacts.bin, python-core_project-g06-main/cash.bin/storage_contacts_new.bin, python-core_project-g06-main/cash.bin/storage_notes.bin])]
    include_package_data=True,
    install_requires=[
        'prompt_toolkit',
        'autocomplete',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'start_cli=python-core_project-g06-main:main',
        ],
    },
)
