# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver 3
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
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
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

%if %{pyver} == 2
Requires: ansible
Requires: python-lxml
%else
%if 0%{?rhel} > 7
Requires: ansible
%else
Requires: ansible-python3
%endif
Requires: python%{pyver}-lxml
%endif

%description

Ansible-pacemaker is a set of Ansible modules for a Pacemaker cluster, nodes
and resources.

%prep
%autosetup -n %{name}-%{upstream_version} -S git


%build
%pyver_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%pyver_install


%files
%doc README*
%license LICENSE
%{pyver_sitelib}/%{srcname}-%{version}-*.egg-info
%{_datadir}/ansible-modules/


%changelog
