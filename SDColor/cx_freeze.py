import sys
from cx_Freeze import setup, Executable

path_platforms = ("C:/Python34/Lib/site-packages/PyQt5/plugins/platforms/qwindows.dll", "platforms/qwindows.dll")
path_icon = "C:/Users/Shane DiNozzo/PycharmProjects/sdcolor/SDColor/pencils.ico"
path_ui = "C:/Users/Shane DiNozzo/PycharmProjects/sdcolor/SDColor/sdcolor.ui"
path_res = "C:/Users/Shane DiNozzo/PycharmProjects/sdcolor/SDColor/res.qrc"
path_res_rc_py = "C:/Users/Shane DiNozzo/PycharmProjects/sdcolor/SDColor/res_rc.py"

includes = ["PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets", "PyQt5.uic"]
includefiles = [path_platforms, path_icon, path_ui, path_res, path_res_rc_py]
excludes = []
packages = ["sys"]
path = []

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "includes": includes,
    "include_files": includefiles,
    "excludes": excludes,
    "packages": packages,
    "path": path
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
exe = None
if sys.platform == "win32":
    exe = Executable(
        script="C:/Users/Shane DiNozzo/PycharmProjects/sdcolor/SDColor/sdcolor.py",
        initScript=None,
        base="Win32GUI",
        targetName="SDColor.exe",
        compress=True,
        copyDependentFiles=True,
        appendScriptToExe=False,
        appendScriptToLibrary=False,
        icon=path_icon
    )

setup(
    name="SD Color",
    version="1.0",
    author='Shane DiNozzo',
    description="A very little app written in Python 3.4/PyQt5 using PyCharm to select colors from a color picker",
    options={"build_exe": build_exe_options},
    executables=[exe]
)