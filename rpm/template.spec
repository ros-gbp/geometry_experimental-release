Name:           ros-jade-tf2
Version:        0.5.8
Release:        0%{?dist}
Summary:        ROS tf2 package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/tf2
Source0:        %{name}-%{version}.tar.gz

Requires:       console-bridge-devel
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-rostime
Requires:       ros-jade-tf2-msgs
BuildRequires:  console-bridge-devel
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-rostime
BuildRequires:  ros-jade-tf2-msgs

%description
tf2 is the second generation of the transform library, which lets the user keep
track of multiple coordinate frames over time. tf2 maintains the relationship
between coordinate frames in a tree structure buffered in time, and lets the
user transform points, vectors, etc between any two coordinate frames at any
desired point in time.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Mar 17 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.8-0
- Autogenerated by Bloom

* Tue Jan 13 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.7-0
- Autogenerated by Bloom

