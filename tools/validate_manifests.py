#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED={
'ASSET_MASTER_MANIFEST.csv':['asset_id','name','category','subcategory','district_usage','source_type','source','creator','license','license_url','source_url','source_revision','download_date','archive_sha256','original_format','processed_format','game_path','triangle_count','lod_count','material_count','max_texture_resolution','collision_type','android_test_status','integration_status','notes'],
'ASSET_GENERATION_QUEUE.csv':['priority','asset_id','asset_name','category','required_output','generation_method','dependencies','assigned_status','review_status','android_status','blocker'],
'WORLD_DISTRICT_ASSET_MATRIX.csv':['asset_id','manama','bahrain_bay','seef','juffair','adliya','muharraq','isa_town','riffa','saar','budaiya','zallaq','desert','coast','industrial'],
'ASSET_ACCEPTANCE_REPORT.csv':['asset_id','license_pass','style_pass','scale_pass','material_pass','texture_pass','collision_pass','lod_pass','godot_import_pass','android_pass','approved','rejection_reason']}

def main():
    errors=[]
    ids=set()
    for filename,headers in REQUIRED.items():
        path=ROOT/'docs/assets'/filename
        if not path.is_file(): errors.append(f'missing {path}'); continue
        with path.open(newline='',encoding='utf-8') as f:
            reader=csv.DictReader(f)
            if reader.fieldnames!=headers: errors.append(f'{filename}: header mismatch')
            rows=list(reader)
        if not rows: errors.append(f'{filename}: empty')
        if filename=='ASSET_MASTER_MANIFEST.csv':
            for row in rows:
                aid=row['asset_id']
                if aid in ids: errors.append(f'duplicate asset_id {aid}')
                ids.add(aid)
                if row['source_type']=='inherited_unverified' and row['integration_status']!='quarantined': errors.append(f'{aid}: inherited asset not quarantined')
    status=json.loads((ROOT/'docs/assets/ASSET_STATUS.json').read_text(encoding='utf-8'))
    if status.get('source_repository_mutated') is not False: errors.append('source mutation flag must be false')
    if errors:
        print('\n'.join(errors)); return 1
    print(f'Manifest validation passed: {len(ids)} master assets')
    return 0
if __name__=='__main__': raise SystemExit(main())
