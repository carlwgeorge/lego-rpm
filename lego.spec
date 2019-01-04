%global import_path github.com/xenolf/lego

%bcond_with debug

%if %{with debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

Name:           lego
Version:        1.2.1
Release:        1%{?dist}
Summary:        Let's Encrypt client and ACME library written in Go
License:        MIT
URL:            https://github.com/xenolf/lego
Source0:        %{url}/archive/v%{version}/lego-%{version}.tar.gz
ExclusiveArch:  %{go_arches}
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}


%description
%{summary}.


%prep
%autosetup
mkdir -p src/%(dirname %{import_path})
ln -s ../../.. src/%{import_path}


%build
export GOPATH=$(pwd):%{gopath}
export LDFLAGS="-X %{import_path}/main.version=%{version}"
%gobuild -o bin/lego %{import_path}


%install
install -D -m 0755 bin/lego %{buildroot}%{_bindir}/lego


%files
%license LICENSE
%doc README.md
%{_bindir}/lego


%changelog
* Fri Jan 04 2019 Carl George <carl@george.computer> - 1.2.1-1
- Latest upstream

* Tue Feb 06 2018 Carl George <carl@george.computer> - 0.4.1-1
- Initial package
