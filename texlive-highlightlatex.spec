Name:		texlive-highlightlatex
Version:	58392
Release:	2
Summary:	Syntax highlighting for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/highlightlatex
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/highlightlatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/highlightlatex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides extensive colored syntax highlighting for
LaTeX. For this purpose it builds on the generic listings
package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/highlightlatex
%doc %{_texmfdistdir}/doc/latex/highlightlatex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
