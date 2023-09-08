from setuptools import setup
from setuptools.discovery import PackageFinder

with open('requirements.txt') as f:
    requirements = f.readlines()

packages_basicsr_exclude = ('options', 'datasets', 'experiments', 'results', 'tb_logger', 'wandb')

packages_basicsr = ['basicsr'] + [
    f"basicsr.{name}"
    for name in PackageFinder.find(where='basicsr', exclude=packages_basicsr_exclude)
]

packages_facelib = ['facelib'] + [
    f"facelib.{name}"
    for name in PackageFinder.find(where='facelib')
]

packages = ['CodeFormer'] + packages_basicsr + packages_facelib + ['facelib.detection.retinaface']
setup(
    name='CodeFormer',
    version='0.1',
    zip_safe=False,
    install_requires=requirements,
    packages=packages,
    package_dir={
        'CodeFormer': '.',
    },
    # include_package_data=True,
    # package_data={
    #     'basicsr': ['basicsr', 'basicsr/*', 'basicsr/*/*'],
    #     'facelib': ['facelib', 'facelib/*', 'facelib/*/*'],
    # },
)
