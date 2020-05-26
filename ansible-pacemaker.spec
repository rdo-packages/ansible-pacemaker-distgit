%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name ansible-pacemaker
%global commit 58471675775bc776399c88438d33158964ba36d2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%global srcname ansible_pacemaker


Name:           ansible-pacemaker
Version:        1.0.3
Release:        2%{?alphatag}%{?dist}
Summary:        Ansible modules for managing Pacemaker clusters

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/redhat-openstack/ansible-pacemaker
Source0:        https://github.com/redhat-openstack/ansible-pacemaker/archive/%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires: ansible
Requires: python3-lxml

%description

Ansible-pacemaker is a set of Ansible modules for a Pacemaker cluster, nodes
and resources.

%prep
%autosetup -n %{name}-%{upstream_version} -S git


%build
%py3_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py3_install


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info
%{_datadir}/ansible/


%changelog
* Tue May 26 2020 Alfredo Moralejo <amoralej@redhat.com> - 1.0.3-2.58471675git
- Update to post-1.0.3 commit (58471675775bc776399c88438d33158964ba36d2)
