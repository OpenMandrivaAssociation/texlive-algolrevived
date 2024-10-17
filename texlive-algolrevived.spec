Name:		texlive-algolrevived
Version:	71368
Release:	1
Summary:	A revival of Frutiger's Algol alphabet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/algolrevived
License:	ofl lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algolrevived.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algolrevived.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package revives Frutiger's Algol alphabet, designed in 1963
for the code segments in an ALGOL manual. OpenType and type1,
regular and medium weights, upright and slanted. Not
monospaced, but good for listings if you don't need code to be
aligned with specific columns. It also makes a passable but
limited text font.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/algolrevived
%{_texmfdistdir}/fonts/vf/public/algolrevived
%{_texmfdistdir}/fonts/type1/public/algolrevived
%{_texmfdistdir}/fonts/tfm/public/algolrevived
%{_texmfdistdir}/fonts/opentype/public/algolrevived
%{_texmfdistdir}/fonts/map/dvips/algolrevived
%{_texmfdistdir}/fonts/enc/dvips/algolrevived
%doc %{_texmfdistdir}/doc/fonts/algolrevived

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
