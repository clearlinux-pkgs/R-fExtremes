#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fExtremes
Version  : 3042.82
Release  : 37
URL      : https://cran.r-project.org/src/contrib/fExtremes_3042.82.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fExtremes_3042.82.tar.gz
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

%description
and modelling extreme events in financial time Series. The

%prep
%setup -q -c -n fExtremes
cd %{_builddir}/fExtremes

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641014363

%install
export SOURCE_DATE_EPOCH=1641014363
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fExtremes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fExtremes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fExtremes
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fExtremes || :


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
