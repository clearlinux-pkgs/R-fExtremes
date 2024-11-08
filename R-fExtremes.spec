#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-fExtremes
Version  : 4032.84
Release  : 49
URL      : https://cran.r-project.org/src/contrib/fExtremes_4032.84.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fExtremes_4032.84.tar.gz
Summary  : Rmetrics - Modelling Extreme Events in Finance
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fBasics
Requires: R-fGarch
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-fBasics
BuildRequires : R-fGarch
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
and modelling extreme events in financial time Series. The

%prep
%setup -q -n fExtremes
pushd ..
cp -a fExtremes buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703260611

%install
export SOURCE_DATE_EPOCH=1703260611
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fExtremes/COPYRIGHT.html
/usr/lib64/R/library/fExtremes/DESCRIPTION
/usr/lib64/R/library/fExtremes/INDEX
/usr/lib64/R/library/fExtremes/Meta/Rd.rds
/usr/lib64/R/library/fExtremes/Meta/data.rds
/usr/lib64/R/library/fExtremes/Meta/features.rds
/usr/lib64/R/library/fExtremes/Meta/hsearch.rds
/usr/lib64/R/library/fExtremes/Meta/links.rds
/usr/lib64/R/library/fExtremes/Meta/nsInfo.rds
/usr/lib64/R/library/fExtremes/Meta/package.rds
/usr/lib64/R/library/fExtremes/NAMESPACE
/usr/lib64/R/library/fExtremes/NEWS.md
/usr/lib64/R/library/fExtremes/R/fExtremes
/usr/lib64/R/library/fExtremes/R/fExtremes.rdb
/usr/lib64/R/library/fExtremes/R/fExtremes.rdx
/usr/lib64/R/library/fExtremes/data/Rdata.rdb
/usr/lib64/R/library/fExtremes/data/Rdata.rds
/usr/lib64/R/library/fExtremes/data/Rdata.rdx
/usr/lib64/R/library/fExtremes/help/AnIndex
/usr/lib64/R/library/fExtremes/help/aliases.rds
/usr/lib64/R/library/fExtremes/help/fExtremes.rdb
/usr/lib64/R/library/fExtremes/help/fExtremes.rdx
/usr/lib64/R/library/fExtremes/help/paths.rds
/usr/lib64/R/library/fExtremes/html/00Index.html
/usr/lib64/R/library/fExtremes/html/R.css
/usr/lib64/R/library/fExtremes/tests/doRUnit.R
/usr/lib64/R/library/fExtremes/unitTests/Makefile
/usr/lib64/R/library/fExtremes/unitTests/runTests.R
/usr/lib64/R/library/fExtremes/unitTests/runit.DataPreprocessing.R
/usr/lib64/R/library/fExtremes/unitTests/runit.ExtremeIndex.R
/usr/lib64/R/library/fExtremes/unitTests/runit.ExtremesData.R
/usr/lib64/R/library/fExtremes/unitTests/runit.GevDistribution.R
/usr/lib64/R/library/fExtremes/unitTests/runit.GevMdaEstimation.R
/usr/lib64/R/library/fExtremes/unitTests/runit.GevModelling.R
/usr/lib64/R/library/fExtremes/unitTests/runit.GevRisk.R
/usr/lib64/R/library/fExtremes/unitTests/runit.GpdDistribution.R
/usr/lib64/R/library/fExtremes/unitTests/runit.GpdModelling.R
/usr/lib64/R/library/fExtremes/unitTests/runit.GpdRisk.R
