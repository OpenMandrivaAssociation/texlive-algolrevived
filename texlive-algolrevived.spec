%global tl_name algolrevived
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.054
Release:	%{tl_revision}.1
Summary:	A revival of Frutigers Algol alphabet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/algolrevived
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algolrevived.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algolrevived.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package revives Frutiger's Algol alphabet, designed in 1963 for the
code segments in an ALGOL manual. OpenType and type1, regular and medium
weights, upright and slanted. Not monospaced, but good for listings if
you don't need code to be aligned with specific columns. It also makes a
passable but limited text font.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/algolrevived
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/opentype/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/tex/latex/algolrevived
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived
%dir %{_datadir}/texmf-dist/fonts/map/dvips/algolrevived
%dir %{_datadir}/texmf-dist/fonts/opentype/public/algolrevived
%dir %{_datadir}/texmf-dist/fonts/tfm/public/algolrevived
%dir %{_datadir}/texmf-dist/fonts/type1/public/algolrevived
%dir %{_datadir}/texmf-dist/fonts/vf/public/algolrevived
%doc %{_datadir}/texmf-dist/doc/fonts/algolrevived/OFL-FAQ.txt
%doc %{_datadir}/texmf-dist/doc/fonts/algolrevived/OFL.txt
%doc %{_datadir}/texmf-dist/doc/fonts/algolrevived/README
%doc %{_datadir}/texmf-dist/doc/fonts/algolrevived/algolrevived-doc.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/algolrevived/algolrevived-doc.tex
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal0-LY1TT.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal0-OT1TT.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal0-T1TT.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal1-LY1TT.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal1-OT1TT.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal1-T1TT.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_2jqefy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_2mszih.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_2vzrvx.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_4nnq6y.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_4rrrqj.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_5ziufx.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_72x6h3.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_7ov2yu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_ajioas.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_bfgpej.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_ekxevm.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_hqfuhr.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_iky7rf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_jmq5jf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_lxmhqh.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_mdij5b.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_pasij5.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_psjebe.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_q4jbw7.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_qtlmay.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_rj5tka.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_ts1.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_v4trah.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_vawbng.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_wqyrc5.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_wzkcbe.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_yz65wh.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_ziib6p.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/algolrevived/zal_zqbwat.enc
%{_datadir}/texmf-dist/fonts/map/dvips/algolrevived/AlgolRevived.map
%{_datadir}/texmf-dist/fonts/opentype/public/algolrevived/AlgolRevived-Medium.otf
%{_datadir}/texmf-dist/fonts/opentype/public/algolrevived/AlgolRevived-MediumSlanted.otf
%{_datadir}/texmf-dist/fonts/opentype/public/algolrevived/AlgolRevived-Slanted.otf
%{_datadir}/texmf-dist/fonts/opentype/public/algolrevived/AlgolRevived.otf
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-inf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-inf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-inf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-inf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium0-ly1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium0-ot1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium0-t1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium1-ly1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium1-ot1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Medium1-t1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-inf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-inf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-inf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-inf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted0-ly1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted0-ot1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted0-t1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted1-ly1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted1-ot1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-MediumSlanted1-t1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-inf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-inf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-inf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-inf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted0-ly1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted0-ot1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted0-t1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted1-ly1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted1-ot1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-Slanted1-t1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-inf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-inf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-inf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-inf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived0-ly1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived0-ot1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived0-t1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived1-ly1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived1-ot1tt.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/algolrevived/AlgolRevived1-t1tt.tfm
%{_datadir}/texmf-dist/fonts/type1/public/algolrevived/AlgolRevived-Medium.pfb
%{_datadir}/texmf-dist/fonts/type1/public/algolrevived/AlgolRevived-MediumSlanted.pfb
%{_datadir}/texmf-dist/fonts/type1/public/algolrevived/AlgolRevived-Slanted.pfb
%{_datadir}/texmf-dist/fonts/type1/public/algolrevived/AlgolRevived.pfb
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-Medium-inf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-Medium-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-Medium-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-Medium-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-Medium-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-MediumSlanted-inf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-MediumSlanted-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-MediumSlanted-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-MediumSlanted-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-MediumSlanted-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-Slanted-inf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-Slanted-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-Slanted-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-Slanted-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-Slanted-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-inf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/algolrevived/AlgolRevived-ts1.vf
%{_datadir}/texmf-dist/tex/latex/algolrevived/LY1AlgolRevived-Inf.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/LY1AlgolRevived-OsF-TT.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/LY1AlgolRevived-OsF.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/LY1AlgolRevived-Sup.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/LY1AlgolRevived-TLF-TT.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/LY1AlgolRevived-TLF.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/OT1AlgolRevived-Inf.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/OT1AlgolRevived-OsF-TT.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/OT1AlgolRevived-OsF.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/OT1AlgolRevived-Sup.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/OT1AlgolRevived-TLF-TT.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/OT1AlgolRevived-TLF.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/T1AlgolRevived-Inf.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/T1AlgolRevived-OsF-TT.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/T1AlgolRevived-OsF.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/T1AlgolRevived-Sup.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/T1AlgolRevived-TLF-TT.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/T1AlgolRevived-TLF.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/TS1AlgolRevived-OsF.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/TS1AlgolRevived-TLF.fd
%{_datadir}/texmf-dist/tex/latex/algolrevived/algolrevived.fontspec
%{_datadir}/texmf-dist/tex/latex/algolrevived/algolrevived.sty
