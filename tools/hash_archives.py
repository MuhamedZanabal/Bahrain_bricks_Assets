#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def main(argv=None):
    files=[Path(x) for x in (argv or sys.argv[1:])]
    records=[]
    for path in files:
        if not path.is_file(): raise SystemExit(f'not a file: {path}')
        records.append({'path':str(path),'size_bytes':path.stat().st_size,'sha256':sha256(path)})
    print(json.dumps(records,indent=2))
if __name__=='__main__': main()
