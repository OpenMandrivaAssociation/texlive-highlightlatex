%global tl_name highlightlatex
%global tl_revision 58392

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Syntax highlighting for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/highlightlatex
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/highlightlatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/highlightlatex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides extensive colored syntax highlighting for LaTeX.
For this purpose it builds on the generic listings package.

