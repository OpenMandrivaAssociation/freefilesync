# Spec is baed on Alberto Altieri's work in MIB

%define		oname FreeFileSync

Name:		freefilesync
Version:	5.0
Release:	%mkrel 1
Summary:	A free file sync tool
Group:		Networking/File transfer
License:	GPLv3
Url:		http://sourceforge.net/projects/freefilesync/
Source:		%{oname}_v%{version}_source.zip
Source1:	%{oname}.desktop
BuildRequires:	gtkmm2.4-devel
BuildRequires:	wxgtku2.8-devel >= 2.8.11
BuildRequires:	boost-devel >= 1.42.0

%description
FreeFileSync is a folder comparison and synchronization tool.

%prep
%setup -q -c %{name}-%{version}

%build
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
%__install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{oname}.desktop
%__sed -i 's/\r//' BUILD/Changelog.txt
%__sed -i 's/\r//' BUILD/License.txt

%__rm -rf %{buildroot}%{_docdir}/%{oname}

%clean
%__rm -rf %{buildroot}

%files
%doc BUILD/Changelog.txt BUILD/License.txt
%{_bindir}/%{oname}
%dir %{_datadir}/%{oname}
%{_datadir}/%{oname}/*
%{_datadir}/applications/%{oname}.desktop
