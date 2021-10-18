%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name ansible-pacemaker
%global commit 666f706b8fef8e59df690a59a838efb6eeec5815
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%global srcname ansible_pacemaker

Name:           ansible-pacemaker
Version:        1.0.4
Release:        2%{?alphatag}%{?dist}
Summary:        Ansible modules for managing Pacemaker clusters

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/redhat-openstack/ansible-pacemaker
Source0:        https://github.com/redhat-openstack/ansible-pacemaker/archive/%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires: (python3dist(ansible) or ansible-core >= 2.11)
Requires: python3-lxml

%description

Ansible-pacemaker is a set of Ansible modules for a Pacemaker cluster, nodes
and resources.

%prep
%autosetup -n %{name}-%{upstream_version} -S git
#Remove ansible from requirements.txt as dependency on ansible is managed manually
sed -i '/^ansible/d' requirements.txt

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
* Thu Apr 14 2022 Joel Capitao <jcapitao@redhat.com> - 1.0.4-2.666f706bgit
- Update to post-1.0.4 commit (666f706b8fef8e59df690a59a838efb6eeec5815)
