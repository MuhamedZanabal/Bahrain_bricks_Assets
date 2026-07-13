#!/usr/bin/env python3
import re, sys
from pathlib import Path
PATTERN = re.compile(r'^(bh_[a-z0-9]+(?:_[a-z0-9]+)*)$')

def valid_asset_id(value: str) -> bool:
    return bool(PATTERN.fullmatch(value)) and '--' not in value

def main(argv=None):
    argv = argv or sys.argv[1:]
    bad=[x for x in argv if not valid_asset_id(x)]
    if bad:
        print('Invalid asset IDs:', *bad, sep='\n- ')
        return 1
    print(f'Naming validation passed: {len(argv)} IDs')
    return 0
if __name__=='__main__': raise SystemExit(main())
