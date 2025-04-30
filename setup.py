
import platform
from setuptools import find_packages, setup

setup(
    name="delta-tts",
    version="0.0.1",
    author="BrokenHypocrite",
    author_email="brokenhypocrite@gmail.com",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    description="Controllable and Efficient Zero-Shot Text-To-Speech System based on IndexTTS",
    url="https://github.com/Delta-Zero-Games/delta-tts",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "torch>=2.1.2",
        "torchaudio",
        "transformers==4.36.2",
        "accelerate",
        "tokenizers==0.15.0",
        "einops==0.8.1",
        "matplotlib==3.8.2",
        "omegaconf",
        "sentencepiece",
        "librosa",
        "numpy",
        "wetext" if platform.system() == "Darwin" else "WeTextProcessing",
    ],
    entry_points={
        "console_scripts": [
            "dzptts = dzptts.cli:main",
        ]
    },
    license="DELTA-TTS License",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: Other/Proprietary License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)