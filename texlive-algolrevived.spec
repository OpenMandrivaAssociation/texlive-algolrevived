%global tl_name algolrevived
%global tl_revision 77682
%global tl_version 1.054

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A revival of Frutigers Algol alphabet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/algolrevived
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algolrevived.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algolrevived.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package revives Frutiger's Algol alphabet, designed in 1963 for the
code segments in an ALGOL manual. OpenType and type1, regular and medium
weights, upright and slanted. Not monospaced, but good for listings if
you don't need code to be aligned with specific columns. It also makes a
passable but limited text font.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from algolrevived:
Map AlgolRevived.map
TL_DROPIN_EOF
