%global srcname ansible_pacemaker

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-pacemaker
Version:        0.1
Release:        1%{?dist}
Summary:        Ansible modules for managing Pacemaker clusters

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/redhat-openstack/ansible-pacemaker/README.md
Source0:        https://github.com/redhat-openstack/ansible-pacemaker/archive/master.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python-pbr

Requires: ansible

%description

Ansible-pacemaker is a set of Ansible modules for a Pacemaker cluster, nodes
and resources.

%prep
%setup -q -n %{name}-%{upstream_version}


%build
%{__python2} setup.py build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc README*
%license LICENSE
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
/usr/share/ansible-modules/


%changelog
