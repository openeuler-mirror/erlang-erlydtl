%global realname erlydtl
%global upstream erlydtl
Name:		erlang-%{realname}
Version:             0.12.1
Release:             1
BuildArch:           noarch
Summary:             Erlang implementation of the Django Template Language
License:             MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-erlydtl-0001-Verbose-testing.patch
Patch2:		erlang-erlydtl-0002-No-such-function-exported-gettext_compile-write_pret.patch
Patch3:		erlang-erlydtl-0003-No-such-function-exported-gettext_compile-fmt_filein.patch
Patch4:		erlang-erlydtl-0004-No-such-fun-gettext_compile-open_po_file-3.patch
Patch5:		erlang-erlydtl-0005-No-such-fun-gettext_compile-close_file-0.patch
Patch6:		erlang-erlydtl-0006-Support-Erlang-OTP-20.0.patch
Patch7:		erlang-erlydtl-0007-compatibility-with-OTP-21.patch
Patch8:		erlang-erlydtl-0008-merl-bug-in-OTP-21-workaround.patch
Patch9:		erlang-erlydtl-0009-Make-sure-that-when-checking-if-a-function-is-export.patch
Patch10:	erlang-erlydtl-0010-Support-Erlang-OTP-22.0.patch
Provides:            ErlyDTL = %{version}-%{release}
BuildRequires:       erlang-rebar
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
* Sat Aug 29 2020 wangyue <wangyue92@huawei.com> - 0.12.1-1
- package init
