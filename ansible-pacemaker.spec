Name:           ansible-pacemaker
Version:        0.1
Release:        1%{?dist}
Summary:        Ansible modules for managing Pacemaker clusters

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/redhat-openstack/ansible-pacemaker/README.md
Source0:        https://github.com/redhat-openstack/ansible-pacemaker

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
%setup -q


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install 


%files
%doc README*
%license LICENSE



%changelog
