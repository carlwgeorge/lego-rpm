%global goipath github.com/xenolf/lego
Version:        1.2.1

%if %{defined fedora}
%gometa
%else
ExclusiveArch:  %{go_arches}
BuildRequires:  golang
%global debug_package %{nil}
%global gourl https://%{goipath}
%global gosource %{gourl}/archive/v%{version}/%{name}-%{version}.tar.gz
%define gobuildroot %{expand:
GO_BUILD_PATH=$PWD/_build
install -m 0755 -vd $(dirname $GO_BUILD_PATH/src/%{goipath})
ln -fs $PWD $GO_BUILD_PATH/src/%{goipath}
cd $GO_BUILD_PATH/src/%{goipath}
install -m 0755 -vd _bin
export PATH=$PWD/_bin${PATH:+:$PATH}
export GOPATH=$GO_BUILD_PATH:%{gopath}
}
%define gobuild(o:) %{expand:
%global _dwz_low_mem_die_limit 0
%ifnarch ppc64
go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags %{?__golang_extldflags}'" -a -v -x %{?**};
%else
go build -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags %{?__golang_extldflags}'" -a -v -x %{?**};
%endif
}
%endif


Name:           lego
Release:        1%{?dist}
Summary:        Let's Encrypt client and ACME library written in Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}


%description
%{summary}.


%prep
%autosetup


%build
%gobuildroot
export LDFLAGS="-X %{goipath}/main.version=%{version}"
%gobuild -o _bin/lego %{goipath}


%install
install -D -p -m 0755 _bin/lego %{buildroot}%{_bindir}/lego


%files
%license LICENSE
%doc README.md
%{_bindir}/lego


%changelog
* Fri Jan 04 2019 Carl George <carl@george.computer> - 1.2.1-1
- Latest upstream

* Tue Feb 06 2018 Carl George <carl@george.computer> - 0.4.1-1
- Initial package
