from pathlib import Path, PurePosixPath
import hashlib, json, stat, zipfile
archive=Path('site.zip');out=Path('_site')
with zipfile.ZipFile(archive) as z:
    names=z.namelist()
    assert len(names)==len(set(names)), 'Duplicate archive paths'
    for info in z.infolist():
        path=PurePosixPath(info.filename)
        assert not path.is_absolute() and '..' not in path.parts
        assert '.git' not in path.parts and not path.name.startswith('.env')
        assert stat.S_IFMT(info.external_attr>>16)!=stat.S_IFLNK
        assert path.name!='Juewen_Chen_Product_GTM_Resume.pdf'
    manifest=json.loads(z.read('public_release.json'))
    assert set(names)==set(manifest['files'])|{'public_release.json'}
    for name,record in manifest['files'].items():
        content=z.read(name)
        assert len(content)==record['bytes'], name
        assert hashlib.sha256(content).hexdigest()==record['sha256'], name
    assert {'index.html','resources/evidence.html','resources/resume/Juewen_Chen_GearLab_Public_Resume.pdf'}<=set(names)
    assert z.read('resources/resume/Juewen_Chen_GearLab_Public_Resume.pdf').startswith(b'%PDF')
    out.mkdir(exist_ok=True)
    z.extractall(out)
print('Verified public release:',len(names),'files. Original private résumé excluded.')
