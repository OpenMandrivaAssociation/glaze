%define debug_package %{nil}

Name:           glaze
Version:        5.3.1
Release:        1
Summary:        JSON library for modern C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/stephenberry/glaze
Source0:        https://github.com/stephenberry/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description
Glaze is a JSON library that reads/writes from/to object memory.
It also supports BEVE and CSV.

%description devel
Glaze is a JSON library that reads/writes from/to object memory. It
supports BEVE and CSV as well.

Glaze utilizes SIMD (SSE/AVX/NEON) and deals well with
out-of-sequence data and missing keys. Based on an August 2024
measurement on an Apple M1 CPU, it was measured at 1224/1366 MB/s,
outperforming other implementations like yyjson-0.10.0 by 10/35%% and
rapidjson-1.1.0 by 172/371%% (read/write speeds, respectively).

This subpackage contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake \
	-DBUILD_TESTING=OFF \
	-Dglaze_DEVELOPER_MODE=OFF \
	-Dglaze_ENABLE_FUZZING=OFF

%make_build

%install
%make_install -C build

%files devel
%license LICENSE
%doc README.md
%doc docs
%{_includedir}/%{name}
%{_datadir}/%{name}
