# arcad-demo-yum
Arcad demo yum package source

Skeleton rpm/yum package source demonstrating packaging/installation of host IBM i library objects.

Create self-extracting jar using  <a href='https://github.com/ThePrez/AppInstall-IBMi'>ThePrez/AppInstall-IBMi</a>:
```fortran
cd rpmbuild
mkdir SOURCES/arcad-demo-1.0.0
java -jar appinstall-ibmi-0.0.1-jar-with-dependencies.jar -o SOURCES/arcad-demo-1.0.0/arcad-demo.jar --qsys ARCAD_DEMO
```

Create tar.gz from zip
```fortran
tar --create --file SOURCES/arcad-demo-1.0.0.tar.gz SOURCES/arcad-demo-1.0.0
```

Do binary rpm build
```fortran
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
https://www.redhat.com/sysadmin/create-rpm-package
https://github.com/kadler/rpm-lab



