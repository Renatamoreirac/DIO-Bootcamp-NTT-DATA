from setuptools import setup, find_packages

setup(
    name='imagemagic',  # Nome do pacote
    version='0.1',  # Versão do pacote
    packages=find_packages(),  # Encontra automaticamente os pacotes
    install_requires=[  # Dependências do pacote
        'Pillow',  # Biblioteca de processamento de imagens
    ],
    description='Um pacote simples para processamento de imagens.',  # Descrição do pacote
    long_description=open('README.md').read(),  # Conteúdo do README
    long_description_content_type='text/markdown',  # Tipo do conteúdo do README
    author='Seu Nome',  # Seu nome
    author_email='seu_email@example.com',  # Seu email
    url='https://github.com/seu_usuario/imagemagic',  # URL do repositório
    classifiers=[  # Classificadores para o PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Requisito de versão do Python
)
