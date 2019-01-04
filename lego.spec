%global goipath github.com/xenolf/lego
Version:        1.2.1
%gometa


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
