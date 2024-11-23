# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:\\mechanical-calculation-4\\参考测试程序\\beamCalculator\\Ui\\beam_calculator_main_window.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['matplotlib.backends.backend_tkagg', 'sympy', 'sympy.physics.continuum_mechanics', 'symbeam'],
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
          name='beam_calculator_main_window',
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
          entitlements_file=None )
