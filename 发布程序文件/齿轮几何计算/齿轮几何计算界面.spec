# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import (
    collect_data_files, collect_entry_point, collect_submodules
)

data, hiddenimports = collect_entry_point("pyface.toolkits")
data += collect_data_files("pyface")
hiddenimports += collect_submodules("pyface")


from PyInstaller.utils.hooks import (
    collect_data_files, collect_entry_point, collect_submodules
)

data, hiddenimports = collect_entry_point("traitsui.toolkits")
data += collect_data_files("traitsui")
hiddenimports += collect_submodules("traitsui")

block_cipher = None
packages_path = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python38\Lib\site-packages'

auto_imports = []
crawl_path = os.path.abspath(os.path.join(packages_path, 'pyface', 'ui', 'qt'))
for file in os.listdir(crawl_path):
    file_path = os.path.join(crawl_path, file)
    if file not in {'__pycache__', '__init__.py'} and (
            os.path.isdir(file_path) or (os.path.isfile(file_path) and file_path.endswith('.py'))):
        auto_imports.append('pyface.ui.qt.%s' % file.replace('.py', ''))


a = Analysis(['E:\\mechanical-calculation-4\\程序文件\\齿轮几何计算\\齿轮几何计算界面.py'],
             pathex=['C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\traitsui-7.4.2.dist-info', 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\pyface-8.0.0.dist-info'],
             binaries=[],
             datas=[('%s/pyface-8.0.0.dist-info' % packages_path, 'pyface-8.0.0.dist-info'),
                    ('%s/traitsui-7.4.2.dist-info' % packages_path, 'traitsui-7.4.2.dist-info'),
                   ],
             hiddenimports=['pandas', 'mpl_toolkits.axes_grid1', 'mpl_toolkits.axisartist', 'sympy', 'geatpy', 'xlwings', 'traits', 'tornado', 'traits.api', 'Pyface', 'traitsui',
             'importlib_metadata',
            'importlib_resources',
            'numpy',
            'pyface',
            'pyface.toolkit',
            'pyface.ui.qt',
            'pyface.ui.qt.action',
            'pyface.ui.qt.clipboard',
            'pyface.ui.qt.code_editor',
            'pyface.ui.qt.console',
            'pyface.ui.qt.data_view',
            'pyface.ui.qt.fields',
            'pyface.ui.qt.images',
            'pyface.ui.qt.init',
            'pyface.ui.qt.tasks',
            'pyface.ui.qt.tests',
            'pyface.ui.qt.timer',
            'pyface.ui.qt.util',
            'pyface.ui.qt.wizard',
            'pyface.ui.qt.workbench',
            'pywin32_system32',
            'pywintypes',
            'scipy',
            'traitsui',
            'traitsui.qt4',
            'traitsui.qt4.extra',
            'traitsui.qt4.toolkit',
            'traitsui.toolkit',
            'traitsui.ui_traits',],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='齿轮几何计算界面',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , uac_admin=True)
def collect_imports(path, prefix):
    hiddenimports.append(prefix)
    for file in os.listdir(path):
        if file in {'__pycache__', '__init__.py', 'tests'}:
            continue
        child = f'{prefix}.{file}'
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            collect_imports(file_path, child)
        elif os.path.isfile(file_path) and file.endswith('.py'):
            hiddenimports.append(child[0:-len('.py')])

collect_imports(os.path.join(packages_path, 'pyface', 'ui', 'qt'), 'pyface.ui.qt')
collect_imports(os.path.join(packages_path, 'traitsui', 'qt4'), 'traitsui.qt4')
coll = COLLECT(exe,
a.binaries,
a.zipfiles,
a.datas,
strip=False,
upx=True,
upx_exclude=[],
name='齿轮几何计算界面')
