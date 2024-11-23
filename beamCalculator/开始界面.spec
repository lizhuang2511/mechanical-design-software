# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:\\mechanical-calculation-4\\程序文件\\开始界面\\开始界面.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['pandas', 'mpl_toolkits.axes_grid1', 'mpl_toolkits.axisartist', 'sympy', 'geatpy', 'xlwings', 'traits', 'traits.api', 'traitsui.toolkits'],
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
          [],
          exclude_binaries=True,
          name='开始界面',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=False,
               upx_exclude=[],
               name='开始界面')
