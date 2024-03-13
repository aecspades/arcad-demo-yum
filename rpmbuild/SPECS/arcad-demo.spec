Name:           arcad-demo
Version:        1.0.0
Release:        3
Summary:        Arcad demo (ARCAD_DEMO) library

License:        GPL
Source0:        %{name}-%{version}.tar.gz

#Requires:       java >= 8

%description
Arcad demo (ARCAD_DEMO) library

%prep
%setup

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}
cp %{name}.jar $RPM_BUILD_ROOT/%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
java -jar %{_sysconfdir}/%{name}.jar -c

%files
%attr(-, qsys, *none) %{_sysconfdir}/%{name}.jar

%changelog
* Tue Mar 12 2024 Andrew Clark <aecspades@gmail.com>
- 1.0.0-3
- Initial version