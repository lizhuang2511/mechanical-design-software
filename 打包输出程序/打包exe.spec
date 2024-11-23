# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:\mechanical-calculation-4\程序文件\开始界面\开始界面.py'],
             pathex=[],
             binaries=[('traitsui', 'traitsui'),('traitsui-7.4.3.dist-info','traitsui-7.4.3.dist-info'),
             ('pyface', 'pyface'),('pyface-7.4.4.dist-info','pyface-7.4.4.dist-info'),
             ('wx','wx'),('wxPython-4.1.0.dist-info','wxPython-4.1.0.dist-info'),
             ('traits','traits'),('traits-6.4.1.dist-info','traits-6.4.1.dist-info'),
             ('numpy','numpy'), ('numpy-1.23.5.dist-info','numpy-1.23.5.dist-info'),
             ('PySide2', 'PySide2'),('PySide2-5.15.2.1.dist-info', 'PySide2-5.15.2.1.dist-info')],
             datas=[],
             hiddenimports=[],
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
          name='皮带计算ui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , uac_admin=True)
coll=COLLECT(exe)

