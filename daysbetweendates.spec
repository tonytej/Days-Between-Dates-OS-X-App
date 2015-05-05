# -*- mode: python -*-
a = Analysis(['daysbetweendates.py'],
             pathex=['/Users/Tony'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DaysBetweenDates',
          debug=False,
          strip=None,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='DaysBetweenDates.app',
             icon=None)
