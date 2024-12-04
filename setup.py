import sys
from cx_Freeze import setup, Executable
from RandomizerCore.randomizer_data import VERSION

build_exe_options = {"packages": ["os"], 
                    "excludes": ["tkinter", "unittest", "sqlite3", "numpy", "matplotlib", "zstandard"],
                    "zip_include_packages": ["encodings", "PySide6"],
                    "include_files": ["RandomizerCore/Data", "RandomizerUI/Resources", "version.txt"],
                    "optimize": 2}

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    build_icon = "RandomizerUI/Resources/icon.ico"

    setup(
    name = "Links Awakening Switch Randomizer",
    version = f"{VERSION}",
    description = "A randomizer for The Legend of Zelda: Link's Awakening remake!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("randomizer.py", base=base, target_name="Links Awakening Switch Randomizer", icon=build_icon)]
)

elif sys.platform == "darwin":
    from py2app import setup as macsetup
    build_icon = "RandomizerUI/Resources/icon.icns"
    APP = ['randomizer.py']
    DATA_FILES = ['RandomizerUI/Resources/icon.icns']
    OPTIONS = {'argv_emulation': True}
    macsetup(
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app']
    )
