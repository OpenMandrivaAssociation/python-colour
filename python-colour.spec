Name:           python-colour
Version:        0.1.5
Release:        1
Summary:        Python module to convert between color representations (RGB, HSL, web)
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/vaab/colour
Source0:        https://files.pythonhosted.org/packages/source/c/colour/colour-%{version}.tar.gz
BuildRequires:  python-pip
BuildRequires:  python-wheel
BuildArch:      noarch

%description
Python module to convert between color representations:
  * RGB, HSL, 6-digit hex, 3-digit hex, human color
  * One object (Color) or several single purpose functions
    (rgb2hex, hsl2rgb, ...)
  * Web format which uses the smallest representation between
    6-digit (e.g. #fa3b2c), 3-digit (e.g. #fbb), fully spelled
    color (e.g. white), following W3C color naming for compatible
    CSS or HTML color specifications
  * Color scale generation choosing N color gradients
  * It's possible to pick colors to identify objects of the
    application being developed

%prep
%setup -q -n colour-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/colour.py
%{python_sitelib}/colour-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/*
