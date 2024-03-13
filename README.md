# arcad-demo-yum
Arcad demo yum package source

Skeleton rpm/yum package source demonstrating packaging/installation of host IBM i library objects.

For whatever reason, the rpm directory structure *must* be in `~/rpmbuild` (e.g. `/home/ACLARK/rpmbuild`) so you must copy the directory there if needed:
```fortran
cp -r ~/git/arcad-demo-yum/rpmbuild ~/rpmbuild
```

Create self-extracting jar using  <a href='https://github.com/ThePrez/AppInstall-IBMi'>ThePrez/AppInstall-IBMi</a>:
```fortran
cd ~/rpmbuild
mkdir SOURCES/arcad-demo-1.0.0
java -jar appinstall-ibmi-0.0.1-jar-with-dependencies.jar -o SOURCES/arcad-demo-1.0.0/arcad-demo.jar --qsys ARCAD_DEMO
```
> **_NOTE:_**  The 'SOURCES/arcad-demo-1.0.0/arcad-demo.ja'r file already exists in this sample repo in case you don't have either 'appinstall-ibmi-xxx.jar' or the 'ARCAD_DEMO' library already on your system - just proceed to the next step.

Create tar.gz from zip
```fortran
cd SOURCES
tar --create --file arcad-demo-1.0.0.tar.gz arcad-demo-1.0.0
```

Do binary rpm build
```fortran
cd ~/rpmbuild
rpmbuild -bb SPECS/arcad-demo.spec
```

Should see message indicating where rpm is written
```fortran
Wrote: /home/ACLARK/rpmbuild/RPMS/ppc64/arcad-demo-1.0.0-1.ibmi7.4.ppc64.rpm
```

Install from rpm
```fortran
yum install /home/ACLARK/rpmbuild/RPMS/ppc64/arcad-demo-1.0.0-1.ibmi7.4.ppc64.rpm
```


See:
<p/>
https://www.redhat.com/sysadmin/create-rpm-package
<p/>
https://github.com/kadler/rpm-lab



