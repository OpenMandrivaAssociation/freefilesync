# Spec is baed on Alberto Altieri's work in MIB

%define		oname FreeFileSync

Name:		freefilesync
Version:	11.16
Release:	1
Summary:	A free file sync tool
Group:		Networking/File transfer
License:	GPLv3
Url:		http://sourceforge.net/projects/freefilesync/
Source0:  https://freefilesync.org/download/FreeFileSync_%{version}_Source.zip
#Source0:	http://ignum.dl.sourceforge.net/project/freefilesync/freefilesync/v%{version}/%{oname}_%{version}_source.zip
Source1:	%{oname}.desktop
BuildRequires:  imagemagick
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  wxgtk3.1-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssh2)

%description
FreeFileSync is a folder comparison and synchronization tool.

%prep
%setup -q -c %{name}-%{version}

%build
# FFS
%make_build -C \
	FreeFileSync/Source \
	EXENAME=FreeFileSync

# RTS
%make_build -C \
	FreeFileSync/Source/RealTimeSync \
	EXENAME=RealTimeSync
%install
%makeinstall_std
%__install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{oname}.desktop
%__sed -i 's/\r//' BUILD/Changelog.txt
%__sed -i 's/\r//' BUILD/License.txt

%__rm -rf %{buildroot}%{_docdir}/%{oname}

%files
%doc BUILD/Changelog.txt BUILD/License.txt
%{_bindir}/%{oname}
%dir %{_datadir}/%{oname}
%{_datadir}/%{oname}/*
%{_datadir}/applications/%{oname}.desktop
