#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-invgamma
Version  : 1.1
Release  : 27
URL      : https://cran.r-project.org/src/contrib/invgamma_1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/invgamma_1.1.tar.gz
Summary  : The Inverse Gamma Distribution
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
functions for the inverse gamma distribution, wrapping those for the gamma
  distribution in the stats package.

%prep
%setup -q -c -n invgamma
cd %{_builddir}/invgamma

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641037881

%install
export SOURCE_DATE_EPOCH=1641037881
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library invgamma
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library invgamma
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library invgamma
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc invgamma || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/invgamma/DESCRIPTION
/usr/lib64/R/library/invgamma/INDEX
/usr/lib64/R/library/invgamma/Meta/Rd.rds
/usr/lib64/R/library/invgamma/Meta/features.rds
/usr/lib64/R/library/invgamma/Meta/hsearch.rds
/usr/lib64/R/library/invgamma/Meta/links.rds
/usr/lib64/R/library/invgamma/Meta/nsInfo.rds
/usr/lib64/R/library/invgamma/Meta/package.rds
/usr/lib64/R/library/invgamma/NAMESPACE
/usr/lib64/R/library/invgamma/NEWS
/usr/lib64/R/library/invgamma/R/invgamma
/usr/lib64/R/library/invgamma/R/invgamma.rdb
/usr/lib64/R/library/invgamma/R/invgamma.rdx
/usr/lib64/R/library/invgamma/help/AnIndex
/usr/lib64/R/library/invgamma/help/aliases.rds
/usr/lib64/R/library/invgamma/help/invgamma.rdb
/usr/lib64/R/library/invgamma/help/invgamma.rdx
/usr/lib64/R/library/invgamma/help/paths.rds
/usr/lib64/R/library/invgamma/html/00Index.html
/usr/lib64/R/library/invgamma/html/R.css
