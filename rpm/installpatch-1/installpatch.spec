Name:	installpatch		
Version:	1	
Release:	1
Summary:	install patch	

Group:	System	
License:	GPL	
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL:http://bjjhl.cn		
Source0: %{name}-%{version}.tar.gz	

Requires: initscripts

%description
install patch

%prep
%setup -q


%build


%install
mkdir -p %{buildroot}/usr/share/installpatch
cp install.sh %{buildroot}/usr/share/installpatch/ -a
cp *.rpm %{buildroot}/usr/share/installpatch/

%files
%doc
/usr/share/installpatch
%post
echo '/usr/share/installpatch/install.sh' >> /etc/rc.local
%postun
sed -i '/\/usr\/share\/installpatch\/install.sh/d' /etc/rc.local

%changelog

