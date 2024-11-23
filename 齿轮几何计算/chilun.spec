# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
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

a = Analysis(['E:\\mechanical-calculation-4\\程序文件\\齿轮几何计算\\chilun.py'],
             pathex=['C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\traitsui-7.4.2.dist-info', 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\pyface-8.0.0.dist-info'],
             binaries=[],
             datas=[],
             hiddenimports=['pandas', 'mpl_toolkits.axes_grid1', 'mpl_toolkits.axisartist', 'sympy', 'geatpy', 'xlwings', 'traits', 'tornado', 'traits.api', 'Pyface', 'traitsui'],
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
          name='chilun',
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
