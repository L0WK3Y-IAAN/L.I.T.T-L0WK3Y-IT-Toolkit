# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['L.I.T.T  by @L0WK3Y_IAANSEC.py'],
             pathex=['/home/l0wk3yiaan/Documents/self-made-projects/python/L.I.T.T  by @L0WK3Y_IAANSEC'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          name='L.I.T.T  by @L0WK3Y_IAANSEC',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
