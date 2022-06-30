from struct import pack
from setuptools import find_packages, setup

setup(
    name ='VOLT',
    version='0.1.0',
    description='An efficient token vocabulary construction method',
    url ='https://github.com/Jingjing-NLP/VOLT',
    author='Jingjing Xu',
    author_email='jingjingxu@pku.edu.cn',
    packages=find_packages(),
    install_requires=['tqdm','subword-nmt','POT'],
    
    classifiers=[
       'Development Status :: 1 - Planning',
       'Intended Audience :: Developers',
       'Programming Language :: Python :: 3'
       'Topic :: Artificial Intelligence :: Machine Translation :: Optimal Transport'
    ],
    include_package_data=True
)