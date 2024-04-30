Name:           cocotb
Version:        1.8.1
Release:        1%{?dist}
Summary:        Coroutine based cosimulation library for writing VHDL and Verilog
License:        BSD
URL:            https://cocotb.org
Source0:        https://github.com/cocotb/cocotb/archive/v%{version}.tar.gz

BuildRequires:  git gcc-c++ make python3-devel python3-setuptools

%description
Cocotb is a coroutine based cosimulation library
for writing VHDL and Verilog testbenches in Python.

%package        python3
Summary:        %{summary}
Provides:       cocotb

%description    python3
Cocotb is a coroutine based cosimulation library
for writing VHDL and Verilog testbenches in Python.


%prep
%autosetup -n %{cocotb}-%{version}

%build
sed -i '/-rpath/d' cocotb_build_libs.py
sed -i 's|"-static-libstdc++"||g' cocotb_build_libs.py
%py3_build


%install
%py3_install


%files python3
%license LICENSE
%doc README.md
%{_bindir}/*
%{python3_sitearch}/*


%changelog
