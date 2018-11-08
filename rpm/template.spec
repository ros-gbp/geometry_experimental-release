Name:           ros-melodic-tf2-bullet
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS tf2_bullet package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/tf2_bullet
Source0:        %{name}-%{version}.tar.gz

Requires:       bullet-devel
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-tf2
BuildRequires:  bullet-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-melodic-catkin >= 0.5.68
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-tf2

%description
tf2_bullet

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Nov 08 2018 Tully Foote <tfoote@osrfoundation.org> - 0.6.4-0
- Autogenerated by Bloom

* Mon Jul 09 2018 Tully Foote <tfoote@osrfoundation.org> - 0.6.3-0
- Autogenerated by Bloom

* Wed May 02 2018 Tully Foote <tfoote@osrfoundation.org> - 0.6.2-0
- Autogenerated by Bloom

* Wed Mar 21 2018 Tully Foote <tfoote@osrfoundation.org> - 0.6.1-0
- Autogenerated by Bloom

* Wed Mar 21 2018 Tully Foote <tfoote@osrfoundation.org> - 0.6.0-0
- Autogenerated by Bloom

* Wed Mar 21 2018 Tully Foote <tfoote@osrfoundation.org> - 0.5.17-1
- Autogenerated by Bloom

* Wed Mar 21 2018 Tully Foote <tfoote@osrfoundation.org> - 0.5.17-0
- Autogenerated by Bloom

