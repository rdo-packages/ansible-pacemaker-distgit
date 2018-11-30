# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pydefault 3
%else
%global pydefault 2
%endif

%global pydefault_bin python%{pydefault}
%global pydefault_sitelib %python%{pydefault}_sitelib
%global pydefault_install %py%{pydefault}_install
%global pydefault_build %py%{pydefault}_build
# End of macros for py2/py3 compatibility

%global srcname ansible_pacemaker

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-pacemaker
Version:        XXX
Release:        XXX
Summary:        Ansible modules for managing Pacemaker clusters

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/redhat-openstack/ansible-pacemaker
Source0:        https://github.com/redhat-openstack/ansible-pacemaker/archive/%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pydefault}-devel
BuildRequires:  python%{pydefault}-setuptools
BuildRequires:  python%{pydefault}-pbr
%if %{pydefault} == 2
BuildRequires: python-d2to1
%else
BuildRequires: python%{pydefault}-d2to1
%endif

%if %{pydefault} == 2
Requires: ansible
Requires: python-lxml
%else
Requires: ansible-python3
Requires: python%{pydefault}-lxml
%endif

%description

Ansible-pacemaker is a set of Ansible modules for a Pacemaker cluster, nodes
and resources.

%prep
%autosetup -n %{name}-%{upstream_version} -S git


%build
%pydefault_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%pydefault_install


%files
%doc README*
%license LICENSE
%{pydefault_sitelib}/%{srcname}-%{version}-*.egg-info
%{_datadir}/ansible-modules/


%changelog
