# revision 15216
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-texinfo
Epoch:		1
Version:	20120224
Release:	11
Summary:	GNU Texinfo
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-texinfo.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-texinfo
Requires:	texlive-collection-basic

%description
TeX macros for the GNU Texinfo documentation system.  The
programs and documentation are no longer distributed with TeX
Live; get the original Texinfo package for your system.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780511
- Update to latest release.
- Import texlive-collection-texinfo
- Import texlive-collection-texinfo

