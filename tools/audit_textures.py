#!/usr/bin/env python3
import struct, sys
from pathlib import Path
LIMIT=2048

def png_size(path: Path):
    data=path.read_bytes()[:24]
    if data[:8]!=b'\x89PNG\r\n\x1a\n': return None
    return struct.unpack('>II',data[16:24])

def main(argv=None):
    root=Path((argv or sys.argv[1:] or ['.'])[0])
    failures=[]; checked=0
    for p in root.rglob('*.png'):
        size=png_size(p)
        if not size: continue
        checked+=1
        if max(size)>LIMIT: failures.append((p,*size))
    for p,w,h in failures: print(f'OVERSIZE {w}x{h} {p}')
    print(f'Checked {checked} PNG textures; oversize={len(failures)}')
    return 1 if failures else 0
if __name__=='__main__': raise SystemExit(main())
