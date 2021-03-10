import shutil, json
from engine.metadata import metadata_db
from engine.helpers import write_file

mdb = metadata_db('audio/simpleCall/metadata.json')
valid_labels = ['B2', 'B3', 'B4', 'VS', 'VSV', 'UPS']

newMdb = dict()
for stem in mdb.db:
    # This file is manipulated/filtered too much
    if stem == 'B3_C_B_Jt1_16_07_06_042':
        continue

    entry = mdb.db[stem].props
    del entry['audio']

    if all([label['sequence'] in valid_labels for label in entry['labels']]) and len(entry['labels']):
        newMdb[stem] = entry
        shutil.copy(f'../audio/simpleCall/{stem}.wav', f'audio/{stem}.wav')
    else:
        print(stem)
        print(entry['labels'])

print(f'file count: {len(newMdb)}')
write_file(f"metadata.json", json.dumps(newMdb, indent=2))
