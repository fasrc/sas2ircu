Name:		sas2ircu
Version:	5.0
Release:	2%{?dist}
Summary:	LSI Corporation SAS2 IR Configuration Utility
License:	Unknown
URL:		http://www.lsi.com/downloads/Public/Host%20Bus%20Adapters/Host%20Bus%20Adapters%20Common%20Files/SAS_SATA_6G_P12/SAS2IRCU_User_Guide.pdf
Source0:	http://www.supermicro.com/support/faqs/data_lib/FAQ_9633_SAS2IRCU_Phase_5.0-5.00.00.00.zip
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
LSI Corporation SAS2 IR Configuration Utility

%prep
rm -rf %{_builddir}/%{name}-%{version}
mkdir -p %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
unzip %{SOURCE0}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
cp %{_builddir}/%{name}-%{version}/sas2ircu_linux_x86_rel/sas2ircu %{buildroot}/%{_sbindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%attr(0755,root,root) %{_sbindir}/sas2ircu

%changelog
* Wed Jul 25 2012 Harvard University FAS Research Computing <rchelp@fas.harvard.edu> - 0.2-1
- use %{_sbindir}

* Fri Jul 20 2012 Harvard University FAS Research Computing <rchelp@fas.harvard.edu> - 0.1-1
- Initial package
