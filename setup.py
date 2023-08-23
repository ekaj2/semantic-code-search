import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='semantic-code-search',
    version='0.4.1',
    author='Kiril Videlov',
    author_email='kiril@codeball.ai',
    description='Search your codebase with natural language.',
    install_requires=[
                'numpy',
                'prompt_toolkit',
                'Pygments',
                'sentence_transformers',
                'setuptools',
                'torch',
                'tree_sitter',
                'tree_sitter_builds',
                'tree_sitter_languages',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    url='https://github.com/sturdy-dev/semantic-code-search',
    package_dir={
        "semantic_code_search": "src/semantic_code_search"
    },
    entry_points={
        'console_scripts': [
            'sem=semantic_code_search.cli:main',
        ]
    },
    keywords='semantic code search',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ]
)
