%global realname erlydtl
%global upstream erlydtl
Name:		erlang-%{realname}
Version:        0.14.0
Release:        1
BuildArch:      noarch
Summary:        Erlang implementation of the Django Template Language
License:        MIT and Apache-2..0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/refs/tags/0.14.0.tar.gz
Patch1:		erlang-erlydtl-0001-Verbose-testing.patch
Patch2:		erlang-erlydtl-0002-No-such-function-exported-gettext_compile-write_pret.patch
Patch3:		erlang-erlydtl-0003-No-such-function-exported-gettext_compile-fmt_filein.patch
Patch4:		erlang-erlydtl-0004-No-such-fun-gettext_compile-open_po_file-3.patch
Patch5:		erlang-erlydtl-0005-No-such-fun-gettext_compile-close_file-0.patch
Provides:       ErlyDTL = %{version}-%{release}
BuildRequires:  erlang-rebar


%description
ErlyDTL is an Erlang implementation of the Django Template Language. The
erlydtl module compiles Django Template source code into Erlang bytecode. The
compiled template has a "render" function that takes a list of variables and
returns a fully rendered document.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}
cp -arv priv %{buildroot}/%{erlang_appdir}/


%check
%{erlang_test -C rebar-tests.config}


%files
%license LICENSE
%doc CONTRIBUTING.md NEWS.md README.markdown README_I18N
%{erlang_appdir}/


%changelog
* Fri Jan 21 2022 Ge Wang <wangge20@huawei.com> - 1.14.0-1
- update to version 1.14.0

* Sat Aug 29 2020 wangyue <wangyue92@huawei.com> - 1.12.1-1
- package init
