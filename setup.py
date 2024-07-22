from setuptools import setup, find_packages

setup(
    name='app-plopez',                # Nombre del paquete
    version='1.3.0',              # Versión del paquete
    description='A brief description of the project',  # Descripción del paquete
    author='ploopez',           # Nombre del autor
    author_email='plopez@stemdo.io',  # Email del autor
    url='https://github.com/yourusername/my_app',  # URL del proyecto
    packages=find_packages(),      # Encuentra automáticamente los paquetes en el directorio
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',       # Versión mínima de Python requerida
    install_requires=[
        'requests>=2.25.1',        # Dependencias del proyecto
    ],
    extras_require={
        'dev': ['pytest>=3.7'],    # Dependencias adicionales para desarrollo
    },
)
